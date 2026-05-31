path = "/Users/amananand/Downloads/SDE/ai:ml/week9.html"
content = open(path, 'r', encoding='utf-8').read()

import re
matches = [m.start() for m in re.finditer('takeaways', content, re.IGNORECASE)]
print(f"Found {len(matches)} matches of 'takeaways' in the file:")
for idx in matches:
    print(f"Match at index {idx}:")
    print(content[max(0, idx-50):min(len(content), idx+50)])
    print("-" * 40)
