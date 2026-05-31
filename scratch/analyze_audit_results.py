import json
import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
report_path = os.path.join(base_dir, "scratch/audit_report.json")

with open(report_path, 'r') as f:
    results = json.load(f)

# Let's check consistency across days
print("================================================================================")
print("MISSING ELEMENTS PER DAY BY WEEK")
print("================================================================================")

for w_str, data in results.items():
    w = int(w_str)
    print(f"\nWeek {w} (week{w}.html):")
    for d_idx, day in enumerate(data['days']):
        day_id = day['day_id']
        missing = []
        if not day['has_code']:
            missing.append('Code Examples')
        if not day['has_quiz']:
            missing.append('Quiz')
        if not day['has_flashcards']:
            # Wait, are flashcards supposed to be in all weeks? Let's check.
            # The audit report says: "Flashcards completely absent in weeks 15, 16, 17", but let's check what the script found.
            missing.append(f"Flashcards ({day['flashcard_count']})")
        if not day['has_tasks']:
            missing.append('Tasks')
        if not day['has_resources']:
            missing.append('Resources')
        if not day['has_predict']:
            missing.append('Predict the Output')
        if not day['has_misconception']:
            missing.append('Misconception')
        if not day['has_hinglish']:
            missing.append('Hinglish Summary')
        if not day['has_mermaid']:
            missing.append('Mermaid Diagram')
            
        if missing:
            print(f"  Day {day_id}: Missing {', '.join(missing)}")
            
print("\n================================================================================")
print("CODE IMPORT ANALYSES")
print("================================================================================")
for w_str, data in results.items():
    w = int(w_str)
    for day in data['days']:
        if day['missing_imports']:
            print(f"Week {w}, Day {day['day_id']}: Code has potential missing imports: {day['missing_imports']}")

print("\n================================================================================")
print("XP CONSISTENCY BY WEEK")
print("================================================================================")
for w_str, data in results.items():
    w = int(w_str)
    xps = [d['xp_value'] for d in data['days'] if d['xp_value'] is not None]
    distinct_xps = set(xps)
    print(f"Week {w}: Distinct XP values: {distinct_xps} | Raw list: {xps}")

print("\n================================================================================")
print("GIT COMMIT SUGGESTIONS")
print("================================================================================")
for w_str, data in results.items():
    w = int(w_str)
    missing_commits = []
    commits = []
    for day in data['days']:
        if not day['commit_msg']:
            missing_commits.append(day['day_id'])
        else:
            commits.append(day['commit_msg'])
    if missing_commits:
        print(f"Week {w}: Missing Suggested Git Commit messages for: {missing_commits}")
    if commits:
        # Check a sample commit message format
        print(f"Week {w} sample commit: '{commits[0]}'")

print("\n================================================================================")
print("EXTERNAL LINK ANALYSIS")
print("================================================================================")
distinct_domains = set()
suspicious_links = []
for w_str, data in results.items():
    w = int(w_str)
    for link in data['links']:
        url = link['url']
        # parse domain
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
        distinct_domains.add(domain)
        # Check if suspicious (e.g. localhost, placeholders, empty paths, etc.)
        if 'TODO' in url or 'placeholder' in url or 'localhost' in url or '127.0.0.1' in url:
            suspicious_links.append((w, link['day'], url))

print(f"Found {len(distinct_domains)} distinct domains: {sorted(list(distinct_domains))}")
if suspicious_links:
    print(f"⚠️ Found suspicious links: {suspicious_links}")
else:
    print("✅ No placeholder or suspicious links found!")
