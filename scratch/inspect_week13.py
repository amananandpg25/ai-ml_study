with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
mermaid_blocks = re.findall(r'<div class="mermaid">.*?</div>', content, re.DOTALL)
print(f"Found {len(mermaid_blocks)} mermaid blocks in week13.html:")
for i, mb in enumerate(mermaid_blocks):
    print(f"--- Block {i} ---")
    print(mb[:200].strip())
