import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
files = [f"week{w}.html" for w in range(1, 18)] + ["roadmap.html", "dashboard.html", "resources.html"]

results = {}

for filename in files:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        results[filename] = {"error": "File not found"}
        continue
    content = open(path, "r", encoding="utf-8").read()
    info = {}

    # 1. Check for toggleSidebar function
    info["has_toggleSidebar"] = "function toggleSidebar()" in content
    info["has_closeSidebar"] = "function closeSidebar()" in content
    info["has_mob_menu_btn"] = 'class="mob-menu-btn"' in content

    # 2. Check for theme toggle
    info["has_toggleTheme"] = "function toggleTheme()" in content
    info["has_theme_btn"] = 'id="theme-btn"' in content

    # 3. Check for level badge
    info["has_level_badge"] = 'class="level-badge"' in content or 'id="level-show"' in content

    # 4. Check for favicon
    info["has_favicon"] = 'rel="icon"' in content

    # 5. Check for meta description
    info["has_meta_desc"] = 'name="description"' in content

    # 6. Navigation links (week nav)
    if filename.startswith("week"):
        w = int(filename.replace("week","").replace(".html",""))
        if w > 1:
            expected_prev = f"week{w-1}.html"
            info["prev_nav"] = expected_prev if expected_prev in content else f"MISSING: {expected_prev}"
        else:
            info["prev_nav"] = "N/A (first week)"
        if w < 17:
            expected_next = f"week{w+1}.html"
            info["next_nav"] = expected_next if expected_next in content else f"MISSING: {expected_next}"
        else:
            info["next_nav"] = "N/A (last week)"

    # 7. Check for week nav links section
    if filename.startswith("week"):
        info["has_week_nav_links"] = 'class="week-nav-links"' in content or 'week-nav-btn' in content

    # 8. Look for day sections
    if filename.startswith("week"):
        day_ids = re.findall(r'id="day-(\d+)"', content)
        info["day_ids"] = sorted(set(int(d) for d in day_ids))

    # 9. Check for ARIA attributes on sidebar toggle
    info["sidebar_aria"] = 'aria-expanded' in content and 'aria-label' in content

    # 10. Check for focus-visible CSS
    info["has_focus_visible"] = ":focus-visible" in content

    # 11. Check for dark mode CSS
    info["has_dark_mode_css"] = 'data-theme' in content

    results[filename] = info

# Print report
print("="*80)
print("COMPREHENSIVE CONSISTENCY AUDIT REPORT")
print("="*80)

for filename, info in results.items():
    if "error" in info:
        print(f"\n❌ {filename}: {info['error']}")
        continue
    issues = []

    if not info.get("has_toggleSidebar") and filename not in ["dashboard.html", "resources.html"]:
        issues.append("Missing toggleSidebar() function")
    if not info.get("has_closeSidebar") and filename not in ["dashboard.html", "resources.html"]:
        issues.append("Missing closeSidebar() function")
    if not info.get("has_mob_menu_btn") and filename not in ["dashboard.html", "resources.html"]:
        issues.append("Missing .mob-menu-btn element")
    if not info.get("has_toggleTheme"):
        issues.append("Missing toggleTheme() function")
    if not info.get("has_theme_btn"):
        issues.append("Missing #theme-btn element")
    if not info.get("has_level_badge") and filename.startswith("week"):
        issues.append("Missing level badge element")
    if not info.get("has_favicon"):
        issues.append("Missing favicon")
    if not info.get("has_meta_desc"):
        issues.append("Missing meta description")
    if filename.startswith("week"):
        if not info.get("has_week_nav_links"):
            issues.append("Missing week nav links")
        pnav = info.get("prev_nav", "")
        nnav = info.get("next_nav", "")
        if isinstance(pnav, str) and pnav.startswith("MISSING"):
            issues.append(f"Missing previous week link: {pnav}")
        if isinstance(nnav, str) and nnav.startswith("MISSING"):
            issues.append(f"Missing next week link: {nnav}")
    if not info.get("has_focus_visible"):
        issues.append("Missing :focus-visible CSS")
    if not info.get("has_dark_mode_css"):
        issues.append("Missing data-theme dark mode CSS")

    if issues:
        print(f"\n⚠️  {filename} ({len(issues)} issues):")
        for issue in issues:
            print(f"    ❌ {issue}")
        # Also show day ids for weeks
        if filename.startswith("week"):
            print(f"    📅 Day IDs found: {info.get('day_ids', [])}")
    else:
        print(f"\n✅ {filename}: All checks passed")
        if filename.startswith("week"):
            print(f"    📅 Day IDs found: {info.get('day_ids', [])}")

print("\n" + "="*80)
