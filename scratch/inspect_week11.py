with open('/Users/amananand/Downloads/SDE/ai:ml/week11.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
# Find all mermaid blocks
mermaid_blocks = re.findall(r'<div class="mermaid">.*?</div>', content, re.DOTALL)
print(f"Found {len(mermaid_blocks)} mermaid blocks in week11.html:")
for i, mb in enumerate(mermaid_blocks):
    print(f"--- Block {i} ---")
    print(mb[:200].strip())

# Find any langchain or pinecone links
links = re.findall(r'href="[^"]*langchain[^"]*"|href="[^"]*pinecone[^"]*"', content)
print("Found LangChain/Pinecone links:", links)
