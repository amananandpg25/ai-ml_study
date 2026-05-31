import re
import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# Bug 2 check (week7.html)
w7_path = os.path.join(base_dir, "week7.html")
if os.path.exists(w7_path):
    w7_content = open(w7_path, 'r', encoding='utf-8').read()
    day43_refs = re.findall(r"Day\s+43", w7_content, re.IGNORECASE)
    print("Week 7 'Day 43' references count:", len(day43_refs))
    # print context of first Day 43 ref
    match = re.search(r"Day\s+43", w7_content, re.IGNORECASE)
    if match:
        print("Context:", w7_content[match.start()-100:match.start()+100])

# Bug 3 check (week10.html)
w10_path = os.path.join(base_dir, "week10.html")
if os.path.exists(w10_path):
    w10_content = open(w10_path, 'r', encoding='utf-8').read()
    toolkits = re.findall(r"id=\"day-toolkit\"", w10_content)
    print("Week 10 duplicate 'day-toolkit' count:", len(toolkits))
    week9_tags = re.findall(r"WEEK\s+9", w10_content, re.IGNORECASE)
    print("Week 10 'WEEK 9' tags count:", len(week9_tags))

# Bug 4 check (week6.html)
w6_path = os.path.join(base_dir, "week6.html")
if os.path.exists(w6_path):
    w6_content = open(w6_path, 'r', encoding='utf-8').read()
    print("Week 6 'Day 38 Key Takeaways' references:")
    for m in re.finditer(r"Day\s+38\s+Key\s+Takeaways", w6_content, re.IGNORECASE):
        print("  Found at index:", m.start(), "context:", w6_content[m.start()-50:m.start()+100])

# Bug 5 check (week14.html)
w14_path = os.path.join(base_dir, "week14.html")
if os.path.exists(w14_path):
    w14_content = open(w14_path, 'r', encoding='utf-8').read()
    tab_seqs = re.findall(r"\\[tT]ext", w14_content)
    print("Week 14 '\\text' patterns count:", len(tab_seqs))
    # print raw text near a \t or similar corruption
    # wait, tab character might be an actual tab character in a string like \text where \t got turned into tab
    corrupted = re.findall(r"\\\t", w14_content)
    print("Week 14 corrupted '\\t' count:", len(corrupted))

# Bug 6 check (week13.html, week14.html)
for w in [13, 14]:
    w_path = os.path.join(base_dir, f"week{w}.html")
    if os.path.exists(w_path):
        w_content = open(w_path, 'r', encoding='utf-8').read()
        res_grid = re.findall(r"resource-grid", w_content)
        resources_grid = re.findall(r"resources-grid", w_content)
        print(f"Week {w}: 'resource-grid' count: {len(res_grid)}, 'resources-grid' count: {len(resources_grid)}")
