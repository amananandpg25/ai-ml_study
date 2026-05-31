with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = re.findall(r'<div\s+[^>]*id="([^"]+)"', content)
print("IDs found in week5.html:", matches)

day_sections = re.findall(r'<div\s+[^>]*class="[^"]*day-section[^"]*"[^>]*>', content)
print("Day sections in week5.html:")
for ds in day_sections:
    print("  -", ds)
