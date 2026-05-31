with open('/Users/amananand/Downloads/SDE/ai:ml/week10.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'r2rt\.com', content)]
print(f"Found {len(matches)} occurrences of r2rt.com:")
for idx in matches:
    print("  - Context:", repr(content[max(0, idx-50):min(len(content), idx+150)]))
