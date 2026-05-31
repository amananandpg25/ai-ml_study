path = "/Users/amananand/Downloads/SDE/ai:ml/week6.html"
content = open(path, 'r', encoding='utf-8').read()

day_marker = 'id="day-44"'
parts = content.split(day_marker, 1)
header_and_body = parts[1]
day_end_idx = header_and_body.find('id="day-45"')
if day_end_idx == -1:
    day_end_idx = header_and_body.find("</div><!-- /day-")
day_body = header_and_body[:day_end_idx]

import re
matches = [m.start() for m in re.finditer('takeaways', day_body, re.IGNORECASE)]
print(f"Found {len(matches)} matches of 'takeaways' in Day 44 body:")
for idx in matches:
    print(f"Match at index {idx}:")
    print(day_body[max(0, idx-50):min(len(day_body), idx+50)])
    print("-" * 40)
