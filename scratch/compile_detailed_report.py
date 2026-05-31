import json
import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
report_path = os.path.join(base_dir, "scratch/audit_report.json")

with open(report_path, 'r') as f:
    results = json.load(f)

md_lines = []
md_lines.append("# Content Quality Detailed Audit Report")
md_lines.append("This report lists all missing elements, anomalies, and structural findings across all 18 weeks and 135 days.\n")

md_lines.append("## 1. Missing elements per day")
md_lines.append("Below is the day-by-day analysis of missing structural elements (Quizzes, Flashcards, Tasks, Resources, Predict output blocks, Misconceptions, Hinglish, Mermaid diagrams).\n")

# Elements to track
elements_list = [
    ('has_code', 'Code Examples'),
    ('has_quiz', 'Quiz'),
    ('has_flashcards', 'Flashcards'),
    ('has_tasks', 'Tasks'),
    ('has_resources', 'Resources'),
    ('has_predict', 'Predict the Output'),
    ('has_misconception', 'Misconception'),
    ('has_hinglish', 'Hinglish Summary'),
    ('has_mermaid', 'Mermaid Diagram')
]

for w_str, data in results.items():
    w = int(w_str)
    md_lines.append(f"### Week {w} (week{w}.html)")
    
    table_headers = "| Day | Code | Quiz | Flashcards | Tasks | Resources | Predict | Misconception | Hinglish | Mermaid |"
    table_divider = "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"
    md_lines.append(table_headers)
    md_lines.append(table_divider)
    
    for day in data['days']:
        day_id = day['day_id']
        row_cols = [f"**{day_id}**"]
        for key, name in elements_list:
            if day[key]:
                val = "✅"
                if key == 'has_flashcards':
                    val = f"✅ ({day['flashcard_count']})"
                elif key == 'has_mermaid':
                    val = f"✅ ({day['mermaid_count']})"
            else:
                val = "❌"
            row_cols.append(val)
        md_lines.append("| " + " | ".join(row_cols) + " |")
    md_lines.append("")

md_lines.append("## 2. Potential Missing Imports in Code Blocks")
md_lines.append("Days where code blocks use library functions (e.g. `pd.`, `np.`, `plt.`, `torch.`, `tf.`) but do not include their import statements:\n")
missing_imp_count = 0
for w_str, data in results.items():
    w = int(w_str)
    for day in data['days']:
        if day['missing_imports']:
            md_lines.append(f"- **Week {w}, Day {day['day_id']}**: Potential missing imports: {', '.join(day['missing_imports'])}")
            missing_imp_count += 1
if missing_imp_count == 0:
    md_lines.append("- ✅ No missing imports detected in code blocks across the curriculum.")
md_lines.append("")

md_lines.append("## 3. XP Value Consistency Check")
md_lines.append("Checking XP values awarded for completing days. In general, milestones/capstones should have higher XP (e.g. 250-500 XP) and standard days should have lower XP (e.g. 150 XP).\n")

table_xp = "| Week | Day-by-Day XP Values |"
table_xp_div = "| --- | --- |"
md_lines.append(table_xp)
md_lines.append(table_xp_div)
for w_str, data in results.items():
    w = int(w_str)
    xps = [str(d['xp_value']) if d['xp_value'] is not None else 'None' for d in data['days']]
    md_lines.append(f"| Week {w} | {', '.join(xps)} |")
md_lines.append("")

md_lines.append("## 4. Suggested Git Commit Message Consistency")
md_lines.append("Checking whether days include suggested Git commit messages and their style format.\n")
missing_commits_all = []
for w_str, data in results.items():
    w = int(w_str)
    missing_commits = [d['day_id'] for d in data['days'] if not d['commit_msg']]
    if missing_commits:
        missing_commits_all.append(f"Week {w}: {', '.join(missing_commits)}")
if missing_commits_all:
    md_lines.append("### Days missing git commit suggestions:")
    for line in missing_commits_all:
        md_lines.append(f"- {line}")
else:
    md_lines.append("- ✅ All days have suggested git commit messages.")
md_lines.append("")

md_lines.append("## 5. External Link Analysis")
md_lines.append("All unique domains referenced in external resources:\n")
distinct_domains = set()
for w_str, data in results.items():
    for link in data['links']:
        from urllib.parse import urlparse
        domain = urlparse(link['url']).netloc
        distinct_domains.add(domain)

for d in sorted(list(distinct_domains)):
    md_lines.append(f"- `{d}`")

with open(os.path.join(base_dir, "scratch/detailed_audit_data.md"), "w", encoding='utf-8') as f:
    f.write("\n".join(md_lines))
print("Saved detailed report to scratch/detailed_audit_data.md")
