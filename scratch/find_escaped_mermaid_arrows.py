import os
import glob
import re

workspace_dir = "/Users/amananand/Downloads/SDE/ai:ml"
html_files = glob.glob(os.path.join(workspace_dir, "*.html"))

print("Auditing HTML files for escaped Mermaid arrow syntax...")

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find all divs or pre with class="mermaid"
    mermaid_blocks = re.findall(r'<div class=\"mermaid\">(.*?)</div>', content, re.DOTALL)
    mermaid_blocks_alt = re.findall(r'<pre class=\"mermaid\">(.*?)</pre>', content, re.DOTALL)
    blocks = mermaid_blocks + mermaid_blocks_alt
    
    if not blocks:
        continue
        
    escaped_found = False
    for idx, block in enumerate(blocks):
        if '--&gt;' in block or '&gt;' in block or '&amp;gt;' in block:
            escaped_found = True
            print(f"  [Found escaped arrow] Block {idx+1} in {filename} contains escaped arrows!")
            
            # Print a snippet of the block containing the escape
            lines = block.split('\n')
            for line in lines:
                if '&gt;' in line or '--&gt;' in line:
                    print(f"    Line: {line.strip()}")

print("Audit completed.")
