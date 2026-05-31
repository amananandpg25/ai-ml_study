import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

print("=" * 80)
print("CONTENT-LEVEL INCONSISTENCY AUDIT")
print("=" * 80)

# ── 1. State key names consistent ────────────────────────────────────────────
print("\n[1] STATE KEY NAMES (should be wN-state)")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    # Look for localStorage.getItem('wN-state')
    state_key = re.findall(r"localStorage\.getItem\(['\"]([^'\"]+)['\"]", content)
    week_state_keys = [k for k in state_key if k.startswith('w') and ('state' in k or 'xp' in k or 'done' in k)]
    correct_key = f"w{w}-state"
    if correct_key not in week_state_keys and f"w{w}-state`" not in content and f"`w${{WEEK}}-state`" not in content:
        # Check template literal
        if f"w${{WEEK}}-state" in content:
            print(f"  ✅ week{w}: Uses template literal w${{WEEK}}-state correctly")
        else:
            print(f"  ❌ week{w}: State key not found! Keys seen: {week_state_keys[:5]}")
    else:
        if correct_key in week_state_keys:
            print(f"  ✅ week{w}: Uses key '{correct_key}'")
        else:
            print(f"  ✅ week{w}: Uses template literal w${{WEEK}}-state")

# ── 2. DAYS array matches actual day IDs ─────────────────────────────────────
print("\n[2] DAYS ARRAY MATCHES ACTUAL DAY IDS")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    days_arr_match = re.search(r"const DAYS\s*=\s*\[([^\]]+)\]", content)
    day_sections = sorted(set(int(d) for d in re.findall(r'id="day-(\d+)"', content)))
    if days_arr_match:
        days_arr = [int(x.strip()) for x in days_arr_match.group(1).split(',')]
        if sorted(days_arr) != day_sections:
            print(f"  ❌ week{w}: DAYS array {days_arr} != Day sections {day_sections}")
        else:
            print(f"  ✅ week{w}: DAYS array matches sections: {days_arr}")
    else:
        print(f"  ❌ week{w}: No DAYS array found!")

# ── 3. Quiz blocks present ────────────────────────────────────────────────────
print("\n[3] QUIZ BLOCKS PER WEEK")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    quiz_blocks = len(re.findall(r'class="quiz-block"', content))
    quiz_opts = len(re.findall(r'class="quiz-opt"', content))
    days = len(re.findall(r'id="day-\d+"', content))
    if quiz_blocks == 0:
        print(f"  ❌ week{w}: No quiz blocks found! ({days} days)")
    elif quiz_blocks < days:
        print(f"  ⚠️  week{w}: Only {quiz_blocks} quiz blocks for {days} days")
    else:
        print(f"  ✅ week{w}: {quiz_blocks} quiz blocks / {quiz_opts} options ({days} days)")

# ── 4. Objectives boxes present ───────────────────────────────────────────────
print("\n[4] OBJECTIVES BLOCKS PER WEEK")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    objectives = len(re.findall(r'class="objectives"', content))
    days = len(re.findall(r'id="day-\d+"', content))
    if objectives == 0:
        print(f"  ❌ week{w}: No objectives blocks! ({days} days)")
    elif objectives < days:
        print(f"  ⚠️  week{w}: Only {objectives} objectives for {days} days")
    else:
        print(f"  ✅ week{w}: {objectives} objectives blocks ({days} days)")

# ── 5. Roadmap sidebar labels vs week file titles ─────────────────────────────
print("\n[5] ROADMAP SIDEBAR LABELS vs WEEK TITLES")
roadmap_path = os.path.join(base_dir, "roadmap.html")
roadmap_content = open(roadmap_path, "r", encoding="utf-8").read()
roadmap_nav_labels = re.findall(r'onclick="showSection\(\'[^\']+\',\s*this\)"\s*>\s*<span[^>]+></span>\s*(.*?)<span class="day-range"', roadmap_content, re.DOTALL)
cleaned_labels = [l.strip() for l in roadmap_nav_labels]
print(f"  Found {len(cleaned_labels)} nav labels in roadmap sidebar")
for i, label in enumerate(cleaned_labels):
    label_clean = re.sub(r'\s+', ' ', label).strip()
    print(f"  Week {i+1}: '{label_clean}'")

# ── 6. Check for broken links/references ─────────────────────────────────────
print("\n[6] INTERNAL LINK VALIDATION")
all_html_files = set(f"week{w}.html" for w in range(1, 18)) | {"roadmap.html", "dashboard.html", "resources.html"}
for filename in sorted(all_html_files):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        continue
    content = open(path, "r", encoding="utf-8").read()
    linked = re.findall(r'href="([^"#]+\.html)"', content)
    for lnk in linked:
        lnk_path = os.path.join(base_dir, lnk)
        if not os.path.exists(lnk_path):
            print(f"  ❌ {filename}: Broken link -> {lnk}")

print("  ✅ All links checked")

# ── 7. Flashcards present ─────────────────────────────────────────────────────
print("\n[7] FLASHCARDS PER WEEK")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    flashcards = len(re.findall(r'class="flashcard"', content))
    days = len(re.findall(r'id="day-\d+"', content))
    if flashcards == 0:
        print(f"  ❌ week{w}: No flashcards! ({days} days)")
    else:
        print(f"  ✅ week{w}: {flashcards} flashcards ({days} days)")

# ── 8. Theme button placement in weeks ───────────────────────────────────────
print("\n[8] THEME BUTTON PLACEMENT IN TOPNAV")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    # Look for toggleTheme in onclick within nav
    theme_in_html = re.search(r'<button[^>]*onclick=["\']toggleTheme\(\)["\'][^>]*>', content)
    if theme_in_html:
        btn = theme_in_html.group(0)
        has_id = 'id="theme-btn"' in btn or "id='theme-btn'" in btn
        print(f"  {'✅' if has_id else '⚠️ '} week{w}: Theme button found {'with id' if has_id else 'but MISSING id=theme-btn'}")
    else:
        print(f"  ❌ week{w}: No theme toggle button in HTML!")

print("\n" + "=" * 80)
print("CONTENT AUDIT COMPLETE")
print("=" * 80)
