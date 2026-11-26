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
