with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
matches = [m.start() for m in re.finditer(r'<div class="mermaid">', content)]
print(f"Found {len(matches)} occurrences of mermaid blocks in restored week13.html:")
for i, idx in enumerate(matches):
    print(f"--- Block {i} ---")
    # print up to next </div>
    end_idx = content.find('</div>', idx)
    print(repr(content[idx:end_idx+6]))
