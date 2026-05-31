with open('/Users/amananand/Downloads/SDE/ai:ml/week8.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.findall(r'<div\s+[^>]*id="(day-52|day-53|day-54)"', content)
print("Found days in week8.html:", matches)

# Print headings in each day
days = ["day-52", "day-53", "day-54"]
for day in days:
    day_start = content.find(f'id="{day}"')
    if day_start != -1:
        # find next day or coding task
        day_end = content.find('id="day-', day_start + 10)
        if day_end == -1:
            day_end = content.find('<!--', day_start + 10)
        block = content[day_start:day_end]
        print(f"=== {day} ===")
        headings = re.findall(r'<h[23]\b[^>]*>.*?</h[23]>|<div class="mermaid">.*?</div>', block, re.DOTALL)
        for h in headings[:10]:
            print("  -", h.strip())
