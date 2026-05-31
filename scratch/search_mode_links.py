with open('/Users/amananand/Downloads/SDE/ai:ml/week2.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'mode\.com', content)]
print(f"Found {len(matches)} occurrences of mode.com in week2.html:")
for idx in matches:
    # print 50 chars before and after
    print("  - Context:", repr(content[max(0, idx-50):min(len(content), idx+100)]))
