import os
import re
import glob

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
report_path = os.path.join(base_dir, "scratch/remaining_weeks_audit_report.md")

issues = []

# List of paywalled or dead domains to flag
SUSPECT_DOMAINS = [
    ("towardsdatascience.com", "Towards Data Science (Paywalled)"),
    ("medium.com", "Medium (Paywalled)"),
    ("r2rt.com", "R2RT Blog (Dead Domain)"),
    ("analyticsvidhya.com", "Analytics Vidhya (Aggressive ads/popups, sometimes paywalled)")
]

for filepath in sorted(glob.glob(os.path.join(base_dir, "week*.html"))):
    filename = os.path.basename(filepath)
    week_num = int(filename.replace("week", "").replace(".html", ""))
    
    # Audit only Weeks 6-18
    if week_num < 6:
        continue
        
    content = open(filepath, "r", encoding="utf-8").read()
    
    # 1. State key checks
    state_key_matches = re.findall(r"localStorage\.getItem\(['\"]([^'\"]+)['\"]", content)
    week_state_keys = [k for k in state_key_matches if k.startswith('w') and ('state' in k or 'xp' in k or 'done' in k)]
    expected_key = f"w{week_num}-state"
    if expected_key not in week_state_keys and f"w{week_num}-state`" not in content and f"`w${{WEEK}}-state`" not in content:
        if f"w${{WEEK}}-state" not in content:
            issues.append({
                "week": week_num,
                "file": filename,
                "category": "State Key",
                "severity": "High",
                "description": f"Expected localStorage key '{expected_key}' or dynamic template literal not found in scripts."
            })
            
    # 2. Check for empty quiz feedback or placeholders
    # e.g., correct-fb with empty content or minimal content like "✅ Correct!" or "❌ Incorrect."
    quiz_feedbacks = re.findall(r'class="quiz-feedback [^"]+"[^>]*>(.*?)</div>', content)
    for fb in quiz_feedbacks:
        fb_clean = fb.strip().replace(" ", "").replace("&nbsp;", "")
        if fb_clean in ["✅Correct!", "❌Incorrect.", "✅Correct", "❌Incorrect", "Correct!", "Incorrect."]:
            issues.append({
                "week": week_num,
                "file": filename,
                "category": "Quiz Feedback",
                "severity": "Medium",
                "description": f"Found empty or minimally populated placeholder quiz feedback: '{fb.strip()}'"
            })
            
    # 3. Check for suspect/paywalled/dead domains in resources
    for domain, label in SUSPECT_DOMAINS:
        occurrences = re.findall(r'href=["\'](https?://(?:www\.)?' + re.escape(domain) + r'[^\s"\'<>]*)(?:["\'])', content)
        for url in occurrences:
            issues.append({
                "week": week_num,
                "file": filename,
                "category": f"Resource Link ({label})",
                "severity": "High" if "Dead" in label else "Medium",
                "description": f"Paywalled or dead resource link found: `{url}`. Recommend replacing with a free, open-access alternative."
            })
            
    # 4. Check for deprecated Pandas/sklearn patterns in code blocks
    if "inplace=True" in content or "inplace = True" in content:
        # Check if it is a pandas inplace or pytorch inplace
        # Print matching lines for context analysis
        lines = content.split("\n")
        for i, l in enumerate(lines):
            if "inplace=True" in l or "inplace = True" in l:
                # If it contains pd., df., or drop/fillna/rename/set_index/replace, it is likely pandas
                if any(k in l for k in ["df", "pd", "fillna", "drop", "rename", "set_index", "replace"]):
                    issues.append({
                        "week": week_num,
                        "file": filename,
                        "category": "Deprecated API (Pandas inplace)",
                        "severity": "Medium",
                        "description": f"Line {i+1} uses `inplace=True` in Pandas: `{l.strip()}`. Modern Pandas (2.0+) discourages inplace modifications. Prefer assignment instead."
                    })
                    
    # 5. Check for Seaborn distplot
    if "distplot" in content:
        lines = content.split("\n")
        for i, l in enumerate(lines):
            if "distplot" in l:
                issues.append({
                    "week": week_num,
                    "file": filename,
                    "category": "Deprecated API (Seaborn distplot)",
                    "severity": "Medium",
                    "description": f"Line {i+1} uses deprecated Seaborn method `distplot`: `{l.strip()}`. Replaced by `histplot` or `displot` in Seaborn 0.12+."
                })
                
    # 6. Check for missing flashcards or predict outputs where they should be
    # Let's count day sections
    day_ids = re.findall(r'id="day-(\d+)"', content)
    for day in day_ids:
        # Extract content for this specific day section
        day_pattern = r'id="day-' + day + r'".*?(?:id="day-' + str(int(day)+1) + r'"|<!-- /day-' + day + r'|$)'
        day_match = re.search(day_pattern, content, re.S)
        if day_match:
            day_text = day_match.group(0)
            
            # Check for flashcards
            if "flashcard" not in day_text and "flashcard-grid" not in day_text:
                # Standard days should have flashcards except maybe project days or capstones
                # Day 44, 51, 65, 72, 79, 86, 93, 100, 107, 117, 124, 135 are final/project days
                is_recap_day = int(day) % 7 == 0 or int(day) in [44, 51, 65, 72, 79, 86, 93, 100, 107, 117, 124, 135]
                if not is_recap_day:
                    # Ignore if the day has no theory (e.g. project days)
                    if "🧠 Theory" in day_text or "h2 class=\"sh2\"" in day_text:
                        issues.append({
                            "week": week_num,
                            "file": filename,
                            "category": "Missing Flashcards",
                            "severity": "Low",
                            "description": f"Day {day} has theory but is missing interactive revision flashcards."
                        })
            
            # Check for Predict the Output
            if "predict-block" not in day_text:
                is_recap_day = int(day) % 7 == 0 or int(day) in [44, 51, 65, 72, 79, 86, 93, 100, 107, 117, 124, 135]
                if not is_recap_day:
                    if "🧠 Theory" in day_text:
                        issues.append({
                            "week": week_num,
                            "file": filename,
                            "category": "Missing Predict-the-Output",
                            "severity": "Low",
                            "description": f"Day {day} has theory but is missing a Predict-the-Output block."
                        })

# Generate markdown report
md = "# Content Quality Audit Report (Weeks 6-18)\n"
md += "This report documents all content quality, pedagogical, and structural issues found in Weeks 6–18 (Days 38–135).\n\n"

# Split by severity
for severity in ["High", "Medium", "Low"]:
    sev_issues = [i for i in issues if i["severity"] == severity]
    md += f"## 🔴 {severity} Severity Issues ({len(sev_issues)})\n"
    if not sev_issues:
        md += "No issues found.\n\n"
        continue
    md += "| Week | File | Category | Description |\n"
    md += "| --- | --- | --- | --- |\n"
    for i in sorted(sev_issues, key=lambda x: (x["week"], x["category"])):
        desc = i["description"].replace("\n", " ")
        md += f"| Week {i['week']} | [{i['file']}](file://{os.path.join(base_dir, i['file'])}) | {i['category']} | {desc} |\n"
    md += "\n"

with open(report_path, "w", encoding="utf-8") as f:
    f.write(md)

print("🎉 Successfully generated remaining_weeks_audit_report.md!")
print(f"Total issues found: {len(issues)}")
