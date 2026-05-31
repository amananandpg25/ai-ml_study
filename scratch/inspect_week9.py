with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all occurrences of <div class="mermaid">...</div> in week9.html
import re
mermaid_blocks = re.findall(r'<div class="mermaid">.*?</div>', content, re.DOTALL)
print(f"Found {len(mermaid_blocks)} mermaid blocks in week9.html:")
for i, mb in enumerate(mermaid_blocks):
    print(f"--- Block {i} ---")
    print(mb[:200].strip())
