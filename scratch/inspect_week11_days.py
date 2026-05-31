with open('/Users/amananand/Downloads/SDE/ai:ml/week11.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
days = ["day-73", "day-74", "day-75", "day-76", "day-77", "day-78", "day-79"]
for i in range(len(days)):
    start_tag = f'<div class="day-section" id="{days[i]}">' if i > 0 else f'<div class="day-section active" id="{days[i]}">'
    end_tag = f'<div class="day-section" id="{days[i+1]}">' if i < len(days)-1 else '<!-- ── FOOTER ── -->'
    
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)
    
    if start_idx != -1 and end_idx != -1:
        block = content[start_idx:end_idx]
        print(f"=== {days[i]} ===")
        # Print mermaid blocks in this day block
        mb = re.findall(r'<div class="mermaid">.*?</div>', block, re.DOTALL)
        for m in mb:
            print("  Mermaid:", m[:150].replace('\n', ' '))
        # Check for LangChain/Pinecone
        lc = re.findall(r'langchain|pinecone', block)
        if lc:
            print("  Contains LangChain/Pinecone links:", lc)
    else:
        print(f"Could not find start/end for {days[i]}")
