with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
days = ["day-88", "day-90", "day-91", "day-92", "day-93"]
for day in days:
    idx = content.find(f'id="{day}"')
    if idx != -1:
        print(f"=== {day} ===")
        block = content[idx:idx+2500]
        h3s = re.findall(r'<h3 class="sh3">.*?</h3>', block)
        for h in h3s[:2]:
            print("  -", h)
