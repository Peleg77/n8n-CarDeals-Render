#!/usr/bin/env python3
"""
מודל יוניט-אקונומיקס פרמטרי ליחידת דרופשיפינג (חשבון IG + מוצר + חנות).

הרצה:
    python3 unit_economics.py                    # שלושה תרחישים + רגישויות
    python3 unit_economics.py --params my.json   # פרמטרים משלך
    python3 unit_economics.py --dump             # מייצא את פרמטרי ברירת המחדל ל-JSON

הכל stdlib. אין תלויות.
"""

import argparse
import json
import sys
from dataclasses import dataclass, asdict, replace


# ---------------------------------------------------------------- פרמטרים

@dataclass
class Params:
    name: str = "base"

    # --- ראש המשפך ---
    views_month: float = 500_000        # צפיות חודשיות מצטברות בכל החשבון
    view_to_session: float = 0.0050     # צפייה → סשן באתר (כולל אוטומציית DM)

    # --- המרה ---
    cvr: float = 0.012                  # סשן → הזמנה משולמת
    aov: float = 42.0                   # ערך הזמנה ממוצע כולל באנדל/אפסייל

    # --- עלות ישירה להזמנה ---
    cogs: float = 8.0                   # עלות סחורה לספק (לפני מכס)
    shipping: float = 4.0               # שילוח ללקוח (מחסן אמריקאי)
    duty: float = 3.0                   # מכס/אגרות ליחידה — אחרי ביטול de minimis
    support_cost: float = 0.40          # עלות שירות לקוחות משתנה להזמנה

    # --- סליקה ---
    pay_pct: float = 0.049              # 2.9% סולק + 2.0% עמלת צד-ג' של Shopify
    pay_fixed: float = 0.30

    # --- דליפות ---
    refund_rate: float = 0.060          # החזרות/ביטולים (הסחורה לא חוזרת)
    chargeback_rate: float = 0.008
    chargeback_fee: float = 20.0        # אגרת מחלוקת לסולק

    # --- עלויות קבועות חודשיות ---
    fixed_shopify: float = 39.0
    fixed_apps: float = 50.0            # ManyChat, הלפדסק, אפליקציית באנדל
    fixed_ai_tools: float = 60.0
    fixed_other: float = 25.0

    # --- זמן ---
    hours_month: float = 26.0           # שעות אישיות בחודש (6 ש'/שבוע)

    @property
    def fixed_total(self) -> float:
        return (self.fixed_shopify + self.fixed_apps
                + self.fixed_ai_tools + self.fixed_other)


# ---------------------------------------------------------------- חישוב

def compute(p: Params) -> dict:
    sessions = p.views_month * p.view_to_session
    orders = sessions * p.cvr

    revenue = orders * p.aov

    # דליפות. הסחורה נשלחה ולא חוזרת, והעמלות לא מוחזרות.
    refunds = orders * p.refund_rate * p.aov
    chargebacks = orders * p.chargeback_rate * (p.aov + p.chargeback_fee)

    # עלות ישירה משולמת על כל הזמנה, כולל הזמנות שיוחזרו
    unit_direct = p.cogs + p.shipping + p.duty + p.support_cost
    cogs_total = orders * unit_direct

    fees = orders * (p.aov * p.pay_pct + p.pay_fixed)

    gross_contrib = revenue - refunds - chargebacks - cogs_total - fees
    net = gross_contrib - p.fixed_total

    return {
        "name": p.name,
        "sessions": sessions,
        "orders": orders,
        "revenue": revenue,
        "refunds": -refunds,
        "chargebacks": -chargebacks,
        "cogs_total": -cogs_total,
        "fees": -fees,
        "fixed": -p.fixed_total,
        "gross_contrib": gross_contrib,
        "net": net,
        "contrib_per_order": (gross_contrib / orders) if orders else 0.0,
        "net_margin": (net / revenue) if revenue else 0.0,
        "net_per_hour": (net / p.hours_month) if p.hours_month else 0.0,
        "breakeven_orders": (p.fixed_total / (gross_contrib / orders))
                            if orders and gross_contrib > 0 else float("inf"),
    }


def breakeven_views(p: Params) -> float:
    """כמה צפיות בחודש דרושות רק כדי לכסות את העלויות הקבועות."""
    r = compute(p)
    if r["orders"] <= 0 or r["contrib_per_order"] <= 0:
        return float("inf")
    orders_needed = p.fixed_total / r["contrib_per_order"]
    return orders_needed / (p.cvr * p.view_to_session)


# ---------------------------------------------------------------- תרחישים

def scenarios() -> list:
    base = Params(name="בסיס")

    pess = replace(
        base, name="פסימי",
        views_month=150_000, view_to_session=0.0015, cvr=0.007,
        aov=34.0, cogs=10.0, shipping=5.0, duty=6.0,
        refund_rate=0.10, chargeback_rate=0.018,
        fixed_apps=50.0, hours_month=34.0,
    )
    opt = replace(
        base, name="אופטימי",
        views_month=2_000_000, view_to_session=0.0100, cvr=0.020,
        aov=48.0, cogs=8.5, shipping=3.5, duty=1.5,
        refund_rate=0.04, chargeback_rate=0.004,
        fixed_apps=90.0, fixed_other=60.0, hours_month=30.0,
    )
    return [pess, base, opt]


# ---------------------------------------------------------------- פלט

def money(x: float) -> str:
    return f"${x:,.0f}"


def print_table(results: list, params: list) -> None:
    names = [r["name"] for r in results]
    w = 16

    def row(label, vals):
        print(f"{label:<26}" + "".join(f"{v:>{w}}" for v in vals))

    print("\n" + "=" * (26 + w * len(names)))
    print(f"{'יוניט-אקונומיקס · לחודש':<26}" + "".join(f"{n:>{w}}" for n in names))
    print("=" * (26 + w * len(names)))

    row("צפיות", [f"{p.views_month:,.0f}" for p in params])
    row("צפייה→סשן", [f"{p.view_to_session*100:.2f}%" for p in params])
    row("סשנים", [f"{r['sessions']:,.0f}" for r in results])
    row("CVR", [f"{p.cvr*100:.2f}%" for p in params])
    row("הזמנות", [f"{r['orders']:,.1f}" for r in results])
    row("AOV", [money(p.aov) for p in params])
    print("-" * (26 + w * len(names)))
    row("הכנסה", [money(r["revenue"]) for r in results])
    row("  החזרות", [money(r["refunds"]) for r in results])
    row("  צ'ארג'בקים", [money(r["chargebacks"]) for r in results])
    row("  סחורה+משלוח+מכס", [money(r["cogs_total"]) for r in results])
    row("  עמלות סליקה", [money(r["fees"]) for r in results])
    print("-" * (26 + w * len(names)))
    row("תרומה שולית", [money(r["gross_contrib"]) for r in results])
    row("  עלויות קבועות", [money(r["fixed"]) for r in results])
    print("-" * (26 + w * len(names)))
    row("*** נטו לחודש ***", [money(r["net"]) for r in results])
    row("תרומה להזמנה", [f"${r['contrib_per_order']:.2f}" for r in results])
    row("שיעור רווח נטו", [f"{r['net_margin']*100:.1f}%" for r in results])
    row("שעות אישיות/חודש", [f"{p.hours_month:.0f}" for p in params])
    row("נטו לשעה", [f"${r['net_per_hour']:.1f}" for r in results])
    print("-" * (26 + w * len(names)))
    row("הזמנות לאיזון", [f"{r['breakeven_orders']:.1f}"
                          if r["breakeven_orders"] != float("inf") else "לא ניתן"
                          for r in results])
    row("צפיות לאיזון", [f"{breakeven_views(p):,.0f}"
                         if breakeven_views(p) != float("inf") else "לא ניתן"
                         for p in params])
    print("=" * (26 + w * len(names)) + "\n")


def sensitivity(base: Params) -> None:
    """רגישות הנטו החודשי לשינוי של ±30% בכל פרמטר לחוד."""
    fields = [
        ("views_month", "צפיות חודשיות"),
        ("view_to_session", "צפייה→סשן"),
        ("cvr", "CVR"),
        ("aov", "AOV"),
        ("cogs", "עלות סחורה"),
        ("shipping", "משלוח"),
        ("duty", "מכס ליחידה"),
        ("pay_pct", "אחוז סליקה"),
        ("refund_rate", "שיעור החזרות"),
        ("chargeback_rate", "שיעור צ'ארג'בק"),
    ]
    b = compute(base)["net"]
    print("רגישות · שינוי בנטו החודשי מול תרחיש הבסיס")
    print(f"(בסיס = {money(b)})\n")
    print(f"{'פרמטר':<22}{'-30%':>14}{'+30%':>14}{'טווח':>14}")
    print("-" * 64)

    rows = []
    for f, label in fields:
        cur = getattr(base, f)
        lo = compute(replace(base, **{f: cur * 0.7}))["net"]
        hi = compute(replace(base, **{f: cur * 1.3}))["net"]
        rows.append((label, lo - b, hi - b, abs(hi - lo)))

    for label, dlo, dhi, span in sorted(rows, key=lambda r: -r[3]):
        print(f"{label:<22}{money(dlo):>14}{money(dhi):>14}{money(span):>14}")
    print()


def realistic_range(base: Params) -> None:
    """
    רגישות על טווחי אי-ודאות אמיתיים, לא על +-30% שרירותי.
    זו הטבלה הנכונה: רגישות של +-30% מתייחסת לכל הפרמטרים כאילו
    אי-הוודאות שלהם זהה, וזה פשוט לא נכון. view_to_session נע בין
    פי 0.3 לפי 2 מהבסיס; AOV נע בקושי ב-15% לכל כיוון.
    """
    ranges = [
        ("צפיות חודשיות", "views_month", 150_000, 2_000_000),
        ("צפייה→סשן", "view_to_session", 0.0015, 0.0100),
        ("CVR", "cvr", 0.007, 0.020),
        ("AOV", "aov", 34.0, 48.0),
        ("עלות סחורה", "cogs", 6.0, 12.0),
        ("מכס ליחידה", "duty", 0.0, 7.0),
        ("אחוז סליקה", "pay_pct", 0.029, 0.062),
        ("שיעור החזרות", "refund_rate", 0.03, 0.12),
    ]
    b = compute(base)["net"]
    print("רגישות על טווחי אי-ודאות אמיתיים · נטו חודשי")
    print(f"(בסיס = {money(b)}. כל שורה: משנים פרמטר אחד לקצוות הטווח האמיתי שלו)\n")
    print(f"{'פרמטר':<22}{'קצה נמוך':>16}{'קצה גבוה':>16}{'טווח נטו':>16}")
    print("-" * 70)
    rows = []
    for label, f, lo_v, hi_v in ranges:
        lo = compute(replace(base, **{f: lo_v}))["net"]
        hi = compute(replace(base, **{f: hi_v}))["net"]
        rows.append((label, lo, hi, abs(hi - lo)))
    for label, lo, hi, span in sorted(rows, key=lambda r: -r[3]):
        print(f"{label:<22}{money(lo):>16}{money(hi):>16}{money(span):>16}")
    print()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", help="קובץ JSON עם פרמטרים לתרחיש הבסיס")
    ap.add_argument("--dump", action="store_true",
                    help="הדפס את פרמטרי ברירת המחדל כ-JSON וצא")
    args = ap.parse_args()

    if args.dump:
        print(json.dumps(asdict(Params()), indent=2, ensure_ascii=False))
        return 0

    scen = scenarios()
    if args.params:
        with open(args.params, encoding="utf-8") as fh:
            override = json.load(fh)
        scen[1] = replace(scen[1], **override)

    print_table([compute(p) for p in scen], scen)
    sensitivity(scen[1])
    realistic_range(scen[1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
