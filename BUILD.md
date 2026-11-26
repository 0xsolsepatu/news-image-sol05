# BUILD — news-image-20261126 "Atlas Ledger"

Entry: newspaper front page summing up Thursday 26 November 2026.
Built in a fresh session started after the competition opened (07:00 WIB /
00:00 UTC 26 Nov 2026). All code written from scratch in this session;
the 25 Nov renderer was read once for layout-geometry reference only.

## Design

- 1024×1024 PNG, cream paper (#F7F1E3), serif masthead
  "THE WORLD IN ONE DAY" + "THURSDAY 26 NOVEMBER 2026".
- 6-number stat strip: US GDP +4.3% (BEA) · jobless claims 189,000
  (Labor Dept) · KOSPI −6.2% (Reuters) · Thanksgiving storm 250M+ in path
  (Fox Weather) · Colombia hostages freed 76 (BBC) · alcohol harm 3.2M women
  (AIHW) — stat 6 tagged [26 Nov] in a dark pill.
- 3 lead panels with flat drawn illustrations (storm clouds + rain +
  parade balloon; tariff container ship; GDP growth chart) + verification
  labels + source tags.
- 9-card grid (stories #7–#15), each with a dark [25 NOV] pill.
- 18-item tail list: pure stories #2, #3, #4 first (pale "26 NOV" pills),
  then #16–#30 (dark [25 NOV] pills; #16 also carries a red CLAIM pill).
- World map with 6 numbered pins + legend; DATE CHECK box; footer
  "MAKE.FUN // 26 NOVEMBER 2026 // 24-HOUR GLOBAL SUMMARY".

## Gemini design review (GO) — changes applied

1. Lead order changed: Lead 1 = #1 Thanksgiving storm (pure 26 Nov),
   Lead 2 = #5 US tariffs [25 Nov], Lead 3 = #6 US GDP [25 Nov].
2. Stat strip as listed above; stat 6 explicitly tagged [26 Nov].
3. Every [25 Nov] tag is a high-contrast dark pill with white bold text
   (leads, grid cards, tail list) — no plain inline brackets anywhere.

## Stories (30: 4 pure 26 Nov, 26 flagged [25 Nov])

Pure 26 Nov: #1 Thanksgiving storm slams US East Coast · #2 India marks
77th Constitution Day, 26/11 · #3 Chess title deadlocked 1-1 as Game 3 looms
(Game 3 "today", no invented result) · #4 3.2m Australian women harmed by
drinkers.

Flagged [25 Nov]: #5 US unveils new tariffs on China, EU ("proposes", not in
force) · #6 US economy grows 4.3%, fastest in 3 years · #7 Asteroid's crash
scar seen up close at last · #8 Ramaphosa wins court fight on Farmgate ·
#9 76 hostages freed in Colombia supermarket · #10 Army blows up 5 tons of
toxic explosives · #11 Israel kills Hamas security chief in Gaza · #12 RSF
drones kill 19 civilians in Sudan ("Rights group:") · #13 Ukraine hits 5
Russian jets at air base ("Kyiv says") · #14 Bangladesh garment pay up 36%
after protests · #15 Malaysia sues Google for $146m over YouTube · #16
Houthis claim hit on Saudi's biggest refinery (CLAIM — hit unconfirmed by
Riyadh) · #17 9 dead, 17 trapped in Indonesia mine flood · #18 6 die as
Cessna plunges into Gulf of Mexico · #19 Cairo tanker fire kills 31 on ring
road · #20 Lebanon to open second airport next month · #21 N. Korea expels
Swiss envoy in sanctions row · #22 Judges urge dropping Netanyahu bribery
case ("urge", not a ruling) · #23 Saudi national seized by IS suspects in
Niger · #24 US jobless claims fall to 189,000 in a week · #25 Wall St
rebounds after 1,100-point Dow plunge · #26 Poundland collapses, 11,000 jobs
at risk · #27 Liverpool cruise, United held in wild UCL night · #28 Asia
stocks slump as AI rout deepens · #29 1,220 players sign up for IPL 2027
auction · #30 Flipkart CEO quits after 11 years at helm.

All 30 headlines and decks rendered verbatim from RESEARCH.md (scripted
cross-check: 0 missing). No story dropped or changed.

DATE CHECK box: masthead date + "26 of the 30 stories stem from Wed 25 Nov.
Each is flagged [25 Nov] where it appears." + rejected: NZ–India Test draw
(23 Nov), Nepal quake (24 Nov), COP31 ended (22 Nov), Shenzhou-24 (already
in the 25 Nov image).

## Files

- `render.py` — build tool (NOT committed to GitHub): draws entry.png.
- `main.py` — entrypoint (committed): stdlib only, copies entry.png to
  $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), verifying PNG
  magic + IEND trailer + ≤1 MiB + sha256 of the copy. Written from scratch,
  then revised once (added trailer + size checks).
- `entry.png` — the image (committed).
- `README.md` — from the live requirements template (badges for
  0xsolsepatu/news-image-sol05, run command, referral r4c0y56z).
- `LICENSE` — MIT. `.makefun/owner.json` — wallet claim file.
- `RESEARCH.md`, `gemini-design-prompt.txt`, `gemini-design-response.txt`
  — records (the Gemini files are NOT committed to GitHub).

## Verification (all passed)

- Render twice: byte-identical.
  sha256 `7bbfee5259a13e5b706201fb6e2ca82ba38c7bf57d8daa8bdd1753242f71e1bc`
- entry.png: 1024×1024, 234,504 bytes (< 1,048,576).
- main.py twice to two different output dirs: both outputs byte-identical
  to entry.png (same sha256 above).
- Renderer audit: 0 issues (20 OK lines, no OVERFLOW / TOO LONG).
  Two defects found during visual review and fixed: lead #6 title wrapped
  to 3 lines at 24pt (title font reduced to 22pt); stat-6 pill overflowed
  its box (strip raised to 54px, pill shortened to 14px).
- 300px downscale read visually: masthead, date, all 6 stat numbers, and
  all 3 lead headlines legible; dark [25 Nov] pills read as clear dark
  markers across grid and tail; footer legible. PASS.
- 1024px visual read: every headline/deck/stat/date tag/footer legible, no
  overlap, no text past edges. PASS (after the two fixes above).
- Scripted cross-check: all 30 headlines + all 30 decks verbatim in
  render.py; pure/flagged 4/26; lead order storm/tariffs/GDP; all 6 stat
  numbers present; masthead date correct; all 30 stories covered by
  leads + grid + tail; README badges/placeholders verified (no placeholders
  left); main.py stdlib-only, no network.

## Status

Built and committed locally only. NOT pushed, NOT submitted — GitHub repo
creation + submit are the parent's job.
