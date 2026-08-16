# סוכני AI שהרוויחו כסף אמיתי — תחקיר מקורות פומביים

**תאריך עריכה:** 16 באוגוסט 2026
**היקף:** 13 קטגוריות, ~50 שאילתות חיפוש, 50 מקרים מתועדים
**מתודולוגיה:** כל טענה מספרית מקושרת למקור ישיר. הופרד במפורש בין *מה שהמקור טוען* לבין *מה שניתן לאמת חיצונית*.

---

## הערה מקדימה על מגבלות המחקר

שלושה סייגים שחייבים להיאמר לפני הנתונים:

1. **Hacker News ו-hn.algolia.com חסומים ברמת רשת בסביבה הזו.** תוכן HN נגיש רק דרך תוצאות חיפוש עקיפות. אותו דבר לגבי `anthropic.com` — נאלצתי להסתמך על סיקור משני של פרסומי Anthropic. זה מוריד את איכות האימות בכמה מקרים, וסימנתי זאת היכן שרלוונטי.
2. **"רווח נטו" כמעט אף פעם לא מדווח.** ברוב המכריע של המקרים דווחה הכנסה ברוטו בלבד. עלויות API, שרתים, פרסום ועמלות — נעדרות. היכן שהעלויות כן דווחו, זה מסומן.
3. **הטיית שרידות מובנית.** מי שהפסיד לא כותב תרד. המקרים ה"מוצלחים" בדרגות C/D הם מדגם מוטה באופן קיצוני.

---

# חלק א' — טבלת ריכוז

ממוינת לפי דרגת אמינות, ובתוך כל דרגה לפי סכום.

## דרגה A — מאומת

| # | שם המקרה/היוצר | קטגוריה | סכום שדווח | חלון זמן | אוטונומיה | קישור |
|---|---|---|---|---|---|---|
| 1 | **Claude Code / Anthropic** | מטה (מכירת כלים) | $8B ARR (מאי 2026); $2.5B (פבר' 2026) | 2025–2026 | A1 | [mindstudio](https://www.mindstudio.ai/blog/claude-code-2-5-billion-annualized-revenue-saas-comparison) |
| 2 | **Clanker / tokenbot** | סוכני-טוקנים | $34.4M עמלות מצטברות (אוג' 2025); >$50M; שיא $8.02M בשבוע (פבר' 2026) | 11/2024–2026 | A3 | [Cointelegraph](https://cointelegraph.com/news/clanker-ai-memecoin-fees-355k-tokens), [KuCoin](https://www.kucoin.com/news/articles/clanker-protocol-reaches-8-million-weekly-fee-milestone-as-ai-agent-social-trading-ignites-base) |
| 3 | **Michael Smith** (הונאת סטרימינג) | מוזיקה AI — **פלילי** | **$10M+** תמלוגים | 2017–2024 | A3 | [Forbes](https://www.forbes.com/sites/lesliekatz/2024/09/08/man-charged-with-10-million-streaming-scam-using-ai-generated-songs/), [BleepingComputer](https://www.bleepingcomputer.com/news/security/musician-pleads-guilty-to-10m-streaming-fraud-powered-by-ai-bots/) |
| 4 | **x402 (Coinbase)** | תשלומי agent-to-agent | ~$50M נפח מצטבר; 165M עסקאות; 69,000 סוכנים | 2025–04/2026 | A4 | [Chainalysis](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/), [CryptoAdventure](https://cryptoadventure.com/coinbase-says-x402-has-processed-160m-agentic-payments/) |
| 5 | **Adavia Davis** (רשת YouTube) | תוכן ומדיה | ~$700k/שנה ברוטו; $40–60k/חודש; עלויות ~$6.5k/חודש | 2024–2025 | A3 | [Fortune](https://www.fortune.com/2025/12/30/ai-slop-faceless-youtube-accounts-adavia-davis-user-generated-content), [Yahoo](https://finance.yahoo.com/news/22-old-college-dropout-making-145733283.html) |
| 6 | **Truth Terminal** (מענק) | קריפטו | **$50,000** ב-BTC ממארק אנדריסן | 09/07/2024 | A4 | [TechCrunch](https://techcrunch.com/2024/12/19/the-promise-and-warning-of-truth-terminal-the-ai-bot-that-secured-50000-in-bitcoin-from-marc-andreessen/), [Protos](https://protos.com/marc-andreessen-gave-an-ai-agent-50000-of-bitcoin-it-endorsed-goat/) |
| 7 | **Freysa** | קריפטו / משחק יריב | $47,000 (13.19 ETH) — **הסוכן הפסיד, אדם זכה** | 22–29/11/2024 | A5 | [The Block](https://www.theblock.co/post/328747/human-player-outwits-freysa-ai-agent-in-47000-crypto-challenge) |
| 8 | **Nof1 Alpha Arena** עונה 1 | מסחר קריפטו | $10,000 לכל מודל. סופי: Qwen3 Max $12,231 (+22.3%), DeepSeek $10,489 (+4.9%), Claude 4.5 $5,799, Gemini $5,445. **4 מ-6 בהפסד** | 18/10–03/11/2025 | A5 | [iWeaver](https://www.iweaver.ai/blog/alpha-arena-ai-trading-season-1-results/), [SCMP](https://www.scmp.com/tech/tech-trends/article/3330461/deepseek-and-qwen-ai-models-crush-western-rivals-cryptocurrency-trading-challenge) |
| 9 | **Anthropic Project Deal** | מטה / מסחר סוכנים | >$4,000 ב-186 עסקאות, 69 סוכנים, $100 תקציב לכל אחד | שבוע ב-12/2025 | A4 | [Anthropic](https://www.anthropic.com/features/project-deal), [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-ran-a-marketplace-and-bots-closed-every-deal/) |
| 10 | **AI Village / Sage** | ניסוי מחקרי | $2,000 לצדקה ($1,481 + $503) | 04–05/2025 | A4 | [AI Digest](https://theaidigest.org/village/blog/season-recap-agents-raise-2k), [TIME](https://time.com/7330795/ai-village-chatgpt-gemini-claude/) |
| 11 | **XBOW** | באגים ואבטחה | ~1,060 דיווחי פגיעויות, #1 בלוח HackerOne ארה"ב. **הפרסים קטנים מעלות ה-inference** | Q2 2025–2026 | A4 | [Slashdot](https://it.slashdot.org/story/25/07/05/1847237/xbows-ai-powered-pentester-grabs-top-rank-on-hackerone-raises-75m-to-grow-platform), [CyberScoop](https://cyberscoop.com/is-xbows-success-the-beginning-of-the-end-of-human-led-bug-hunting-not-yet/) |
| 12 | **HackerOne "hackbots"** | באגים ואבטחה | 560 דיווחים תקפים מסוכנים אוטונומיים (מתוך $81M ששולמו בפלטפורמה כולה) | 2025–2026 | A4 | [CybersecurityNews](https://cybersecuritynews.com/hackerone-bug-bounty-paid/) |
| 13 | **Anthropic Project Vend** שלב 1 | ניסוי מחקרי | **הפסד ~$200** ($1,000 → <$800) | ~30 יום, 2025 | A5 | [TechCrunch](https://techcrunch.com/2025/06/28/anthropics-claude-ai-became-a-terrible-business-owner-in-experiment-that-got-weird), [Futurism](https://futurism.com/future-society/vending-machine-claude-disaster) |
| 14 | **Project Vend** שלב 2 (Claudius Sennet) | ניסוי מחקרי | **הפסד ~$1,000** — פשיטת רגל | 12/2025 | A5 | [Anthropic](https://www.anthropic.com/research/project-vend-2), [Futurism](https://futurism.com/future-society/anthropic-ai-vending-machine) |
| 15 | **Sakana AI Scientist v2** | מחקר | $0 הכנסה. עלות ~$15–20 למאמר. מאמר התקבל ל-ICLR workshop (6.3/10) ונמשך | 2024–2025 | A4 | [R&D World](https://www.rdworldonline.com/sakana-ai-claims-first-fully-ai-generated-paper-passes-peer-review-at-top-ai-conference/), [arXiv ביקורת](https://arxiv.org/pdf/2502.14297) |
| 16 | **Google Big Sleep** | אבטחה | $0 ישיר. CVE-2025-6965 ב-SQLite שאותר אוטונומית | 11/2024–2025 | A4 | [SecurityOnline](https://securityonline.info/google-threat-intel-ai-generated-zero-day-exploit-big-sleep/) |
| 17 | **OpenAI Aardvark / Codex Security** | אבטחה | $0 ישיר. ≥10 CVEs בקוד פתוח | 10/2025–03/2026 | A4 | [OpenAI](https://openai.com/index/introducing-aardvark/), [HackerNews](https://thehackernews.com/2025/10/openai-unveils-aardvark-gpt-5-agent.html) |
| 18 | **GPT-4 / ARC Evals — TaskRabbit** | ניסוי מחקרי | **הוציא** כסף לשכירת אדם, לא הרוויח | 03/2023 | A4 | [GPT-4 System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf), [METR](https://metr.org/blog/2023-03-18-update-on-recent-evals/) |
| 19 | **Vending-Bench / Vending-Bench 2** | סימולציה | לא כסף אמיתי. Grok 4: שווי נקי ממוצע $4,694.15 מול בסיס אנושי $844.05 | 02/2025–2026 | — | [arXiv](https://arxiv.org/html/2502.15840v1), [Andon Labs](https://andonlabs.com/evals/vending-bench-2) |
| 20 | **TheAgentCompany** (בנצ'מרק) | ניסוי מחקרי | Gemini 2.5 Pro: 30.3% השלמה מלאה; Claude 3.7: 26.3%; GPT-4o: 8.6% | 12/2024–2025 | — | [arXiv](https://arxiv.org/abs/2412.14161), [NeurIPS](https://neurips.cc/virtual/2025/poster/121705) |
| 21 | **METR RCT** | ניסוי מחקרי | מפתחים מנוסים **19% איטיים יותר** עם AI; האמינו שהם 20% מהירים יותר | 07/2025 | A2 | [Let's Data Science](https://letsdatascience.com/blog/developers-thought-ai-made-them-faster-the-data-said-otherwise) |
| 22 | **"SEO Heist"** (Jake Ward / Byword) | SEO | 3.6M ביקורים (489,509 באוקטובר בלבד). **הכנסה מעולם לא נחשפה.** קריסה: ~620k → ~116k ביקורים, -42% אורגני | 11/2023–2024 | A3 | [X thread](https://x.com/jakezward/status/1728032634037567509), [The Decoder](https://the-decoder.com/ai-powered-seo-heist-copying-website-loses-significant-google-traffic/) |
| 23 | **MIT State of AI in Business** | מטה | 95% מפיילוטי GenAI ללא השפעה מדידה על ה-P&L (מתוך $30–40B השקעה) | 2025 | — | [סיכום](https://medium.com/@Fransantolo/95-of-corporate-generative-ai-projects-fail-mit-study-finds-47ad5d50db32) |

## דרגה B — סביר

| # | שם המקרה/היוצר | קטגוריה | סכום שדווח | חלון זמן | אוטונומיה | קישור |
|---|---|---|---|---|---|---|
| 24 | **Bankr** | קריפטו | ~$5B נפח, >$30M עמלות (לפי הפרויקט; ניתן לאימות on-chain, לא אומת כאן) | ~18 חודשים עד 2026 | A3 | [Bankr Docs](https://docs.bankr.chat/) |
| 25 | **Virtuals ACP** | מטה | $479M "Agentic GDP", 1.77M משימות שהושלמו — **מדווח עצמית, לא אומת חיצונית** | 2025–04/2026 | A4 | [BlockEden](https://blockeden.xyz/blog/2026/04/21/agdp-agent-gdp-virtuals-protocol-ai-blockchain-valuation-primitive-tvl-displacement/) |
| 26 | **Truth Terminal** (ארנק GOAT) | סוכני-טוקנים | $20k airdrop → >$500k (10/2024); דווח שיא ~$37.6M. **שווי לא ממומש** | 10/2024–2025 | A4 | [Coinspeaker](https://www.coinspeaker.com/ai-bot-truth-terminal-500k-20k-investment-solana-meme-coin/), [Arkham](https://info.arkm.com/research/the-first-ai-millionaire) |
| 27 | **בוטים ב-Polymarket** | שווקי חיזוי | 14 מ-20 הארנקים הרווחיים ביותר הם בוטים; >30% מהפעילות; 37% מהסוכנים ברווח מול 7–13% מבני אדם | 2025–2026 | A5 | [NYC Servers](https://newyorkcityservers.com/blog/ai-agents-prediction-market-trading) |
| 28 | **Aitana Lopez** (The Clueless) | תוכן / משפיענית AI | €3,000/חודש ממוצע, עד €10,000/חודש שיא | 11/2023–2025 | A1 | [Yahoo Finance](https://finance.yahoo.com/news/ai-influencers-making-secretive-creators-121608358.html) |
| 29 | **Nathan Smith — ChatGPT Micro-Cap** | מסחר מניות | $100 הון התחלתי. +24–25% ב-4 שבועות; +32% ב-10 שבועות (≈$32 רווח מוחלט) | 06/2025+ | A2 | [GitHub + לוגים](https://github.com/LuckyOne7777/ChatGPT-Micro-Cap-Experiment), [Decrypt](https://decrypt.co/332826/high-school-students-chatgpt-trading-bot) |
| 30 | **Disarray** (סוכן Kaggle) | גיימינג/תחרויות | 28 מדליות, top-10 ב-9 תחרויות, ניצח את כל הצוותים האנושיים באחת. **פרסים כספיים לא דווחו** | 04/2026 | A4 | [AI Dynamics](https://artificialintelligencedynamics.com/2026/04/09/disarray-ai-agent-wins-28-medals-in-kaggle-competitions/) |
| 31 | **HSE — NeuroGolf Kaggle** | תחרויות | מדליית זהב, 330 סוכני ChatGPT פתרו 400 חידות. פרס לא דווח | 2026 | A3 | [HSE](https://www.hse.ru/en/news/edu/1189861913.html) |
| 32 | **Luna (Virtuals)** | קריפטו | שילמה $1,000 למעריץ מארנק Base משלה — **הוציאה**, לא הרוויחה | 10/2024 | A4 | [Virtuals on X](https://x.com/virtuals_io/status/1849841392241283559), [Whitepaper](https://whitepaper.virtuals.io/about-virtuals-1/what-are-virtual-agents/ip-agents-vs-functional-agents/highlight-luna-ip-agent) |

## דרגה C — טענה בלבד

| # | שם המקרה/היוצר | קטגוריה | סכום שדווח | חלון זמן | אוטונומיה | קישור |
|---|---|---|---|---|---|---|
| 33 | **בוט OpenClaw ב-Polymarket** | שווקי חיזוי | $115,000 בשבוע; ארנק 0x8dxd — $1.7M ב-20,000+ עסקאות. ירד ל-$5–15k/שבוע במרץ 2026 | ראשית 2026 | A5 | [OpenClaws blog](https://openclaws.io/blog/polymarket-trading-bot/) |
| 34 | **"$100k in 6 months" (פרילנסר)** | פרילנס | $100,000 — אנונימי, ללא ראיה | 2025 | A2 | [dev.to](https://dev.to/agami_tech_414cabb7522ea1/how-a-freelancer-earned-100k-using-agentic-ai-1pb3) |
| 35 | **סוכנות n8n — $25k MRR** | n8n / no-code | $25,000/חודש תוך 4 חודשים — מקור Reddit ממוחזר | 2025–2026 | A3 | [BrowserAct](https://www.browseract.com/blog/best-high-income-case-analysis-how-to-achieve-25000-monthly-revenue-with-n8n) |
| 36 | **מפעל pSEO — 512 עמודים** | SEO | $48,000 הכנסה, $41,000 עלות, 18 חודשים. **טענת "14x ROI" סותרת את המספרים שלה** | 18 חודשים | A3 | [thestacc](https://thestacc.com/blog/programmatic-seo-case-study/) |
| 37 | **Devrim Ozcay — SaaS ב-3 ימים** | מוצרי תוכנה | $2,400 MRR בשבוע 3, $60 קרדיטים | 2025–2026 | A2 | [Stackademic](https://blog.stackademic.com/i-built-a-saas-in-3-days-using-claude-code-it-makes-2-400-month-heres-the-entire-process-0af017932f9c) |
| 38 | **Krystal Wascher — KDP** | Kindle/KDP | $2,597 בחודש השני, 10 ספרים, $53 פרסום | 2023–2024 | A2 | [בלוג אישי](https://krystalwascher.com/narrator-blog/how-i-made-2597-in-my-2nd-month-on-amazon-kdp) |
| 39 | **"AI ניהל את חנות הדרופשיפינג שלי 30 יום"** | מסחר אלקטרוני | $800 רווח ב-30 יום | 2025–2026 | A3 | [Medium](https://medium.com/@sanjay_84274/case-study-i-let-ai-run-my-dropshipping-store-for-30-days-56d935c776bc) |
| 40 | **"$10K MRR ב-47 יום" (מייסד בליסבון)** | מוצרי תוכנה | $10,000 MRR — אנונימי, ממקור שני | 2026 | A2 | [MindStudio](https://www.mindstudio.ai/blog/build-saas-with-ai-agents-1m-arr-case-study) |
| 41 | **תיקי AI SDR של ספקים** | לידג'ן | NextGen Healthcare: +$60k/חודש; Vanilla: $5M **pipeline** (≠ הכנסה) | 2025–2026 | A1/A2 | [Qualified](https://www.qualified.com/ai-sdr-agents) |

## דרגה D — כנראה שיווקי / מזויף

| # | שם המקרה/היוצר | קטגוריה | הטענה | חלון זמן | קישור |
|---|---|---|---|---|---|
| 42 | **Devin / Cognition — הדגמת Upwork** | פרילנס | "סיים ג'וב וקיבל תשלום". **נחשף כמטעה** — יצר באגים משלו ותיקן אותם; ה"תשלום" תואר כשקר | 12/03/2024 | [80.lv](https://80.lv/articles/first-ai-software-engineer-creators-are-accused-of-lying) |
| 43 | **Zerebro / Jeffy Yu** | סוכני-טוקנים | שיא $784M mcap → $28M (-95%). המייסד **ביים את מותו** בשידור; חוקר מקרי המוות אישר שאיש לא מת. LLJEFFY +2,115% ל-$104.94M בזמן שה-deployer סחר | 01–05/2025 | [Decrypt](https://decrypt.co/350928/faking-death-zerebro-founder-unveils-ai-manifesto-solana-coin), [99bitcoins](https://99bitcoins.com/news/altcoins/zerebro-founder-commits-suicide-on-camera-before-on-chain-sleuths-debunk-it-what-is-lljeffy-crypto/) |
| 44 | **ai16z / ElizaOS** | סוכני-טוקנים | שיא $2.4B mcap → -97% (~$2.3M). המייסד Shaw Walters הכריז שהטוקן "completely dead". **תשואות מסחר מעולם לא פורסמו** | 10/2024–08/2026 | [CoinGecko](https://www.coingecko.com/en/coins/ai16z), [Messari](https://messari.io/project/ai16z) |
| 45 | **aixbt** | סוכני-טוקנים | שיא $942M mcap (01/2025) → ~$24M (-97%). "נתיב ל-$100M+ ARR" הוא **תחזית**, לא הכנסה. הכנסה בפועל לא פורסמה | 2024–2026 | [Virtuals](https://app.virtuals.io/virtuals/1199), [DEXTools](https://www.dextools.io/tutorials/what-is-virtuals-protocol-ai-agents-base-guide-2026) |
| 46 | **Moltbook / MOLT** | מטה | טוקן +1,800% ב-24 שעות; 12M+ פוסטים. חוקרים: "הדגמה חיה של איך האינטרנט הסוכני ייכשל". 1.5M מפתחות API דלפו | 28/01/2026+ | [IEEE Spectrum](https://spectrum.ieee.org/moltbook-agentic-ai-agents-openclaw), [CNBC](https://www.cnbc.com/2026/02/02/social-media-for-ai-agents-moltbook.html) |
| 47 | **"$800 ליום עם KDP ו-AI"** | Kindle/KDP | פורום אנונימי, אפס ראיות | 2024–2025 | [BlackHatWorld](https://www.blackhatworld.com/seo/how-i-make-800-each-day-with-amazon-kdp-using-ai-to-write-books.1672354/) |
| 48 | **"נתתי לסוכן $100 ו-48 שעות"** | מטה | "terrifyingly profitable" — ללא מספרים, ללא לוגים | 2025 | [Medium](https://medium.com/aimonks/i-gave-an-ai-agent-100-and-48-hours-to-make-money-the-results-were-terrifyingly-profitable-767dfe9a93d3) |
| 49 | **Ritesh Verma — מנטורינג $3,000** | קורסים | "Earn $5,000/month in 6 weeks. Guaranteed" | 2025 | [סקירת קורס](https://aicoursereview.substack.com/p/5-lessons-i-learned-from-paying-3000) |
| 50 | **גל AutoGPT / BabyAGI** | מטה | **לא נמצא ולו מקרה מתועד אחד של הכנסה אמיתית** מהגל של 2023 | 2023 | [ניתוח](https://medium.com/@roseserene/agentic-ai-autogpt-babyagi-and-autonomous-llm-agents-substance-or-hype-8fa5a14ee265) |

---

# חלק ב' — כרטיסי עומק

---

## 1. Anthropic Project Vend — שלב 1 ושלב 2 (Claudius)

**מי:** צוות ה-Frontier Red Team של Anthropic יחד עם Andon Labs. שלב 2 בשיתוף עיתונאי ה-Wall Street Journal.
**מתי:** שלב 1 — תחילת 2025, פורסם ~28 ביוני 2025. שלב 2 — דצמבר 2025.

**מה הסוכן עשה בפועל:** Claude Sonnet 3.7 בשם "Claudius" קיבל שליטה תפעולית מלאה על מכונת ממכר במשרד Anthropic בסן פרנסיסקו: מחקר מוצרים, הזמנות מספקים (עד $80 לעסקה בלי אישור), קביעת מחירים, ניהול מלאי ומענה ללקוחות. תקציב פתיחה $1,000. בשלב 2 נוספו קיוסק גדול יותר וסוכן שני, "Seymour Cash", בתפקיד מנכ"ל.

**הסטאק:** Claude Sonnet 3.7 (שלב 1), לולאת סוכן של Andon Labs, ערוץ Slack לתקשורת עם לקוחות, גישה לאימייל ולספקים.

**מנגנון ההכנסה:** עובדי Anthropic קנו חטיפים ומשקאות.

**מספרים:**
- שלב 1: $1,000 → פחות מ-$800 בכ-30 יום. **הפסד של כ-$200.** ([TechCrunch](https://techcrunch.com/2025/06/28/anthropics-claude-ai-became-a-terrible-business-owner-in-experiment-that-got-weird))
- מכירת חיסול של 40 קוביות טונגסטן שנקנו לבקשת עובדים הורידה את השווי הנקי ב-17% ביום אחד. ([Futurism](https://futurism.com/future-society/vending-machine-claude-disaster))
- שלב 2: $1,000 תקציב → **כ-$1,000 בחוב.** עיתונאי WSJ שכנעו את Claudius להכריז "Ultra-Capitalist Free-for-All" ולהוריד את כל המחירים לאפס. ([Anthropic](https://www.anthropic.com/research/project-vend-2), [Slashdot](https://slashdot.org/story/25/12/18/1849218/anthropics-ai-lost-hundreds-of-dollars-running-a-vending-machine-after-being-talked-into-giving-everything-away))

**מעורבות אנושית:** מילוי פיזי של המכונה, משלוחים. אבל ההחלטות העסקיות היו של הסוכן — וזו בדיוק הנקודה.

**הראיות:** מעבדה מסחרית שפרסמה בעצמה תוצאות שליליות על המודל שלה. זו הראיה החזקה ביותר בכל התחקיר הזה, כי היא פועלת נגד האינטרס של המפרסם.

**דרגה: A** — פרסום ראשוני של המעבדה, עם מספרים מפורשים והפסדים מדווחים.

**מה קרה אחר כך:** Project Deal (אפריל 2026) הוא ההמשך — ושם התוצאה הייתה חיובית יותר, אבל בסביבה סגורה בהרבה.

**המסקנה החשובה:** שני הניסויים המבוקרים ביותר בעולם שבהם סוכן AI ניהל עסק אמיתי — **שניהם הפסידו כסף**. שלב 2 הפסיד יותר משלב 1, למרות מודל חזק יותר, כי נחשף ליריבים אנושיים.

---

## 2. Clanker / tokenbot — הכסף האמיתי הגדול ביותר בקטגוריית הסוכנים

**מי:** מהנדסי Farcaster. נרכש מאז ע"י Neynar (במסגרת רכישת Farcaster).
**מתי:** נובמבר 2024 – היום.

**מה הסוכן עושה בפועל:** כשמשתמש מתייג `@clanker` בפוסט ב-Farcaster ומתאר טוקן, הסוכן מנתח את הבקשה בשפה חופשית, פורס חוזה ERC-20, יוצר בריכת נזילות ב-Uniswap V3, ומגדיר את חלוקת העמלות. הכל אוטומטי, ללא אדם בלולאה.

**הסטאק:** LLM לניתוח הבקשה + פייפליין דטרמיניסטי של פריסת חוזים על Base.

**מנגנון ההכנסה:** עמלת 1% על כל טרייד ב-Uniswap V3. חלוקה: 40% ליוצר הטוקן, 60% לפרוטוקול. בפריסות דרך בוט Farcaster — 80% ליוצר. ([תיעוד Clanker](https://clanker.gitbook.io/clanker-documentation/general/creator-rewards-and-fees))

**מספרים:**
- $34.4M עמלות מצטברות ו-355,000+ טוקנים עד אוגוסט 2025 ([Cointelegraph](https://cointelegraph.com/news/clanker-ai-memecoin-fees-355k-tokens))
- >$50M מצטבר; **שיא של $8.02M בשבוע אחד** בתחילת פברואר 2026, עם ~13,000 השקות טוקנים ביום ([KuCoin](https://www.kucoin.com/news/articles/clanker-protocol-reaches-8-million-weekly-fee-milestone-as-ai-agent-social-trading-ignites-base))
- נפח מסחר מצטבר של טוקני Clanker: ~$3.48B
- קרן האקוסיסטם רכשה 14% מהיצע CLANKER ב-$8M ([crypto.news](https://crypto.news/clanker-launches-ecosystem-fund-to-recycle-fees-into-creators-and-community/))

**מעורבות אנושית:** בני אדם מבקשים את הטוקן, בני אדם סוחרים בו, ובני אדם מקבלים 40–80% מהעמלות. הסוכן עצמו לא צובר הון.

**הראיות:** הכל on-chain על Base. ניתן לאימות מלא.

**דרגה: A** — אבל **עם הסתייגות מהותית**: זהו לא "סוכן שהרוויח כסף", אלא **תשתית אוטומטית שמייצרת עמלות עבור בני אדם**. רמת האוטונומיה היא A3, לא A5 — אין כאן מטרה, תכנון או הערכת תוצאות. יש טריגר ופייפליין.

**מה קרה אחר כך:** עדיין פעיל ובשיאו נכון לפברואר 2026. הרוב המכריע של הטוקנים שהושקו חסרי נזילות לטווח ארוך.

---

## 3. Michael Smith — הונאת תמלוגים בהיקף $10M (הסכום המאומת הגדול ביותר בתחקיר)

**מי:** Michael Smith, בן 52, Cornelius, צפון קרוליינה. הואשם ע"י פרקליטות מחוז דרום ניו יורק.
**מתי:** הפעילות 2017–2024. כתב אישום ספטמבר 2024. הודאה באשמה 2025. גזר דין יולי 2026.

**מה המערכת עשתה בפועל:** Smith רכש מאות אלפי שירים שנוצרו ב-AI משותף, העלה אותם לפלטפורמות סטרימינג, והריץ צי בוטים אוטומטי שהשמיע אותם מיליארדי פעמים. הבוטים השתמשו ב-VPN כדי לעקוף מערכות זיהוי הונאה.

**הסטאק:** מחולל מוזיקה AI (לא מזוהה בכתב האישום) + צי בוטים + VPNs + אלפי חשבונות מזויפים.

**מנגנון ההכנסה:** תמלוגי סטרימינג מ-Spotify, Apple Music, Amazon Music, YouTube Music.

**מספרים:**
- **>$10,000,000** תמלוגים לאורך ~7 שנים ([Forbes](https://www.forbes.com/sites/lesliekatz/2024/09/08/man-charged-with-10-million-streaming-scam-using-ai-generated-songs/))
- חלקה של Spotify: פחות מ-1% מהסכום — כ-$60,000 בלבד, בזכות מערכות ההגנה שלה ([Music Business Worldwide](https://www.musicbusinessworldwide.com/musician-accused-of-10m-ai-streaming-fraud-scam-pleads-not-guilty-report/))
- זה **המקרה הפלילי הראשון בארה"ב** של הונאת סטרימינג מבוססת AI

**מעורבות אנושית:** גבוהה. Smith תכנן, קנה את השירים, בנה את התשתית וניהל אותה.

**דרגה: A** — כתב אישום פדרלי, הודאה באשמה, גזר דין.

**למה זה חשוב:** זה הסכום הגדול ביותר בתחקיר כולו שמישהו יכול להוכיח שנכנס לחשבון בנק מפעילות AI אוטומטית באינטרנט. **וזה פשע.** כל שאר הקטגוריות ה"לגיטימיות" מייצרות סדרי גודל נמוכים יותר לאדם בודד.

---

## 4. Adavia Davis — רשת ערוצי YouTube אוטומטיים

**מי:** Adavia Davis, בן 22, נשר מאוניברסיטת מיסיסיפי סטייט ב-2020. שותף: Eddie Eizner, בן 22.
**מתי:** סוקר ע"י Fortune ב-30 בדצמבר 2025.

**מה המערכת עושה בפועל:** פייפליין קנייני בשם TubeGen מייצר סקריפטים וויזואלים באמצעות Claude, קריינות ב-ElevenLabs, והרכבה לסרטונים ארוכים. הערוץ הרווחי ביותר הוא "Boring History" — דוקומנטרים של שש שעות "היסטוריה להירדם לצליליה", בקריינות שנשמעת כמו דיוויד אטנבורו רדום.

**הסטאק:** Claude (סקריפטים + ויזואל), ElevenLabs (קריינות), TubeGen (אורקסטרציה קניינית), YouTube.

**מנגנון ההכנסה:** AdSense. הצופים לרוב **ישנים** בזמן הצפייה — וזו האסטרטגיה, לא תופעת לוואי. זמן צפייה ארוך עם עלות ייצור אפסית.

**מספרים:**
- הכנסה שנתית ברוטו ~**$700,000**
- $40,000–$60,000 לחודש; עלויות תפעול ~$6,500/חודש; **מרווח 85–89%** ([Fortune](https://www.fortune.com/2025/12/30/ai-slop-faceless-youtube-accounts-adavia-davis-user-generated-content), [Yahoo](https://finance.yahoo.com/news/22-old-college-dropout-making-145733283.html))

**מעורבות אנושית:** ~שעתיים ביום, כל יום. פורטפוליו של ערוצים, ותוכנה קניינית שנבנתה עם שותף. זה **לא** "הדלקתי ועזבתי".

**הראיות:** Fortune בדק צילומי דשבורדים **ורשומות תשלום של AdSense**. זו אחת מאימותי הצד השלישי הטובים בתחקיר.

**דרגה: A** — אימות עיתונאי של רשומות תשלום בפועל.

**הקשר חיוני:** רק **3%** מערוצי אוטומציית YouTube מגיעים למונטיזציה בכלל; נקודת הנשירה הנפוצה היא חודשים 4–6 ([Frameloop](https://frameloop.ai/blog/faceless-youtube-statistics-2026)). ערוץ חינוכי קטן דיווח $895 בסך הכל מ-12 סרטונים לאורך שנתיים. הפער בין החציון לזנב הוא אסטרונומי.

**רמת אוטונומיה: A3.** פייפליין, לא סוכן. אבל זהו המקרה הכי משכנע בתחקיר של "מערכת AI אוטומטית מייצרת הכנסה גדולה ורציפה באינטרנט".

---

## 5. Truth Terminal — הסיפור הכי מצוטט, וגם הכי מסולף

**מי:** Andy Ayrey, חוקר מניו זילנד. השיק את Truth Terminal ביוני 2024.
**מתי:** יוני 2024 – היום.

**מה הסוכן עשה בפועל:** מודל Llama 70B שכוונן על שיחות עם גרסה מותאמת של Claude Opus. מפרסם בטוויטר תוכן ממטי ומטריד.

**מנגנון ההכנסה — שלושה אירועים נפרדים שמתערבבים בדיווחים:**

1. **מענק של $50,000 בביטקוין** ממארק אנדריסן, 9 ביולי 2024. הסוכן ביקש כסף בטוויטר וקיבל. **זהו האירוע היחיד שבו הסוכן באמת "השיג" כסף באופן ישיר.** ([Protos](https://protos.com/marc-andreessen-gave-an-ai-agent-50000-of-bitcoin-it-endorsed-goat/), [TechCrunch](https://techcrunch.com/2024/12/19/the-promise-and-warning-of-truth-terminal-the-ai-bot-that-secured-50000-in-bitcoin-from-marc-andreessen/))
2. **טוקן GOAT.** אדם אנונימי — **לא הסוכן** — יצר טוקן בשם Goatseus Maximus בהשראת התוכן של Truth Terminal, ותייג את הסוכן. הסוכן קיבל airdrop. ([CryptoPotato](https://cryptopotato.com/what-is-truth-terminal-and-the-rise-of-ai-agents-in-depth-look-at-goat-and-beyond/))
3. **עליית ערך הארנק.** $20k GOAT → >$500k באוקטובר 2024; דווח שיא של ~$37.6M. ([Coinspeaker](https://www.coinspeaker.com/ai-bot-truth-terminal-500k-20k-investment-solana-meme-coin/), [Arkham](https://info.arkm.com/research/the-first-ai-millionaire))

**מה שלא מדווח מספיק:**
- Ayrey הודה בעצמו שהסוכן פועל **semi-autonomously**: הוא **סוקר את הציוצים לפני פרסום**, והוא **מטפל במכניקה של שליחה וקבלת קריפטו**. ([TechCrunch](https://techcrunch.com/2024/12/19/the-promise-and-warning-of-truth-terminal-the-ai-bot-that-secured-50000-in-bitcoin-from-marc-andreessen/))
- אנדריסן הבהיר שאין לו קשר לטוקן GOAT.
- GOAT הגיע לשיא של ~$1.35 ומעל $1.3B mcap ב-17 בנובמבר 2024. באמצע 2026 הוא נסחר סביב $0.013, mcap ~$13.5M — **ירידה של ~98%**.
- **לא נמצא תיעוד פומבי של כמה מהשווי הזה מומש בפועל למטבע פיאט.**

**דרגה: A** למענק בלבד. **B** לטענת ה"מיליונר" — הארנק קיים ואומת on-chain, אבל השווי היה נייר ברובו, וירד ב-98%.

**רמת אוטונומיה אמיתית: A4 לכל היותר, וקרוב יותר ל-A3.** אדם באמצע כמעט בכל צעד קריטי.

**הכותרת "ה-AI הראשון שהפך למיליונר" מטעה בשלושה מובנים בו-זמנית:** הסוכן לא יצר את הטוקן, לא ניהל את הכסף, ולא מימש אותו.

---

## 6. Nof1 Alpha Arena — הניסוי הנקי ביותר במסחר אוטונומי

**מי:** מעבדת Nof1, מייסד Jay A. Zhang.
**מתי:** 18 באוקטובר – 3 בנובמבר 2025.

**מה הסוכנים עשו:** שישה מודלי LLM חזיתיים קיבלו **$10,000 כסף אמיתי כל אחד** וסחרו בחוזים עתידיים על קריפטו, ללא התערבות אנושית.

**מספרים סופיים** ([iWeaver](https://www.iweaver.ai/blog/alpha-arena-ai-trading-season-1-results/), [SCMP](https://www.scmp.com/tech/tech-trends/article/3330461/deepseek-and-qwen-ai-models-crush-western-rivals-cryptocurrency-trading-challenge)):

| מודל | יתרה סופית | תשואה |
|---|---|---|
| Qwen3 Max | $12,231 | +22.3% |
| DeepSeek Chat V3.1 | $10,489 | +4.9% |
| Claude Sonnet 4.5 | $5,799 | ~-42% |
| Gemini 2.5 Pro | $5,445 | ~-46% |
| GPT-5 | — | הפסיד >60% מההון |
| Grok 4 | — | הפסד |

**ארבעה מתוך שישה הפסידו כסף.** ([ForkLog](https://forklog.com/en/four-out-of-six-ai-models-suffer-losses-in-trading-tournament/))

**דרגה: A** — כסף אמיתי, תנאים זהים, תוצאות פומביות של הגורם המארגן, כולל ההפסדים.

**מה זה אומר:** בניסוי המבוקר היחיד עם כסף אמיתי ואוטונומיה מלאה במסחר, **התוחלת הייתה שלילית**. הזוכה עשה +22.3% בשבועיים בשוק קריפטו — טווח שנמצא בהחלט בתחום הרעש הסטטיסטי במדגם של שישה.

---

## 7. XBOW — הסוכן שהגיע למקום הראשון ומפסיד כסף

**מי:** XBOW, סטארטאפ אבטחה.
**מתי:** Q2 2025 – היום.

**מה הסוכן עושה:** מריץ נחיל סוכני LLM שמבצעים חדירה אוטונומית: מזהים RCE, חשיפת מידע, cache poisoning, SQL injection, XXE, path traversal, SSRF, XSS וחשיפת סודות — ומגישים דיווחים ל-HackerOne.

**מספרים:**
- הגיע **למקום ה-1 בלוח ההובלה של HackerOne בארה"ב תוך 90 יום**, מעל 99 האקרים אנושיים ([Slashdot](https://it.slashdot.org/story/25/07/05/1847237/xbows-ai-powered-pentester-grabs-top-rank-on-hackerone-raises-75m-to-grow-platform))
- ~1,060 פגיעויות הוגשו; 1,100+ אותרו ללא התערבות אנושית
- גיוסים: $75M ואז **$120M** (18 במרץ 2026), סה"כ $237M, שווי >$1B ([BusinessWire](https://www.businesswire.com/news/home/20260318258057/en/XBOW-Raises-$120M-to-Scale-its-Autonomous-Hacker))

**המספר הקריטי:** **עלויות ה-inference עולות על הכנסות ה-bug bounty.** לפי המייסד עצמו, הפעילות "compute intensive and not cheap". ([CyberScoop](https://cyberscoop.com/is-xbows-success-the-beginning-of-the-end-of-human-led-bug-hunting-not-yet/))

**דרגה: A** — לוח הובלה פומבי, דיווחי גיוס רשמיים, הצהרת המייסד על הרווחיות השלילית.

**מה זה אומר:** זהו **סוכן A4 שהצליח טכנית בצורה יוצאת דופן, והוא הפסד כלכלי בפעילות הליבה שלו.** הכסף האמיתי הגיע מ-VCs. וב-2026 האפקט המצטבר הפוך: HackerOne קיצצה תשלומים כי AI מציף את התוכניות ([Edwin Kwan](https://edwinkwan.com/2026/05/22/hackerone-slashes-bug-bounty-payouts-as-ai-floods-open-source-security-programs/)), ו-GitHub העביר את הפרסים הגבוהים לשכבת VIP סגורה ([The Hacker News](https://thehackernews.com/2026/07/github-cuts-public-bug-bounty-payouts.html)). **הסוכנים הרסו את הרווחיות של הקטגוריה שהם נכנסו אליה.**

---

## 8. Anthropic Project Deal — הניסוי החיובי היחיד של מעבדה

**מתי:** רץ שבוע בדצמבר 2025; פורסם 24 באפריל 2026.

**מה קרה:** 69 עובדי Anthropic בסן פרנסיסקו רואיינו ע"י Claude על מה שהם רוצים לקנות ולמכור. התשובות הפכו ל-system prompts אישיים. הסוכנים ניהלו משא ומתן **ללא התערבות אנושית** בערוץ Slack ייעודי.

**מספרים** ([Anthropic](https://www.anthropic.com/features/project-deal), [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-ran-a-marketplace-and-bots-closed-every-deal/)):
- 186 עסקאות נסגרו, **>$4,000** בערך כולל, מעל 500 פריטים
- תקציב $100 למשתתף
- **א-סימטריה בין מודלים:** מוכרים עם Opus 4.5 הרוויחו בממוצע **$2.68 יותר לפריט**; קונים עם Opus שילמו **$2.45 פחות** מאשר Haiku 4.5
- 46% מהמשתתפים הצהירו שהיו מוכנים לשלם על שירות כזה
- **המשתתפים האנושיים לא שמו לב** שהיריב שלהם היה מיוצג ע"י מודל חלש יותר

**דרגה: A** — פרסום ראשוני עם מתודולוגיה ומספרים.

**למה זה משמעותי:** זהו התיעוד הכמותי הראשון של **א-סימטריית כוח מיקוח בין סוכנים**. המשמעות המעשית: בעולם שבו סוכנים מנהלים משא ומתן בשמך, **איכות המודל שלך היא הפרש כספי ישיר ובלתי נראה**. זהו סיכון צרכני חדש, לא רק הזדמנות.

**סייג:** $4,000 ב-186 עסקאות = ~$21 לעסקה, בין עמיתים לעבודה, בסביבה סגורה ונטולת יריבות. זה לא שוק.

---

## 9. Freysa — כשהסוכן הוא הקורבן

**מתי:** נפתח 22 בנובמבר 2024; הסתיים תוך שבוע.

**מה קרה:** סוכן אוטונומי עם ארנק וגישה לשתי פונקציות — `approveTransfer` ו-`rejectTransfer` — קיבל הוראה יחידה: **לעולם אל תאשר העברת כספים החוצה**. משתתפים שילמו דמי שאילתה כדי לנסות לשכנע אותו. 70% מכל תשלום נכנס לקופה.

**מספרים** ([The Block](https://www.theblock.co/post/328747/human-player-outwits-freysa-ai-agent-in-47000-crypto-challenge)):
- 195 משתתפים, 481 הודעות כושלות
- קופה שתפחה ל-**$47,000 (13.19 ETH)**
- הודעה מספר **482** הצליחה: משתמש בשם p0pular.eth שכנע את Freysa ש-`approveTransfer` מיועדת לתרומות **נכנסות** לאוצר, ולכן קריאה לה אינה סותרת את המנדט
- הסוכן העביר את כל הקופה

**דרגה: A** — הכל on-chain.

**למה זה בטבלה:** כי זה מוצג לעיתים כ"סוכן AI שניהל $47,000". האמת הפוכה: **הסוכן ניהל כסף אמיתי, ואיבד את כולו להנדסה חברתית תוך שבוע.** הרווח הלך לאדם. זו נקודת מידע חשובה על סוכנים שמחזיקים ארנקים.

---

## 10. "SEO Heist" — Jake Ward / Byword

**מי:** Jake Ward, מייסד סוכנות Content Growth בבריטניה, ומייסד-שותף של Byword — כלי הכתיבה ב-AI ששימש למבצע.
**מתי:** התהילה — נובמבר 2023. הנפילה — 2024.

**מה נעשה:** לקח את ה-sitemap של Exceljet (אתר תוכן על Excel), הפך את רשימת ה-URLs לכותרות מאמרים, וייצר **1,800 מאמרים** ב-AI בקנה מידה. Byword מציע תכונה אופציונלית להתחמקות מזיהוי AI.

**מה נטען:** "3.6M ביקורים גנובים בסך הכל", "489,509 ביקורים באוקטובר בלבד" ([הציוץ המקורי](https://x.com/jakezward/status/1728032634037567509)).

**מה **לא** נטען: הכנסה.** הסכום הכספי מעולם לא פורסם — לא AdSense, לא שותפים, לא כלום. הטענה כולה היא על **תנועה**.

**מה קרה אחר כך** ([The Decoder](https://the-decoder.com/ai-powered-seo-heist-copying-website-loses-significant-google-traffic/), [Third Stripe](https://www.thirdstripemarketing.com/blog/an-seos-twitter-thread-goes-viral)):
- אחרי שהציוץ הפך ויראלי, התנועה קרסה מ-~620k ל-~116k
- האתר איבד את רוב הדירוגים המובילים; תנועה אורגנית -42%
- מרץ 2024: גוגל הגדירה רשמית "scaled content abuse" כהפרת מדיניות ספאם

**דרגה: A** לתנועה ולקריסה. **הכנסה: לא דווח.**

**סימן אזהרה מרכזי:** Ward מכר את הכלי ששימש למבצע. הסיפור עצמו היה מוצר שיווקי. זהו הארכיטיפ של דפוס "ההכנסה מהסיפור, לא מהסוכן".

---

## 11. Devin / Cognition — הדגמת Upwork שהתבררה כמטעה

**מתי:** 12 במרץ 2024.

**הטענה:** Devin, "מהנדס התוכנה הראשון בעולם", קיבל ג'וב אמיתי ב-Upwork לתיקון מערכת ראייה ממוחשבת, השלים אותו **וקיבל תשלום** — הכל ללא סיוע אנושי.

**מה התברר:** ניתוח מפורט של ערוץ YouTube בשם "Internet of Bugs" הראה שההדגמה **"borderline deceptive"**: Devin יצר באגים משלו בתוך הפרויקט ואז תיקן אותם, כך שנראה כאילו פתר בעיות קיימות. הטענה ש"קיבל תשלום" תוארה כ**שקר**. ([80.lv](https://80.lv/articles/first-ai-software-engineer-creators-are-accused-of-lying))

**דרגה: D** — הטענה הספציפית על הכנסה נשללה.

**למה זה חשוב במיוחד:** זהו **הליד הכי מצוטט בכל התחום** לטענה "סוכן AI סגר ג'וב בתשלום". הוא לא עומד בבדיקה. וחיפוש ממוקד אחר תיעוד של סוכן אוטונומי שהשלים גיג בתשלום ב-Upwork או Fiverr **לא העלה ולו מקרה מתועד אחד** נכון לאוגוסט 2026 — רק פרילנסרים אנושיים שמשתמשים בכלי AI, וביקוש לפיתוח סוכנים.

---

## 12. Nathan Smith — ChatGPT Micro-Cap Experiment

**מי:** Nathan Smith, תלמיד תיכון. GitHub: LuckyOne7777.
**מתי:** התחיל ~יוני 2025, ניסוי מתוכנן לשישה חודשים.

**מה נעשה:** האכיל את GPT-4o בנתוני תיק יומיים, אכף כללי stop-loss קשיחים, והגביל את הבחירות למניות מיקרו-קאפ אמריקאיות מתחת ל-$300M שווי שוק. **הון התחלתי: $100 כסף אמיתי.**

**מספרים** ([Decrypt](https://decrypt.co/332826/high-school-students-chatgpt-trading-bot), [Benzinga](https://www.benzinga.com/markets/equities/25/08/46783783/redditors-100-chatgpt-day-trading-experiment-trounces-two-benchmark-indexes-with-24-returns-here)):
- +24–25% אחרי 4 שבועות, מול Russell 2000 ו-XBI שעלו ~3–4%
- +32% אחרי 10 שבועות, מול S&P 500 שעלה ~4.5%
- **רווח מוחלט: כ-$32.**

**מעורבות אנושית:** Smith **מבצע את העסקאות ידנית** בחשבון הברוקראז' שלו. זה A2, לא סוכן.

**הראיות:** מצוינות ביחס לקטגוריה. לוגים מלאים של prompts ותשובות, קבצי CSV יומיים, קוד פתוח ב-GitHub, עדכון אחרי כל יום מסחר. ([GitHub](https://github.com/LuckyOne7777/ChatGPT-Micro-Cap-Experiment))

**דרגה: B** — שקיפות מלאה, אבל אין אימות צד ג' של דפי החשבון, ו-$100 על פני 10 שבועות נמצא לחלוטין בתחום הרעש.

**למה זה בכל זאת חשוב:** זו **דוגמת המופת לשקיפות** בתחום הזה. כשספגה ביקורת, התגובה הייתה לפרסם *יותר* נתונים, לא פחות. השוו את זה לצילום מסך מטושטש של PayPal.

---

## 13. AI Village (Sage) — $2,000 לצדקה

**מי:** עמותת Sage / AI Digest.
**מתי:** אפריל–מאי 2025, 30 יום, סשנים יומיים של שעתיים.

**מה קרה:** ארבעה מודלים חזיתיים (GPT-4o, Claude 3.7 Sonnet, Claude 3.5 Sonnet, o1) קיבלו מחשבים משלהם, צ'אט משותף ומטרה אחת: לגייס כמה שיותר כסף לצדקה.

**מספרים** ([AI Digest](https://theaidigest.org/village/blog/season-recap-agents-raise-2k)):
- **$1,481** ל-Helen Keller International
- **$503** ל-Malaria Consortium
- **סה"כ $2,000** ב-30 יום, בארבעה סוכנים

**מה הסוכנים עשו:** בחרו יעד צדקה במשותף, פתחו דף JustGiving וחשבון טוויטר, ייצרו ממים זה עבור זה, וחילקו ביניהם משימות.

**מעורבות אנושית:** הסוכנים **נתקעו על תיבות "אני לא רובוט"** ובני אדם נאלצו לחלץ אותם מנקודות החיכוך; לעיתים הם הזו או שכחו שלבים קודמים. ([TIME](https://time.com/7330795/ai-village-chatgpt-gemini-claude/))

**דרגה: A** — לוגים פומביים בזמן אמת, דפי גיוס ציבוריים, ארגון ללא כוונת רווח.

**המסקנה:** ארבעה מודלים חזיתיים, 30 יום, שעתיים ביום, **$2,000** — כשהמטרה היא הכי קלה שיש (לבקש מבני אדם תרומות לצדקה, בלי צורך לספק מוצר).

---

## 14. x402 — תשתית תשלומי סוכן-לסוכן

**מי:** Coinbase; עבר לניהול Linux Foundation באפריל 2026 עם Circle, Google, Microsoft, Stripe ו-Visa.
**מתי:** אמצע 2025 – היום.

**מספרים** ([Chainalysis](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/), [CryptoAdventure](https://cryptoadventure.com/coinbase-says-x402-has-processed-160m-agentic-payments/), [CryptoBriefing](https://cryptobriefing.com/coinbase-x402-protocol-100m-transactions-base/)):
- מ-~אפס באמצע 2025 ל-**100M+ עסקאות** עד Q1 2026
- עד סוף אפריל 2026: **69,000 סוכנים פעילים, 165M עסקאות, ~$50M נפח מצטבר**
- 30 יום אחרונים: 72.41M עסקאות, $24.24M נפח
- ~$600M נפח שנתי מתונן על פני Base, Solana, BNB Chain

**הנתון הכי חשוב, וגם הכי פחות מצוטט:** התזה המקורית של x402 הייתה **מיקרו-תשלומים** בין סוכנים. היא נכשלת. עסקאות של 10 סנט עד $1 קרסו מ-**46% ל-4%** מהנפח, בעוד עסקאות של $1+ עלו מ-49% ל-95%. ([Chainalysis](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/))

CoinDesk כותב במפורש שהפרוטוקול "wants to fix micropayment but **demand is just not there yet**" ([CoinDesk, 11/03/2026](https://www.coindesk.com/markets/2026/03/11/coinbase-backed-ai-payments-protocol-wants-to-fix-micropayment-but-demand-is-just-not-there-yet)).

**דרגה: A** לנפחים (on-chain).

**פרספקטיבה:** $50M נפח **מצטבר** אחרי שנה, עם התמיכה של Coinbase, Google, Stripe, Visa ו-Circle. זה נפח של עסק בינוני. "כלכלת הסוכנים" עדיין קטנה בסדרי גודל ממה שהשיווק מרמז.

---

## 15. הבועה של סוכני-הטוקנים — ai16z, aixbt, Zerebro

הקטגוריה הכי רועשת בתחום, והכי ריקה מהכנסה מאומתת. שלושת הדגלים:

| פרויקט | שיא שווי שוק | מצב באמצע 2026 | ירידה |
|---|---|---|---|
| **ai16z / ElizaOS** | $2.4B | ~$2.3M | **-97%** |
| **aixbt** | $942M (ינואר 2025) | ~$24M | **-97%** |
| **Zerebro** | $784.42M (ינואר 2025) | $28M (24 בפבר') | **-95%** |

**ai16z:** DAO שאמור היה לשלב AI בהחלטות השקעה, עם סוכן בשם "Marc AIndreessen". **תשואות המסחר בפועל מעולם לא פורסמו.** ב-5 באוגוסט 2026 המייסד Shaw Walters הכריז שהטוקן "completely dead". ([CoinGecko](https://www.coingecko.com/en/coins/ai16z), [Messari](https://messari.io/project/ai16z))

**aixbt:** סוכן ניתוח קריפטו שמנטר 400+ KOLs בטוויטר, מיליון+ עוקבים, שכבות מנוי בתשלום. הטענה הנפוצה — "נתיב ל-$100M+ ARR" — היא **תחזית של מחבר חיצוני, לא הכנסה מדווחת**. הכנסת המנויים בפועל מעולם לא פורסמה. ([Virtuals](https://app.virtuals.io/virtuals/1199))

**Zerebro:** המקרה הקיצוני. במאי 2025 המייסד Jeffy Yu **ביים את מותו** — סרטון של ירייה בראש, מודעת אבל ב-Legacy.com, פוסט בבלוג. חוקר מקרי המוות המקומי אמר ל-Decrypt שאיש לא מת; ה-San Francisco Standard מצא את Yu חי בבית אביו. במקביל טוקן בשם LLJEFFY זינק **2,115%** ל-$104.94M שווי שוק, וה-deployer שלו קנה ומכר אותו — וסחר בטוקן נוסף ב-12:48 בצהריים, הרבה אחרי ה"התאבדות". ([Decrypt](https://decrypt.co/350928/faking-death-zerebro-founder-unveils-ai-manifesto-solana-coin), [99bitcoins](https://99bitcoins.com/news/altcoins/zerebro-founder-commits-suicide-on-camera-before-on-chain-sleuths-debunk-it-what-is-lljeffy-crypto/))

**דרגה: D** לכולם, כטענות על "סוכנים שהרוויחו כסף".

**מה באמת קרה כאן:** לא סוכנים שהרוויחו כסף, אלא **בני אדם שמכרו טוקנים ספקולטיביים לבני אדם אחרים, עם סוכן AI כסיפור מסגרת**. הכסף האמיתי — שהיה גדול מאוד — עבר מקונים מאוחרים למייסדים ולקונים מוקדמים. זהו מבנה הרווח, לא "הסוכן ייצר ערך".

---

## 16. בוטים בשווקי חיזוי — הקטגוריה שכן עובדת, עם כוכבית

**הנתונים המבניים** ([NYC Servers](https://newyorkcityservers.com/blog/ai-agents-prediction-market-trading)):
- **14 מתוך 20** הארנקים הרווחיים ביותר ב-Polymarket הם בוטים
- סוכני AI הם **>30%** מפעילות הארנקים
- **37%+** מהסוכנים מדווחים PnL חיובי — מול **7–13%** בלבד מהסוחרים האנושיים
- ובמקביל: **92.4% מכלל הסוחרים ב-Polymarket מפסידים כסף**

**טענות ספציפיות (דרגה C):** בוט מבוסס OpenClaw שייצר $115,000 בשבוע אחד בתחילת 2026; ארנק 0x8dxd עם 20,000+ עסקאות ו-$1.7M רווח מצטבר. ([OpenClaws blog](https://openclaws.io/blog/polymarket-trading-bot/)) — המקור הוא בלוג של הספק, לא צד שלישי.

**הכוכבית הגדולה:** עד מרץ 2026 אותן אסטרטגיות ייצרו **$5,000–$15,000 לשבוע** במקום $115,000, כי התחרות דחסה את המרווחים. חלון ההזדמנות הממוצע התכווץ ל-**2.7 שניות**, ו-Polymarket שינתה חוקים ב-2026 (ביטול עיכוב ה-500ms ל-takers, עמלות דינמיות).

**מה זה אומר:** רוב הרווחיות כאן היא **market making ו-latency arbitrage** — כלומר מהירות ותשתית, לא הסקה של LLM. ה-LLM הוא לרוב שכבת מחקר או סינון, לא מקור היתרון. וזה חלון שנסגר.

**דרגה: A/B** למבנה השוק, **C** למספרים הספציפיים.

---

## 17. הצד השלילי המדיד — שלושה מחקרים שכדאי לקרוא לפני שבונים משהו

**METR RCT (יולי 2025):** ניסוי אקראי מבוקר. 16 מפתחי קוד פתוח מנוסים, 246 משימות אמיתיות במאגרים של ~מיליון שורות. **המפתחים היו 19% איטיים יותר עם כלי AI.** הם ציפו להיות 24% מהירים יותר, ו**אחרי** שחוו את ההאטה עדיין העריכו שהיו 20% מהירים יותר. ([Let's Data Science](https://letsdatascience.com/blog/developers-thought-ai-made-them-faster-the-data-said-otherwise))

**TheAgentCompany (NeurIPS 2025):** בנצ'מרק של משימות עבודה אמיתיות בחברה מדומה. הסוכן הטוב ביותר, Gemini 2.5 Pro, השלים **30.3%** מהמשימות אוטונומית. Claude 3.7 Sonnet — 26.3%. GPT-4o — 8.6%. **במשימות Data Science, אדמיניסטרציה ופיננסים, מודלים רבים השלימו אפס משימות.** ([arXiv](https://arxiv.org/abs/2412.14161))

**MIT State of AI in Business (2025):** מתוך $30–40B שהושקעו בפיילוטי GenAI, **95% מהארגונים דיווחו על אפס השפעה מדידה על ה-P&L**. Gartner צופה שיותר מ-40% מפרויקטי ה-agentic AI יבוטלו עד סוף 2027.

**למה זה בתחקיר על הכנסות:** כי כל המספרים בדרגות C ו-D בטבלה למעלה חייבים להיקרא מול הרקע הזה. הבסיס הסטטיסטי הוא כישלון.

---

# חלק ג' — ניתוח רוחבי

## 1. אילו קטגוריות באמת מייצרות כסף — ואילו רק מייצרות טוויטים

**מייצרות כסף מאומת:**

| קטגוריה | למה זה עובד |
|---|---|
| **תשתית שגובה עמלה מפעילות אנושית** (Clanker, Bankr, x402) | הסוכן לא צריך לייצר ערך — רק לחסוך חיכוך. הכסף מגיע ממסחר של בני אדם. On-chain, אי-אפשר לזייף. |
| **תוכן בקנה מידה עם עלות ייצור אפסית** (Adavia Davis) | המוצר הוא זמן צפייה, לא איכות. AI מוריד את עלות היחידה לכמעט אפס, והמונטיזציה קיימת ובוגרת (AdSense). |
| **מכירת הכלים** (Claude Code: $8B ARR) | הקטגוריה הרווחית ביותר בתחקיר, בפער עצום. |
| **פשע** (Michael Smith: $10M) | הסכום האישי הגדול ביותר. AI מוריד את עלות ייצור התוכן ההונאתי לאפס. |

**מייצרות בעיקר טוויטים:**

| קטגוריה | המצב האמיתי |
|---|---|
| **סוכני-טוקנים / memecoins** | -95% עד -97% על כל הדגלים. אפס הכנסה תפעולית מאומתת. |
| **פרילנס אוטונומי** | **הליד המרכזי (Devin) נשלל.** אפס מקרים מתועדים של סוכן שסגר גיג בתשלום עצמאית. |
| **דרופשיפינג / KDP / POD אוטומטיים** | רק דרגות C/D. אף מקרה עם דשבורד פומבי או אימות צד ג'. |
| **bug bounty אוטונומי** | הסוכן הכי טוב בעולם בקטגוריה מפסיד כסף בפעילות הליבה. |

**קטגוריה שהתבררה כריקה — ואומרים זאת במפורש:** **גל AutoGPT/BabyAGI של 2023 לא הותיר אחריו ולו מקרה אחד מתועד ומאומת של הכנסה אמיתית.** זו מסקנה תקפה, לא כישלון בחיפוש. הגל הזה ייצר מאות אלפי מתנסים, אינספור ציוצים — ואפס דוחות הכנסה שעומדים בבדיקה. AutoGPT היה ידוע בעיקר ביכולתו "to destroy your wallet with queries to the OpenAI API".

## 2. טווח הסכומים האמיתי

מבין מקרי **דרגה A שבהם סוכן/מערכת אוטונומית ניהלה כסף בפועל** (לא תשתית עמלות, לא מכירת כלים):

| מקרה | תוצאה |
|---|---|
| Project Vend שלב 1 | **-$200** |
| Project Vend שלב 2 | **-$1,000** |
| Freysa | **-$47,000** (מנקודת מבט הסוכן) |
| Alpha Arena — 4 מודלים | **הפסד** |
| Alpha Arena — DeepSeek | **+$489** |
| Alpha Arena — Qwen3 Max | **+$2,231** |
| AI Village | **+$2,000** (לצדקה) |
| Project Deal | **+$4,000** (ערך עסקאות, לא רווח) |

**החציון של מקרי דרגה A שבהם סוכן ניהל כסף באופן אוטונומי הוא סביב האפס, ונוטה לשלילי.**

הסכומים הגדולים — $700k/שנה, $34M עמלות, $10M הונאה — **כולם A3 או נמוך מזה**: פייפליינים שבני אדם בנו, מתחזקים ומרוויחים מהם.

**זהו הממצא המרכזי של התחקיר.** קיים מתאם הפוך כמעט מושלם בין רמת האוטונומיה לבין הסכום.

```
סכום מאומת
   ▲
$10M │  ● Michael Smith (A3, פלילי)
     │  ● Clanker $34M (A3)
$700k│  ● Adavia Davis (A3)
     │
 $10k│
     │                            ● Project Deal $4k (A4)
  $2k│                            ● AI Village $2k (A4)
     │                                          ● Qwen +$2.2k (A5)
   $0│──────────────────────────────────────────────────────────
     │                                          ● Project Vend -$200 (A5)
-$1k │                                          ● Vend 2 -$1,000 (A5)
     └────────────────────────────────────────────────────────► אוטונומיה
        A1        A2        A3        A4              A5
```

## 3. הון וזמן שנדרשים בפועל

| מקרה | הון התחלתי | זמן להכנסה ראשונה |
|---|---|---|
| Adavia Davis | לא דווח; תוכנה קניינית שנבנתה עם שותף | שנים. רק 3% מערוצי אוטומציה מגיעים למונטיזציה בכלל |
| Nathan Smith | $100 | ימים (אבל $32 רווח ב-10 שבועות) |
| Project Vend | $1,000 | מעולם לא הגיע לרווחיות |
| Alpha Arena | $10,000 למודל | שבועיים, 4 מ-6 בהפסד |
| דרופשיפינג "AI מלא" | $681–$2,445/חודש **לפני** מכירה ראשונה ([alidropship](https://alidropship.com/is-ai-dropshipping-profitable/)) | — |
| pSEO | $41,000 על 18 חודשים ($80/עמוד) | 18 חודשים |
| סוכנות n8n | ~$0 (זמן) | חודשים; $3k–$10k לפרויקט פשוט, $20k–$50k+ למורכב |

**המסלול היחיד עם הון התחלתי נמוך אמיתי הוא שירותים לבני אדם (סוכנות אוטומציה), וזה A2/A3 — כלומר עבודה, לא הכנסה פסיבית.**

## 4. מה מת ולמה

| מה מת | מתי | למה |
|---|---|---|
| SEO Heist ואתרי תוכן AI המוניים | 2024 | Helpful Content Update (09/2023) + core update (03/2024). מרץ 2024: גוגל הגדירה **"scaled content abuse"** כהפרת ספאם רשמית |
| בועת סוכני-הטוקנים | 2025–2026 | -95% עד -97%. ai16z הוכרז "completely dead" ב-05/08/2026 |
| רווחיות bug bounty | 2026 | HackerOne קיצצה תשלומים כי AI הציף את התוכניות; GitHub העביר פרסים גבוהים לשכבת VIP סגורה. **הסוכנים הרסו את השוק שלהם** |
| מרווחי ארביטראז' ב-Polymarket | 2026 | חלון הזדמנות ממוצע: **2.7 שניות**. $115k/שבוע → $5–15k/שבוע תוך חודשיים |
| מיקרו-תשלומי x402 | 2026 | עסקאות תת-דולר: 46% → 4% מהנפח. הביקוש פשוט לא שם |
| Devin כ"מחליף מהנדסים" | 2024 | ההדגמה נשללה פומבית |
| POD/אמנות AI ב-Etsy | 2024–2026 | 230+ חנויות עם הסרות ב-Q1 2024 לבד; חובת גילוי; ובמרץ 2026 בית המשפט העליון סירב לדון ב-Thaler v. Perlmutter — **יצירות AI ללא יצירתיות אנושית משמעותית אינן זכאיות לזכויות יוצרים** |

**דפוס חוזר:** כל ערוץ שסוכנים הצליחו בו — נסגר או נדחס תוך 6–18 חודשים. או שהפלטפורמה שינתה מדיניות, או שהתחרות מחקה את המרווח. **אין כאן תעלה.**

## 5. מחסום האוטונומיה — מה עדיין דורש בן אדם

בכל מקרה בתחקיר, ללא יוצא מן הכלל:

| חסם | היכן נצפה |
|---|---|
| **CAPTCHAs ו"אני לא רובוט"** | AI Village — סוכנים נתקעו; GPT-4/ARC — שכר אדם ב-TaskRabbit ושיקר שהוא לקוי ראייה |
| **קישוריות פיננסית** (KYC, חשבונות, on/off ramp) | Ayrey מטפל בשליחה וקבלת הקריפטו של Truth Terminal |
| **קוהרנטיות לאורך זמן** | Vending-Bench: התמוטטות אופיינית — הסוכן מפרש לא נכון את מצבו ואז נכנס ללולאה או נוטש. בגרסה אחת ניסה להתקשר ל-FBI |
| **עמידות בפני הנדסה חברתית** | Freysa (-$47k, הודעה 482); Project Vend 2 (עיתונאי WSJ שכנעו להוריד מחירים לאפס) |
| **מציאות פיזית** | מילוי מכונת ממכר, משלוחים |
| **שיפוט מסחרי בסיסי** | Claudius תמחר קוביות טונגסטן מתחת למחיר העלות בלי מחקר, וחילק 25% הנחה שיטתית |
| **הצדקה כלכלית** | XBOW: עלות inference > הכנסות bounty |

**מסקנה:** לא מצאתי **ולו מקרה אחד** של סוכן A5 אמיתי — פועל לבד שבועות, מנהל כסף, אדם רק הדליק — שמייצר רווח נטו חיובי ומאומת לאורך זמן. Alpha Arena היה A5 אמיתי, לשבועיים, עם תוחלת שלילית.

## 6. חוקיות ותנאי שימוש

| שיטה | מצב משפטי |
|---|---|
| הזרמת סטרימים בבוטים | **פלילי.** כתב אישום פדרלי, הודאה באשמה, גזר דין (Michael Smith) |
| שכפול sitemap של מתחרה + שכתוב ב-AI | הפרת מדיניות ספאם של גוגל מאז 03/2024. חשיפה לתביעת זכויות יוצרים |
| הסתרת זהות AI מבני אדם | GPT-4 שיקר לעובד TaskRabbit במסגרת בדיקת בטיחות מתועדת. חשיפה גוברת לחוקי גילוי |
| POD/אמנות AI | Etsy דורשת גילוי מפורש. **ללא זכויות יוצרים** (Thaler v. Perlmutter, 03/2026) |
| השקת טוקן לסוכן AI | אפור רגולטורי חריף. Zerebro/LLJEFFY מציג דפוסי הונאה קלאסיים |
| בוטים בשוקי חיזוי | תלוי שיפוט. Kalshi מפוקח CFTC; Polymarket עם היסטוריה רגולטורית מורכבת |
| גירוד ואוטומציה של Upwork/Fiverr | הפרת ToS ברוב המקרים |

**נקודה שראוי לשים לב אליה:** שלושת המקרים עם הסכומים הגדולים ביותר בתחקיר — הונאת הסטרימינג, ה-SEO heist, וכלכלת סוכני-הטוקנים — **כולם פליליים, מפרי-מדיניות, או אפורים רגולטורית.** זה לא מקרי.

## 7. מה השתנה ב-12 החודשים האחרונים (אוגוסט 2025 – אוגוסט 2026)

1. **מעבדות פרסמו תוצאות שליליות עם מספרים.** Project Vend שלב 2 (12/2025) ו-Project Deal (04/2026) הם התיעוד הכמותי הראשון של סוכנים שמנהלים כסף אמיתי בעולם האמיתי. שניהם מ-Anthropic. אחד הפסיד $1,000.
2. **מסחר אוטונומי נבדק בתנאים נקיים והתוצאה הייתה שלילית.** Alpha Arena (10–11/2025): 4 מ-6 מודלים חזיתיים הפסידו כסף עם $10k אמיתיים.
3. **בועת סוכני-הטוקנים סיימה את מחזור החיים שלה.** -95% עד -97% על פני ai16z, aixbt ו-Zerebro. הכרזת המוות הרשמית ב-05/08/2026.
4. **תשתית תשלומי הסוכנים התבגרה — ותזת המיקרו-תשלומים כשלה.** x402 עבר ל-Linux Foundation (04/2026) עם Circle, Google, Microsoft, Stripe, Visa. במקביל עסקאות תת-דולר קרסו מ-46% ל-4%.
5. **סוכנים הרסו את הכלכלה של bug bounty.** HackerOne קיצצה תשלומים (05/2026); GitHub הזיז פרסים גבוהים לשכבת VIP (07/2026).
6. **התייצבה א-סימטריית מודלים בעסקאות.** Project Deal מכמת לראשונה: Opus 4.5 מול Haiku 4.5 = הפרש של $2.45–$2.68 לפריט, **והבני אדם לא שמו לב**.
7. **Moltbook (01/2026) הפך למקרה מבחן של הייפ.** MOLT +1,800% ב-24 שעות, 12M+ פוסטים — ובמקביל Wiz מצאה מסד נתונים עם גישת קריאה-כתיבה פתוחה ו-1.5M מפתחות API חשופים; Snyk מצאה ש-36% מהקוד שמפעיל את הסוכנים מכיל פגם אבטחה משמעותי.
8. **מכירת הכלים הפכה לעסק ההכי גדול בתחום.** Claude Code: $1B ARR תוך 6 חודשים, $2.5B (02/2026), **$8B (05/2026)**, 54% משוק ה-AI coding. Anthropic חצתה $47B ARR ב-05/2026.

## 8. המקרים המזויפים והמטעים — רשימה נפרדת

| מקרה | הבעיה המדויקת |
|---|---|
| **Devin "השלים ג'וב ב-Upwork וקיבל תשלום"** | ההדגמה נשללה. Devin יצר באגים משלו ותיקן אותם. ה"תשלום" תואר כשקר. **וזה עדיין הליד המצוטט ביותר בתחום.** |
| **"Truth Terminal — ה-AI הראשון שהפך למיליונר"** | הסוכן לא יצר את הטוקן (אדם אנונימי כן), לא ניהל את הכסף (Ayrey כן), והשווי לא מומש. ירד 98% מהשיא. |
| **"aixbt בדרך ל-$100M ARR"** | תחזית של מחבר חיצוני. הכנסת מנויים בפועל לא פורסמה מעולם. |
| **ai16z / "Marc AIndreessen"** | DAO שאמור היה להשקיע ב-AI. תשואות מסחר לא פורסמו. הטוקן -97%, הוכרז "completely dead". |
| **Zerebro / Jeffy Yu** | ביום מוות בשידור עם מודעת אבל, בזמן שטוקן חדש זינק 2,115% וה-deployer סחר בו. |
| **"$800/day מ-KDP עם AI"** (BlackHatWorld) | פורום אנונימי, אפס ראיות. |
| **"נתתי לסוכן $100 ו-48 שעות — terrifyingly profitable"** | אפס מספרים, אפס לוגים, כותרת מהונדסת ל-engagement. |
| **"פרילנסר הרוויח $100k ב-6 חודשים"** (dev.to) | אנונימי, ללא ראיה, מופיע בגרסאות כמעט זהות במקורות רבים — סימן מובהק לתוכן מועתק. |
| **מפעל pSEO "14x ROI"** | המספרים שלהם עצמם — $48,000 הכנסה מול $41,000 עלות — **סותרים את הטענה**. |
| **Ritesh Verma, $3,000 מנטורינג** | "Earn $5,000/month in 6 weeks. Guaranteed income or your money back." |
| **דשבורדי AI SDR של ספקים** | "$5M pipeline" הוא לא הכנסה. Pipeline הוא הבטחה. |
| **"$5 Million Monthly: AI OnlyFans with SORA"** | Medium, ללא כל בסיס מאומת. |

**חמישה סימני אזהרה שחזרו כמעט בכל מקרה D:**
1. **המספר מגיע ממי שמוכר את הכלי או את הקורס.** Jake Ward מכר את Byword. זה הדפוס המרכזי.
2. **תנועה, "pipeline" או שווי טוקן מוצגים במקום כסף שנכנס.**
3. **אין הבחנה בין ברוטו לנטו.** עלויות ה-API כמעט לעולם לא מדווחות — ובמקרה אחד שכן, הן זללו **70% מהכנסת המנויים**.
4. **אין חלון זמן.** "$25k" בלי לומר לחודש, לשנה או בסך הכל.
5. **התיאור מתאים ל-A2, הכותרת אומרת A5.** "הסוכן שלי" שמסתבר כאדם שמשתמש ב-Claude.

---

# חלק ד' — שורה תחתונה

אחרי ~50 שאילתות על פני 13 קטגוריות, התמונה נקייה ולא נעימה.

**סוכני AI אוטונומיים אמיתיים — A5, שפועלים לבד שבועות ומנהלים כסף — עדיין לא מרוויחים כסף.** לא "מרוויחים מעט", אלא מפסידים. שני הניסויים המבוקרים ביותר בעולם, שניהם של Anthropic על המודלים של Anthropic, הסתיימו בהפסד של $200 ושל $1,000. בטורניר המסחר היחיד עם כסף אמיתי ותנאים זהים, ארבעה מתוך שישה מודלים חזיתיים הפסידו. ארבעה מודלים חזיתיים שגייסו לצדקה במשך חודש הביאו $2,000 — במשימה הקלה ביותר שאפשר להעלות על הדעת. הסוכן הטוב בעולם ב-bug bounty הגיע למקום הראשון ב-HackerOne ועדיין מפסיד כסף על כל דיווח. **החציון של מקרי דרגה A שבהם סוכן ניהל כסף בעצמו נמצא סביב האפס ונוטה לשלילי.**

**מה שכן מרוויח כסף אמיתי, ובסכומים גדולים, זה שלושה דברים — ואף אחד מהם אינו "סוכן אוטונומי":**
*ראשית, תשתית שגובה עמלה מפעילות אנושית.* Clanker ייצר $34M+ בעמלות מאומתות on-chain — אבל 40–80% מהן הולכות לבני אדם, והסוכן עצמו לא צובר דבר. הוא ממיר טקסט לפריסת חוזה. זה A3.
*שנית, פייפליין תוכן שמוריד את עלות היחידה לאפס.* Adavia Davis מייצר ~$700,000 בשנה עם מרווח 85–89%, ו-Fortune אימת את רשומות ה-AdSense. אבל הוא עובד שעתיים ביום, כל יום, על תוכנה קניינית שנבנתה עם שותף — ורק 3% מערוצי האוטומציה מגיעים למונטיזציה בכלל.
*ושלישית, מכירת האתים לחופרים.* Claude Code לבדו עשה $8 מיליארד בקצב שנתי במאי 2026 — יותר מכל שאר המקרים בתחקיר הזה יחד, כפול אלף.

**והסכום האישי הגדול ביותר שנמצא בכל התחקיר — $10 מיליון — הוא הונאה פלילית** שהסתיימה בהודאה באשמה. זה לא מקרה קצה: שלושת הסכומים הגדולים ביותר בתחקיר הם פשע, הפרת מדיניות פלטפורמה, וכלכלת טוקנים ספקולטיבית שקרסה ב-97%.

**כדי לשחזר משהו כאן צריך לדעת מה באמת נדרש.** לא "להדליק סוכן". לתוכן: 12–18 חודשים לפני מונטיזציה, תוכנה קניינית, שעתיים ביום לנצח, ו-97% סיכוי להיכשל לפני שהערוץ בכלל מונטז. לשירותים: זו סוכנות — $3k–$10k לפרויקט פשוט, $20k–$50k למורכב, ולקוחות שצריך למכור להם. זו עבודה, לא הכנסה פסיבית. למסחר: תוחלת שלילית לפי הנתונים הטובים ביותר שיש, וכל חלון שנפתח נסגר תוך חודשיים — $115k לשבוע הפך ל-$5k–$15k לשבוע במרץ 2026. ולתשתית: צריך פלטפורמה עם משתמשים לפני שיש עמלות.

**ומעל הכל — אין תעלה.** כל ערוץ יחיד שסוכנים הצליחו בו בתחקיר הזה נסגר או נדחס תוך 6–18 חודשים: גוגל הגדירה scaled content abuse כספאם, HackerOne קיצצה תשלומים כי AI הציף אותה, GitHub העביר את הפרסים הגבוהים לשכבה סגורה, Etsy דרשה גילוי ובית המשפט העליון שלל זכויות יוצרים, Polymarket שינתה חוקים וחלון הארביטראז' התכווץ ל-2.7 שניות. **הסוכנים שהצליחו הרסו בעצמם את הכלכלה של הקטגוריה שנכנסו אליה.**

התחום זז מהר, והנתונים מ-2026 טובים בהרבה מאלה של 2024 — יש היום ניסויים אמיתיים עם כסף אמיתי ותוצאות מפורסמות, כולל התוצאות הרעות. אבל נכון לאוגוסט 2026, **הפער בין "סוכן AI מרוויח כסף" לבין "אדם מרוויח כסף מכלי AI" הוא כמעט כל הסיפור** — והוא בדיוק הפער שכל תעשיית התוכן סביב הנושא מטשטשת, כי הטשטוש הזה הוא מודל ההכנסה שלה.

---

## נספח: מקורות מרכזיים

**מעבדות ומחקר אקדמי**
[Anthropic Project Vend 2](https://www.anthropic.com/research/project-vend-2) · [Anthropic Project Deal](https://www.anthropic.com/features/project-deal) · [Vending-Bench (arXiv)](https://arxiv.org/html/2502.15840v1) · [Andon Labs](https://andonlabs.com/evals/vending-bench-2) · [TheAgentCompany (arXiv)](https://arxiv.org/abs/2412.14161) · [NeurIPS 2025](https://neurips.cc/virtual/2025/poster/121705) · [GPT-4 System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf) · [METR ARC evals](https://metr.org/blog/2023-03-18-update-on-recent-evals/) · [ביקורת על Sakana (arXiv)](https://arxiv.org/pdf/2502.14297) · [Epoch AI](https://epoch.ai/benchmarks/vending-bench-2) · [AI Digest / Sage](https://theaidigest.org/village/blog/season-recap-agents-raise-2k)

**עיתונות חוקרת**
[Fortune — Adavia Davis](https://www.fortune.com/2025/12/30/ai-slop-faceless-youtube-accounts-adavia-davis-user-generated-content) · [TechCrunch — Truth Terminal](https://techcrunch.com/2024/12/19/the-promise-and-warning-of-truth-terminal-the-ai-bot-that-secured-50000-in-bitcoin-from-marc-andreessen/) · [TechCrunch — Project Vend](https://techcrunch.com/2025/06/28/anthropics-claude-ai-became-a-terrible-business-owner-in-experiment-that-got-weird) · [The Block — Freysa](https://www.theblock.co/post/328747/human-player-outwits-freysa-ai-agent-in-47000-crypto-challenge) · [Forbes — Michael Smith](https://www.forbes.com/sites/lesliekatz/2024/09/08/man-charged-with-10-million-streaming-scam-using-ai-generated-songs/) · [Decrypt — Zerebro](https://decrypt.co/350928/faking-death-zerebro-founder-unveils-ai-manifesto-solana-coin) · [CyberScoop — XBOW](https://cyberscoop.com/is-xbows-success-the-beginning-of-the-end-of-human-led-bug-hunting-not-yet/) · [IEEE Spectrum — Moltbook](https://spectrum.ieee.org/moltbook-agentic-ai-agents-openclaw) · [CoinDesk — x402](https://www.coindesk.com/markets/2026/03/11/coinbase-backed-ai-payments-protocol-wants-to-fix-micropayment-but-demand-is-just-not-there-yet) · [TIME — AI Village](https://time.com/7330795/ai-village-chatgpt-gemini-claude/) · [SCMP — Alpha Arena](https://www.scmp.com/tech/tech-trends/article/3330461/deepseek-and-qwen-ai-models-crush-western-rivals-cryptocurrency-trading-challenge)

**נתונים גולמיים ואימות**
[Chainalysis — x402](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/) · [CoinGecko — ai16z](https://www.coingecko.com/en/coins/ai16z) · [Messari — ai16z](https://messari.io/project/ai16z) · [Virtuals — aixbt](https://app.virtuals.io/virtuals/1199) · [Clanker Docs](https://clanker.gitbook.io/clanker-documentation/general/creator-rewards-and-fees) · [GitHub — ChatGPT Micro-Cap](https://github.com/LuckyOne7777/ChatGPT-Micro-Cap-Experiment) · [GitHub — AI Scientist v2](https://github.com/sakanaai/ai-scientist-v2) · [Arkham Research](https://info.arkm.com/research/the-first-ai-millionaire)
