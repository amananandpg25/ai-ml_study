import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

print("=" * 80)
print("DEEP INCONSISTENCY AUDIT")
print("=" * 80)

# ── 1. Theme toggle button presence ──────────────────────────────────────────
print("\n[1] THEME TOGGLE BUTTON IN TOPNAV")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    # Check if theme-btn appears in the HTML (not just JS)
    # It should appear inside a nav or button tag
    html_theme_btn = re.search(r'<button[^>]+id=["\']theme-btn["\']', content)
    if not html_theme_btn:
        # Let's check if there's a toggleTheme button anywhere in HTML
        html_toggle = re.search(r'onclick=["\']toggleTheme\(\)["\']', content)
        if html_toggle:
            print(f"  week{w}: theme button exists (onclick toggleTheme) but no id='theme-btn'")
        else:
            print(f"  ❌ week{w}: NO theme toggle button in HTML at all!")
    else:
        print(f"  ✅ week{w}: Has id='theme-btn' button")

# ── 2. Brand labels match week number ─────────────────────────────────────────
print("\n[2] TOPNAV BRAND LABEL CONSISTENCY")
week_expected_brands = {
    1: "Week 1", 2: "Week 2", 3: "Week 3", 4: "Week 4",
    5: "Week 5", 6: "Week 6", 7: "Week 7", 8: "Week 8",
    9: "Week 9", 10: "Week 10", 11: "Week 11", 12: "Week 12",
    13: "Week 13", 14: "Week 14", 15: "Week 15", 16: "Week 16", 17: "Week 17"
}
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    brand_match = re.search(r'class="brand"[^>]*>(.*?)</div>', content, re.DOTALL)
    if brand_match:
        brand = brand_match.group(1).strip()
        expected = f"Week {w}"
        if expected not in brand:
            print(f"  ❌ week{w}: Brand says '{brand}' but should contain '{expected}'")
        else:
            print(f"  ✅ week{w}: Brand OK: {brand[:60]}")
    else:
        print(f"  ❌ week{w}: No .brand element found")

# ── 3. Day IDs consecutive and non-overlapping ────────────────────────────────
print("\n[3] DAY IDS CONSECUTIVE AND NON-OVERLAPPING")
all_day_ids = {}
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    day_ids = sorted(set(int(d) for d in re.findall(r'id="day-(\d+)"', content)))
    all_day_ids[w] = day_ids

# Check continuity
prev_max = 0
for w in range(1, 18):
    ids = all_day_ids[w]
    if not ids:
        print(f"  ❌ week{w}: No day sections found!")
        continue
    if ids[0] != prev_max + 1:
        print(f"  ❌ week{w}: Day IDs start at {ids[0]} but expected {prev_max + 1}")
    else:
        print(f"  ✅ week{w}: Days {ids[0]}-{ids[-1]} (count: {len(ids)})")
    prev_max = ids[-1]

# ── 4. Sidebar sb-items match day sections ────────────────────────────────────
print("\n[4] SIDEBAR SB-ITEMS vs DAY SECTIONS")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    sb_items = sorted(set(int(d) for d in re.findall(r'id="sb-(\d+)"', content)))
    day_ids = sorted(set(int(d) for d in re.findall(r'id="day-(\d+)"', content)))
    if sb_items != day_ids:
        print(f"  ❌ week{w}: Sidebar items {sb_items} != Day IDs {day_ids}")
    else:
        print(f"  ✅ week{w}: Sidebar matches days {day_ids}")

# ── 5. Day pills in topnav match day sections ─────────────────────────────────
print("\n[5] DAY PILLS vs DAY SECTIONS")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    pills = sorted(set(int(d) for d in re.findall(r'id="pill-(\d+)"', content)))
    day_ids = sorted(set(int(d) for d in re.findall(r'id="day-(\d+)"', content)))
    if pills != day_ids:
        print(f"  ❌ week{w}: Pills {pills} != Day IDs {day_ids}")
    else:
        print(f"  ✅ week{w}: Pills match days {day_ids}")

# ── 6. Complete buttons (XP) present for each day ────────────────────────────
print("\n[6] COMPLETE BUTTONS XP VALUES")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    xp_values = re.findall(r'completeDay\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)', content)
    day_ids = sorted(set(int(d) for d in re.findall(r'id="day-(\d+)"', content)))
    completed_days = sorted(set(int(d) for d, _ in xp_values))
    missing_btns = [d for d in day_ids if d not in completed_days]
    if missing_btns:
        print(f"  ❌ week{w}: Missing complete buttons for days: {missing_btns}")
    else:
        print(f"  ✅ week{w}: All {len(day_ids)} days have complete buttons")
    # Check XP values look sane
    for day, xp in xp_values:
        if int(xp) < 50 or int(xp) > 1000:
            print(f"     ⚠️  week{w} Day {day}: Suspicious XP={xp}")

# ── 7. Week nav links correct ─────────────────────────────────────────────────
print("\n[7] WEEK NAV LINKS")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    issues = []
    if w > 1:
        prev = f"week{w-1}.html"
        if prev not in content:
            issues.append(f"Missing prev link: {prev}")
    if w < 17:
        nxt = f"week{w+1}.html"
        if nxt not in content:
            issues.append(f"Missing next link: {nxt}")
    if "roadmap.html" not in content:
        issues.append("Missing roadmap.html link")
    if "dashboard.html" not in content:
        issues.append("Missing dashboard.html link")
    if issues:
        print(f"  ❌ week{w}: {', '.join(issues)}")
    else:
        print(f"  ✅ week{w}: Nav links OK")

# ── 8. Title tags ─────────────────────────────────────────────────────────────
print("\n[8] TITLE TAGS")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        print(f"  week{w}: '{title}'")
    else:
        print(f"  ❌ week{w}: No <title> tag!")

# ── 9. LEVELS array present ───────────────────────────────────────────────────
print("\n[9] LEVELS/GETLEVEL JS PRESENT")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    has_levels = "LEVELS" in content and "getLevel" in content
    if not has_levels:
        print(f"  ❌ week{w}: Missing LEVELS array or getLevel function")
    else:
        print(f"  ✅ week{w}: Has LEVELS/getLevel")

# ── 10. CSS: has dark mode variables ─────────────────────────────────────────
print("\n[10] CSS DARK MODE VARIABLES")
for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    content = open(path, "r", encoding="utf-8").read()
    has_dark = '[data-theme="light"]' in content or "data-theme" in content
    has_root = ':root' in content
    if not has_dark:
        print(f"  ❌ week{w}: Missing light mode CSS variables")
    elif not has_root:
        print(f"  ❌ week{w}: Missing :root CSS block")
    else:
        print(f"  ✅ week{w}: Has dark/light mode CSS")

print("\n" + "=" * 80)
print("AUDIT COMPLETE")
print("=" * 80)
