with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'resources-section|Resources', content)]
print(f"Found {len(matches)} occurrences:")
for idx in matches:
    print("  - Context:", repr(content[idx-40:idx+120]))
