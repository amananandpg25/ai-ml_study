import os, re

base = "/Users/amananand/Downloads/SDE/ai:ml"

issues = {}  # filename -> list of issue strings

def add(f, msg):
    issues.setdefault(f, []).append(msg)

# ─── load all files ────────────────────────────────────────────────────────────
contents = {}
for w in range(1, 19):
    fn = f"week{w}.html"
    contents[fn] = open(os.path.join(base, fn)).read()
for extra in ["roadmap.html", "dashboard.html", "resources.html"]:
    p = os.path.join(base, extra)
    if os.path.exists(p):
        contents[extra] = open(p).read()

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 1: WEEK constant matches file number
# ══════════════════════════════════════════════════════════════════════════════
print("\n[1] WEEK CONSTANT vs FILE NUMBER")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    m = re.search(r"const WEEK\s*=\s*(\d+)", c)
    if m:
        declared = int(m.group(1))
        if declared != w:
            add(fn, f"WEEK constant = {declared} but file is week{w}")
            print(f"  ❌ {fn}: WEEK={declared}, file=week{w}")
        else:
            print(f"  ✅ {fn}: WEEK={w}")
    else:
        add(fn, "No WEEK constant found")
        print(f"  ❌ {fn}: No WEEK constant")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 2: XP values per day (all should be 50–500)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[2] XP VALUES PER DAY")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    xp_pairs = re.findall(r'completeDay\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)', c)
    day_ids = sorted(set(int(d) for d in re.findall(r'id="day-(\d+)"', c)))
    bad = []
    for day, xp in xp_pairs:
        xp = int(xp)
        if xp < 50 or xp > 500:
            bad.append(f"Day {day}={xp}XP")
    if bad:
        add(fn, f"Suspicious XP values: {bad}")
        print(f"  ❌ {fn}: {bad}")
    else:
        xps = [int(x) for _, x in xp_pairs]
        print(f"  ✅ {fn}: XP range {min(xps) if xps else 'N/A'}–{max(xps) if xps else 'N/A'}")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 3: Mermaid diagrams per week
# ══════════════════════════════════════════════════════════════════════════════
print("\n[3] MERMAID DIAGRAMS PER WEEK")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    count = len(re.findall(r'class="mermaid"', c))
    days = len(re.findall(r'id="day-\d+"', c))
    if count == 0:
        add(fn, "No mermaid diagrams at all")
        print(f"  ❌ {fn}: 0 diagrams ({days} days)")
    elif count < days:
        print(f"  ⚠️  {fn}: {count} diagrams for {days} days")
    else:
        print(f"  ✅ {fn}: {count} diagrams ({days} days)")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 4: Predict blocks per week
# ══════════════════════════════════════════════════════════════════════════════
print("\n[4] PREDICT BLOCKS PER WEEK")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    predict_blocks = len(re.findall(r'checkPredict\s*\(', c))
    days = len(re.findall(r'id="day-\d+"', c))
    if predict_blocks == 0:
        add(fn, "No predict blocks at all")
        print(f"  ❌ {fn}: 0 predict blocks ({days} days)")
    elif predict_blocks < days:
        print(f"  ⚠️  {fn}: {predict_blocks} predict blocks for {days} days")
    else:
        print(f"  ✅ {fn}: {predict_blocks} predict blocks ({days} days)")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 5: Debug challenges per week (last day only)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[5] DEBUG CHALLENGES")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    debug = len(re.findall(r'class="debug-block"', c))
    if debug == 0:
        add(fn, "No debug-block found")
        print(f"  ❌ {fn}: 0 debug blocks")
    else:
        print(f"  ✅ {fn}: {debug} debug blocks")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 6: Connect-to-next-week bridge
# ══════════════════════════════════════════════════════════════════════════════
print("\n[6] CONNECT-TO-NEXT-WEEK BRIDGE")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    bridge = ("next week" in c.lower() or "week-bridge" in c or 
              "connect" in c.lower() and "next" in c.lower() or
              "coming up next" in c.lower())
    if not bridge:
        add(fn, "No connect-to-next-week bridge")
        print(f"  ❌ {fn}: No bridge found")
    else:
        print(f"  ✅ {fn}: Bridge found")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 7: Misconception blocks
# ══════════════════════════════════════════════════════════════════════════════
print("\n[7] MISCONCEPTION BLOCKS")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    count = len(re.findall(r'class="misconception"', c))
    days = len(re.findall(r'id="day-\d+"', c))
    if count == 0:
        add(fn, "No misconception blocks")
        print(f"  ❌ {fn}: 0 misconceptions ({days} days)")
    elif count < days:
        print(f"  ⚠️  {fn}: {count} misconceptions for {days} days")
    else:
        print(f"  ✅ {fn}: {count} misconceptions ({days} days)")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 8: Task blocks
# ══════════════════════════════════════════════════════════════════════════════
print("\n[8] TASK BLOCKS (task-block class)")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    count = len(re.findall(r'class="task-block"', c))
    days = len(re.findall(r'id="day-\d+"', c))
    if count == 0:
        add(fn, "No task-block elements")
        print(f"  ❌ {fn}: 0 task blocks ({days} days)")
    elif count < days:
        print(f"  ⚠️  {fn}: {count} task blocks for {days} days")
    else:
        print(f"  ✅ {fn}: {count} task blocks ({days} days)")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 9: Resource cards per week
# ══════════════════════════════════════════════════════════════════════════════
print("\n[9] RESOURCE CARDS")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    count = len(re.findall(r'class="[^"]*(?:resource-card|res-card)[^"]*"', c))
    days = len(re.findall(r'id="day-\d+"', c))
    if count == 0:
        add(fn, "No resource cards (resource-card/res-card)")
        print(f"  ❌ {fn}: 0 resource cards ({days} days)")
    elif count < days * 2:
        print(f"  ⚠️  {fn}: Only {count} res-cards for {days} days")
    else:
        print(f"  ✅ {fn}: {count} res-cards ({days} days)")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 10: Duplicate IDs
# ══════════════════════════════════════════════════════════════════════════════
print("\n[10] DUPLICATE HTML IDs")
for fn in [f"week{w}.html" for w in range(1, 19)]:
    c = contents[fn]
    ids = re.findall(r'id="([^"]+)"', c)
    seen = set()
    dupes = []
    for id_ in ids:
        if id_ in seen and id_ not in dupes:
            dupes.append(id_)
        seen.add(id_)
    # Filter out xp-toast, prog-bar type that might be duplicated by templates
    real_dupes = [d for d in dupes if not d.startswith('compiler')]
    if real_dupes:
        add(fn, f"Duplicate IDs: {real_dupes}")
        print(f"  ❌ {fn}: Duplicates: {real_dupes}")
    else:
        print(f"  ✅ {fn}: No duplicate IDs")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 11: renderMermaid call on DOMContentLoaded
# ══════════════════════════════════════════════════════════════════════════════
print("\n[11] RENDERMERMAID ON DOMCONTENTLOADED")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    has_fn = "function renderMermaid" in c
    has_call = "renderMermaid(" in c and "DOMContentLoaded" in c
    if not has_fn:
        add(fn, "Missing renderMermaid function")
        print(f"  ❌ {fn}: No renderMermaid function")
    elif not has_call:
        add(fn, "renderMermaid not called on DOMContentLoaded")
        print(f"  ⚠️  {fn}: renderMermaid exists but not called on DOMContentLoaded")
    else:
        print(f"  ✅ {fn}: OK")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 12: Theme toggle button in topnav HTML
# ══════════════════════════════════════════════════════════════════════════════
print("\n[12] THEME BUTTON IN TOPNAV HTML (id=theme-btn)")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    has_btn = bool(re.search(r'<button[^>]*id=["\']theme-btn["\']', c))
    has_toggle = bool(re.search(r'onclick=["\']toggleTheme\(\)["\']', c))
    if not has_btn and not has_toggle:
        add(fn, "No theme toggle button in HTML body")
        print(f"  ❌ {fn}: Completely missing theme button in HTML")
    elif not has_btn:
        add(fn, "Theme toggle button missing id='theme-btn'")
        print(f"  ⚠️  {fn}: Has toggleTheme() onclick but no id='theme-btn'")
    else:
        print(f"  ✅ {fn}: OK")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 13: Flashcards in weeks 15, 16, 17
# ══════════════════════════════════════════════════════════════════════════════
print("\n[13] FLASHCARDS (weeks 15–17)")
for w in [15, 16, 17]:
    fn = f"week{w}.html"
    c = contents[fn]
    count = len(re.findall(r'class="flashcard"', c))
    print(f"  {'✅' if count > 0 else '❌'} {fn}: {count} flashcards")
    if count == 0:
        add(fn, "No flashcards despite CSS being present")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 14: Roadmap sidebar labels vs week titles
# ══════════════════════════════════════════════════════════════════════════════
print("\n[14] ROADMAP SIDEBAR LABELS")
roadmap = contents["roadmap.html"]
# Extract nav items that link to week files
nav_links = re.findall(r'<a class="nav-item" href="(week\d+\.html)"[^>]*>(.*?)</a>', roadmap, re.DOTALL)
week_titles = {}
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    m = re.search(r'<title>(.*?)</title>', c)
    week_titles[fn] = m.group(1).strip() if m else "?"

for href, inner in nav_links:
    # Clean inner text
    inner_clean = re.sub(r'<[^>]+>', '', inner)
    inner_clean = re.sub(r'\s+', ' ', inner_clean).strip()
    actual_title = week_titles.get(href, "?")
    # Extract the topic part from title (after "Week N — ")
    title_topic = re.sub(r'^Week \d+ — ', '', actual_title.split('|')[0]).strip()
    sidebar_topic = re.sub(r'^Week \d+ — ', '', inner_clean).strip()
    # Remove the day range spans
    sidebar_topic = re.sub(r'\d+[–-]\d+', '', sidebar_topic).strip()
    if title_topic.lower() != sidebar_topic.lower() and title_topic[:20].lower() != sidebar_topic[:20].lower():
        print(f"  ⚠️  {href}: Sidebar='{inner_clean}' | Title='{actual_title.split('|')[0].strip()}'")
        add("roadmap.html", f"Sidebar label mismatch: {href} sidebar='{inner_clean}' vs title topic='{title_topic}'")
    else:
        print(f"  ✅ {href}: Labels match")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 15: Roadmap: sections referenced in nav that don't exist
# ══════════════════════════════════════════════════════════════════════════════
print("\n[15] ROADMAP: SHOWSECTION TARGETS EXIST AS HTML SECTIONS")
section_ids_in_nav = re.findall(r"showSection\('([^']+)'", roadmap)
section_ids_in_html = set(re.findall(r'id="([^"]+)"', roadmap))
for sid in set(section_ids_in_nav):
    if sid not in section_ids_in_html:
        add("roadmap.html", f"showSection('{sid}') target not found as id in roadmap.html")
        print(f"  ❌ roadmap.html: showSection('{sid}') — no matching id found!")
    else:
        print(f"  ✅ roadmap.html: '{sid}' exists")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 16: Title consistency
# ══════════════════════════════════════════════════════════════════════════════
print("\n[16] TITLE TAG CONSISTENCY")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    m = re.search(r'<title>(.*?)</title>', c)
    title = m.group(1).strip() if m else "MISSING"
    if 'v2' in title.lower() or 'v3' in title.lower():
        add(fn, f"Version suffix in title: '{title}'")
        print(f"  ⚠️  {fn}: '{title}'")
    elif '135-Day AI/ML Roadmap' not in title:
        add(fn, f"Missing standard suffix in title: '{title}'")
        print(f"  ⚠️  {fn}: Missing standard suffix: '{title}'")
    else:
        print(f"  ✅ {fn}: OK")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 17: Week 1 has v2 label
# ══════════════════════════════════════════════════════════════════════════════
print("\n[17] BRAND LABEL v2 CHECK")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    brand_m = re.search(r'class="brand"[^>]*>(.*?)</div>', c, re.DOTALL)
    if brand_m:
        brand = brand_m.group(1).strip()
        if 'v2' in brand.lower():
            add(fn, f"Brand has 'v2': '{brand}'")
            print(f"  ⚠️  {fn}: Brand='{brand}'")
        else:
            print(f"  ✅ {fn}: Brand OK")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 18: Dashboard: week state keys
# ══════════════════════════════════════════════════════════════════════════════
print("\n[18] DASHBOARD: READS ALL 17 WEEK STATES")
dash = contents.get("dashboard.html", "")
has_dynamic = "w${weekNum}-state" in dash or "w${w.id}-state" in dash or "`w${" in dash
if has_dynamic:
    print(f"  ✅ dashboard.html: Reads all 17 week states dynamically")
else:
    add("dashboard.html", "Missing dynamic week state loading (w${weekNum}-state)")
    print(f"  ❌ dashboard.html: Missing dynamic week state loading")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 19: Hinglish summaries
# ══════════════════════════════════════════════════════════════════════════════
print("\n[19] HINGLISH SUMMARIES")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    count = len(re.findall(r'class="hinglish"', c))
    days = len(re.findall(r'id="day-\d+"', c))
    if count == 0:
        print(f"  ⚠️  {fn}: 0 hinglish summaries ({days} days)")
        add(fn, "No hinglish summaries")
    elif count < days:
        print(f"  ⚠️  {fn}: {count} hinglish for {days} days")
    else:
        print(f"  ✅ {fn}: {count} hinglish summaries ({days} days)")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 20: Week summary blocks
# ══════════════════════════════════════════════════════════════════════════════
print("\n[20] WEEK SUMMARY BLOCKS")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    count = len(re.findall(r'class="week-summary"', c))
    if count == 0:
        print(f"  ⚠️  {fn}: No week-summary block")
        add(fn, "No week-summary block")
    else:
        print(f"  ✅ {fn}: {count} week-summary block(s)")

# ══════════════════════════════════════════════════════════════════════════════
# CHECK 21: Takeaway blocks per day
# ══════════════════════════════════════════════════════════════════════════════
print("\n[21] TAKEAWAY BLOCKS PER WEEK")
for w in range(1, 19):
    fn = f"week{w}.html"
    c = contents[fn]
    count = len(re.findall(r'class="takeaways"', c))
    days = len(re.findall(r'id="day-\d+"', c))
    if count < days:
        print(f"  ⚠️  {fn}: {count} takeaways for {days} days")
        add(fn, f"Fewer takeaway blocks ({count}) than days ({days})")
    else:
        print(f"  ✅ {fn}: {count} takeaways ({days} days)")

# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "="*80)
print("ISSUES SUMMARY BY FILE")
print("="*80)
for fn, msgs in sorted(issues.items()):
    print(f"\n{fn} ({len(msgs)} issues):")
    for m in msgs:
        print(f"  ❌ {m}")

total = sum(len(v) for v in issues.values())
print(f"\nTotal issues found: {total}")
