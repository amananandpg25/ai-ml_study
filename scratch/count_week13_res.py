with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'id="resources-section"', content)]
print(f"Found {len(matches)} occurrences of id='resources-section' in week13.html:")
for idx in matches:
    print("  - At index:", idx)
    print("  - Context:", repr(content[idx:idx+300]))
