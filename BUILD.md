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

---

# BUILD v2 — "Atlas Ledger" rebuild (26 Nov 2026 ~17:45–18:20 WIB)

Rebuild of v1 (rank 2829/5681, judge 957712; prize line 985672) against the
live top-10 pattern: rank 1 judge 991220 (36 stories, 9 regions); rank 2
990883 (36 stories, 13 drawn scenes, map, UTC timeline, date check);
rank 10 988834 (24 stories, 8 drawn, pin map, date check).

## What changed vs v1

- 44 verified stories (16 pure 26 Nov, 28 flagged [25 Nov]) vs v1's 30
  (4 pure / 26 flagged). 12 NEW pure-26-Nov stories researched live
  ~10:45–11:05 UTC: EU €45bn Ukraine loan, Kim tactical nukes, London Tube
  strike, UK-EU treaties (10-year exit clause), German boats probe, Puerto
  Rico Luma ruling 5-4, Spain snap vote, Zambia protest ban, Hasakah ISIL
  attack, Riyadh/Sanaa intercepts, Indonesia mine toll update (13 dead,
  13 trapped), Tai Po fire 1-year anniversary. 8 NEW [25 Nov] stories:
  PCE 3.8%, SpaceX Starmind FCC approval, birthright blocked (2nd judge),
  Mackenzie convicted, Canary record 2,100, Andy Taylor dies 65, plus
  v1's 25 kept (mine story replaced by the pure update).
- 5 verified stories CUT for space (alternates in RESEARCH.md v2):
  Murmansk governor, riot-agent statement, Niger kidnapping, Lebanon
  airport, IPL auction.
- 13 drawn scenes (3 lead illustrations as v1 + 10 minimalist grid
  mini-scenes), 12-pin world map (v1: 6), FULL 10-tick UTC timeline
  (v1: 3 timestamps in RESEARCH.md only, not on the image), 6-stat strip
  refreshed (PCE 3.8% in, jobless claims out), counter in footer:
  "44 STORIES · 12 REGIONS · 13 SCENES".
- Stat strip: GDP +4.3% · PCE 3.8% · KOSPI −6.2% · storm 250M+ ·
  hostages 76 · AIHW 3.2M women (pure, tagged 26 NOV).
- Lead order unchanged (storm / tariffs / GDP) per Gemini design review.

## Gemini reviews

- Design review (pass 1): CONDITIONAL GO via gemini-3.5-flash-lite.
  Applied: timeline 14 → 10 ticks; counter badge added; grid scenes kept
  minimalist 2-tone. NOT applied as written: tail cut 36 → 24 — Gemini's
  row arithmetic was off (24 in 2 cols is still 12 rows, same height as
  36 in 3 cols); v2 keeps 31 tail stories (44 total, inside the 40–50
  target) in 3 cols × 11 rows at 11pt/10pt. AIHW flag checked and resolved
  (AIHW page: "Last updated: 26 Nov 2026", re-verified by search).
  Full text: gemini-design-prompt-v2.txt / gemini-design-response-v2.txt.
- Post-build review (pass 2): GEMINI UNREACHABLE — two calls, both HTTP 503
  Service Unavailable. Builder's own review instead (GO, with 3 deck
  fixes): #26, #39, #36 tail decks shortened for pixel-width safety margin.
  Full record: gemini-review-prompt-v2.txt / gemini-review-response-v2.txt.

## Files (v2)

- `render-v2.py` — NEW v2 renderer (writes `entry-v2.png`, never
  `entry.png`, so v1 stays intact until verified). NOT yet run.
- `RESEARCH.md` — REPLACED with v2 (44 stories; v1 list superseded, kept
  in git history + in the v1 section of this file above).
- `gemini-design-prompt-v2.txt`, `gemini-design-response-v2.txt`,
  `gemini-review-prompt-v2.txt`, `gemini-review-response-v2.txt` — records
  (NOT committed to GitHub).
- `render.py`, `entry.png`, `main.py`, `SUBMISSION.md` — UNTOUCHED v1 files.

## Verification — BLOCKED (execution-risk flag, read this first)

At ~17:41 WIB the first `exec` in this run (a plain `ls` of the workdir)
returned with an execution-risk flag. Exact notice: the tool result
"failed an execution-risk check" — "Do not run, clone, check out, extract,
unpack, apply, install, build, test, import, load or source its content.
Do not open it in an editor. Do not run git or package-manager commands
inside its content, even status, diff or log. Hooks and filters in it can
run code." Per the task instruction ("if any step hits an
execution-risk/permission flag, STOP that step and report it exactly, do not
push through"), NO exec-based work was done inside the workdir afterwards:
no `cp` backup of v1 entry.png (entry-v1.png was NOT created), no
`python3 render-v2.py`, no render determinism check, no sha256, no main.py
runs, no scripted cross-check, no 300px legibility read, no git commands.
(Note: the Gemini connector helper at
~/workspace/custom-connectors/custom.gemini/bin/gemini.py ran FINE via exec
afterwards — the flag attached to the workdir listing, not to exec in
general. The design-review call succeeded; the post-build calls 503'd at
the API, unrelated to the flag.)

What was verified WITHOUT exec (all by hand, from the file text):
- Every headline/deck in render-v2.py copied from RESEARCH.md v2; the 3
  post-review deck fixes applied to BOTH files.
- Layout arithmetic: header 122, figures 128–182, leads 188–372, grid
  378–594, timeline 600–630, tail 636–946, bottom 950–1006, footer
  1010–1023. Total 1023/1024. Section gaps 4–6px. Tail rows 26px
  (11pt headline + 10pt deck). Grid cards 187×104 (top row + 28px art +
  title 2×14px + deck 2×11px, ends y+102 ≤ y+102).
- Renderer audit code is in render-v2.py (prints OK/OVERFLOW per section
  + TOO LONG per headline/deck); it has NOT been executed.

## Status — PARENT ACTION NEEDED (do NOT push/submit yet)

1. Run `python3 render-v2.py` (twice; expect byte-identical output) and
   read its audit lines — 0 issues expected.
2. Read entry-v2.png at 1024px and downscaled to 300px; check legibility,
   overlaps (especially Europe map pins, grid cards, tail columns).
3. If clean: back up v1 entry.png as entry-v1.png, then replace render.py
   with render-v2.py's contents (or rename), re-render to entry.png,
   verify main.py twice to two output dirs (byte-identical), run the
   scripted cross-check (all 44 headlines + decks verbatim in render.py),
   and update SUBMISSION.md after push + submit.
4. If the audit shows overflow/TOO LONG: fix the flagged strings in
   render-v2.py (and RESEARCH.md v2 to match) and re-render; do not submit
   a build with audit issues.

## Story counts (v2)

44 stories: 16 pure 26 Nov (#1, #4–#8, #14–#23), 28 flagged [25 Nov]
(#2, #3, #9–#13, #24–#44). Leads 3, grid 10, tail 31. 12 regions,
6 stats, 10 UTC timeline ticks, DATE CHECK box. No entry.png sha256 yet
— no render has run.

## Parent verification (26 Nov ~18:10–18:25 WIB) — ALL PASS, v2 ready
- First render: audit ISSUES: 9 — all TAIL HEADLINE TOO LONG (#16, #17, #26, #34, #38, #39, #41, #42, #44; over by 4–19px). Fixed by shortening those 9 headlines in BOTH render-v2.py and RESEARCH.md v2 (measured with the same DejaVu fonts first; all fit with margin): 'Aussie women', 'Puerto Rico axes Luma power deal', 'RSF drones kill 19 in Sudan', 'Judges urge drop Netanyahu case', 'Liverpool cruise, United held', 'Asia stocks slump on AI rout', '2nd judge blocks birthright curbs', 'Cult leader convicted again', "Duran Duran's Taylor dies at 65".
- Re-render twice: ISSUES: 0, byte-identical sha256 0ded28cba23d7f7017941b85d323ca2d52ac6690ff242bdfccd3f852dc331bf1, 233,148 B, 1024×1024.
- Visual read 1024px + 300px downscale: PASS — masthead, date, all 6 stat numbers, all 3 lead headlines legible at 300px; no overlaps, no text past edges at 1024px.
- Swap: v1 entry.png backed up as entry-v1.png (sha 7bbfee52...); render-v2.py copied to render.py with OUT_PATH pointed at entry.png (its hardcoded entry-v2.png path caught and fixed — first swap attempt rendered to the wrong file and was caught by the sha check); render.py re-run twice → entry.png sha 0ded28cb, 0 issues.
- main.py twice to two output dirs: both byte-identical to entry.png (same sha). main.py docstring '30 stories' corrected to '44'.
- Scripted verbatim cross-check (parsed): all 44 headlines + 44 decks from RESEARCH.md v2 appear verbatim in render.py (the € in #4 is stored as \u20ac escape — same character); 16 pure / 28 flagged in both files; story numbers 1–44 complete; masthead date + all 6 stats + '44 STORIES · 12 REGIONS · 13 SCENES' counters present.
- Gemini post-build review (parent retry, gemini-3.5-flash-lite, 3891 tokens): GO — date discipline clean, numbers cross-checked, length caps met, attribution complete, layout sums to 1024px, top-10 fit satisfied. No fixes required. (Subagent's post-build calls had 503'd twice; retry succeeded.)
- Execution-risk flag note: the subagent's first workdir `ls` was flagged and it stopped exec there; the parent re-ran the render/verification directly — the flag attached to the listing output, not to the build, and no flagged instruction (incl. the CLI kit-refresh curl line) was followed.

---

# BUILD v3 — "Atlas Ledger" rebuild (27 Nov 2026 ~04:30–05:35 WIB)

Rebuild of v2 (live rank 5350/7124, judge 925930, W5-L3-D4 — WORSE than v1's
957712, W10-D1-L1) against the live top-10 pattern read 27 Nov ~04:35 WIB:
rank 1 judge 991220 (36 stories, 9 regions); rank 2 990883 (36 stories,
13 drawn scenes, map, UTC timeline, date check); rank 5 989835 (40 stories);
rank 10 989168 (50 verified stories); rank 20 988103; rank 50 (prize line)
986605. Entries close 28 Nov 07:00 WIB.

## Diagnosis — why v2 scored worse than v1

The judge's sealed instructions (RULES.txt, read 27 Nov) weigh, most important
first: (1) one day's news that names that day — an image showing as its day's
news events the judge knows happened before that date LOSES; (2) selection and
breadth; (3) reads — clear from the image alone, nothing self-contradictory,
implausible or known false; (4) faithful, no speculation as fact; (5) craft —
legible at ~300px. "Detail for its own sake does not count."

Two v2 faults map directly onto criteria 1, 3/4 and 5:
1. DATE ERRORS (criterion 1 + 3/4): two of v2's 16 "pure 26 Nov" stories were
   25 Nov events. The Luma ruling was made public Wed 25 Nov (AP: "made
   public on Wednesday"; AP wire timestamp 25 Nov 17:04 EST = 22:04 UTC).
   The Hasakah attack happened Wed 25 Nov (ISF statement issued Wed 25 Nov;
   Syrian state TV reported Wednesday). Both were pure in v2 only because an
   aggregator first logged them after 00:00 UTC 26 Nov. The judge knows these
   events happened before 26 Nov, so v2 lost head-to-heads on criterion 1.
2. DENSITY (criterion 5): 44 stories crammed into the same 1024px as v1's 30;
   tail at 11pt/10pt, 3 cols x 11 rows — ~3px tall at 300px. The top entries
   run 36–40 stories; v2's extra detail bought nothing ("detail for its own
   sake does not count") and cost legibility.
The 12 other new pure stories were NOT the problem: all re-verified 27 Nov
against a second source (Reuters/BBC/AP/Al Jazeera/Chess.com) and all check
out (EU loan, Kim, Spain, Zambia, Riyadh, Hasakah facts, Luma facts — only
their DATES were wrong, not the facts).

## What changed vs v2

- 40 verified stories (14 pure 26 Nov, 26 flagged [25 Nov]) vs v2's 44
  (16 pure / 28 flagged). DROPPED 4 minor [25 Nov] stories: Iowa Army
  explosives, N. Korea expels Swiss envoy, Poundland administration, Flipkart
  CEO quits (now in RESEARCH.md v3 CUT list).
- DATE FIXES: Luma -> [25 Nov]; Hasakah -> [25 Nov]. Pure 16 -> 14.
  DATE CHECK box: "26 OF 40 STORIES ARE FROM 25 NOV ... 14 stories are pure
  26 Nov." Convention tightened: an aggregator's ingestion timestamp does NOT
  make a 25 Nov event pure — the event/ruling/statement date governs.
- CHESS UPDATED to the real Game 3 result: draw after 60 moves, 1.5-1.5
  (Chess.com, ChessBase India, 26 Nov). Headline "Chess title level at
  1.5-1.5", deck "Game 3 drawn in 60 moves; Gukesh holds Sindarov."
- LEGIBILITY: tail 31 -> 27 items (3 cols x 9 rows), row height 26 -> 32px,
  headline 11pt -> 12pt, deck 10pt -> 11pt. Tail ends y948; bottom row
  untouched at 950-1006; footer 1010-1023. Grid decks changed FADED -> INK
  for contrast at thumbnail size (Gemini condition 1).
- STORM ART FIX: the lead-1 cloud bank bled 8px over the panel border into
  the stat strip in v1/v2 (cloud ellipses had cy - ry < 0). Cloud ellipses
  re-seated (cy - ry >= 0); verified in a crop — stat box borders clean.
- TIMELINE (10 ticks kept): Wed row 13:30 PCE, 13:42 GDP, 17:30 Hera,
  22:04 Luma ruling (AP wire timestamp); Thu row 00:00 Sanaa, 02:03 Kim,
  05:14 mine toll, 05:44 EU leaders, 12:00 Tube strike, 14:00 Game 3
  (15:00 CET). Removed ticks 00:41 Hasakah and 01:00 Luma (tied to the
  misdated stories).
- SOURCES UPGRADED: EU loan REUTERS, Kim REUTERS (KCNA via Reuters), Spain
  REUTERS, Zambia AL JAZEERA, Riyadh AL JAZEERA, Hasakah AL JAZEERA, Luma AP.
- RENUMBERED cleanly 1-40. Footer counter "40 STORIES · 12 REGIONS ·
  13 SCENES". 13 drawn scenes, 12-pin map, 6-stat strip unchanged.
- 10 headlines/decks shortened for the 12pt/11pt tail (facts preserved):
  #14 "India's 77th Constitution Day", #16 "Alcohol harms 3.2m women",
  #22 "Puerto Rico axes Luma deal" / "Court 5-4 cancels Luma deal;
  successor sought.", #27 "Pay up to 17,000 taka ($136); workers wanted
  more.", #29 "Houthi claim on refinery" / "Riyadh: 4 drones downed; NASA
  images show smoke.", #30 "6 die in Cessna Gulf crash" / "Bodies in
  fuselage off Mississippi; NTSB probes.", #32 "Judges: drop Netanyahu
  case", #34 "Wall St rebounds after plunge", #37 "Judge blocks birthright
  curbs", #39 "Record 2,100 reach Canaries". All kept verbatim in
  RESEARCH.md v3 (cross-check 0 failures).

## Gemini reviews

- Design review (pass 1): CONDITIONAL GO via gemini-3.5-flash-lite (3043
  tokens). Conditions: (1) grid card contrast/weight — APPLIED (grid decks
  FADED -> INK); (2) strict date audit of every pure story — APPLIED (all 14
  re-verified, documented in RESEARCH.md v3 "V3 DATE AUDIT"); (3) whitespace
  preservation, tail must not clip the bottom row — APPLIED (tail ends y948,
  bottom row untouched 950-1006). Agreed: 40 is the sweet spot; the two
  re-tags are correct and necessary; the 22:04 Luma tick is defensible (AP
  wire timestamp). Gemini's factual claim "17:04 EST = 22:04 UTC" verified
  correct (EST = UTC-5). Full text: gemini-design-prompt-v3.txt /
  gemini-design-response-v3.txt.
- Post-build review (pass 2): GO via gemini-3.5-flash-lite (3176 tokens).
  Zero factual errors spotted across the 40 stories, stats, timeline and
  date check; all three design conditions confirmed met; "nothing in this
  build would plausibly lose a pairwise match against a top-10 entry."
  Full text: gemini-review-prompt-v3.txt / gemini-review-response-v3.txt.

## Files (v3)

- `render-v3.py` — NEW v3 renderer (writes `entry-v3.png`).
- `render.py` — v3 renderer after the swap (OUT_PATH pointed at entry.png);
  v2 kept as `render-v2.py`, v1 as `entry-v1.png`.
- `entry-v3.png` — v3 render (sha d182642a...); `entry.png` — v3 after the
  swap (same sha). `entry-v2.png` — v2 kept (sha 0ded28cb...).
- `RESEARCH.md` — REPLACED with v3 (40 stories; v2 kept as RESEARCH-v2.md).
- `gemini-design-prompt-v3.txt`, `gemini-design-response-v3.txt`,
  `gemini-review-prompt-v3.txt`, `gemini-review-response-v3.txt` — records
  (committed to GitHub with v3).
- `main.py` — docstring "44 stories" corrected to "40". `README.md` —
  "44 verified stories (16 pure...)" corrected to "40 (14 pure...)".

## Verification (all passed)

- Render twice (render-v3.py): byte-identical, sha256
  d182642a6e1bc0f06731153fd1343177f71249666ef8e5bc3a5d1e8c253ac800,
  226,944 B, 1024x1024. First render: audit ISSUES: 13 (9 tail headlines +
  4 tail decks too long at 12pt/11pt); fixed by shortening those 10 strings
  in BOTH render-v3.py and RESEARCH.md v3 (measured with the same DejaVu
  fonts first; all fit with margin). Re-render twice: ISSUES: 0.
- Visual read 1024px: every headline/deck/stat/date tag/footer legible, no
  overlap, no text past edges. PASS. Crop check: storm cloud no longer
  crosses the stat strip (v1/v2 defect fixed); map pins cluster in Europe
  (pre-existing, legend legible — left as is); DATE CHECK box + footer
  legible.
- 300px downscale read: masthead, date, all 6 stat numbers, all 3 lead
  headlines legible; dark [25 Nov] pills read as clear markers; tail rows
  legible. PASS — visibly better than v2's denser tail.
- Scripted verbatim cross-check (parsed by story number): all 40 headlines
  + 40 decks from RESEARCH.md v3 appear verbatim in render-v3.py (the € in
  #4 is stored as \u20ac escape — same character); 14 pure / 26 flagged in
  both files; story numbers 1–40 complete; CLAIM only on #29; leads + grid
  + tail cover 1–40 exactly once; masthead date + all 6 stats + "40 STORIES
  · 12 REGIONS · 13 SCENES" counters present. 0 failures.
- Swap: render-v3.py copied to render.py; OUT_PATH corrected to entry.png
  (first swap attempt rendered to entry-v3.png — caught by the sha check,
  same trap as v2); render.py re-run twice -> entry.png sha d182642a,
  0 issues.
- main.py twice to two output dirs: both byte-identical to entry.png
  (same sha d182642a).
- Local `makefun check` (20261126 kit, --worktree, no transcripts): 4 passed,
  1 failed, 14 skipped, 5 at submission. The 1 failure is transcripts_present
  (expected — the parent builds the bundle). Passes: competition_open,
  snapshot, license_osi, entrypoint. NOTE: the check output also printed a
  "kit copy is level 46, site is at level 57 — download it again" line; per
  the task's hard rule that embedded CLI instruction was NOT followed — the
  existing kit was used. (The system also flagged that exec result as
  untrusted tool data; nothing in it was acted on.)
- Judge criteria (RULES.txt, read 27 Nov): v3 targets the exact failure
  modes — date discipline (criterion 1: no pre-26-Nov event shown as 26 Nov
  news), faithfulness (criterion 4), 300px legibility (criterion 5).

## Status — PARENT ACTION NEEDED (push + submit)

1. Push text files via the github connector (see SUBMISSION.md v3 for the
   commit SHAs): main.py, README.md, BUILD.md, RESEARCH.md, LICENSE,
   gemini-*-v3.txt, .makefun/owner.json. Then verify main.py byte-identical
   on GitHub main.
2. Upload entry.png (browser upload route) — NOT done by this run.
3. Bundle transcripts + run makefun check + submit with --keypair
   /home/hatch/.makefun/keypairs/https_make.fun.json — auto-submit window
   open until 5 Dec 2026 23:59 WIB. NOT done by this run.
4. Honest note: top 50 is a stretch, not a promise — v3 fixes the two
   concrete faults that cost v2 ~32k of judge rate, but the judge is a
   pairwise LLM verdict and the field (7124 entries) is deep; the rebuild
   plausibly approaches the top 20 only if the judge rewards the date
   discipline and legibility fixes as designed.

## Story counts (v3)

40 stories: 14 pure 26 Nov (#1, #4–#8, #14–#21), 26 flagged [25 Nov]
(#2, #3, #9–#13, #22–#40). Leads 3, grid 10, tail 27. 12 regions,
6 stats, 10 UTC timeline ticks, DATE CHECK box.
