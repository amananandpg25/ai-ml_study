with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'class="resources-grid"', content)]
print(f"Found {len(matches)} occurrences of 'class=\"resources-grid\"' in week13.html:")
for i, idx in enumerate(matches):
    print(f"--- {i} ---")
    print(repr(content[idx-100:idx+300]))
