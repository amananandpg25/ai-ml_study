import os
import glob
import re

workspace_dir = "/Users/amananand/Downloads/SDE/ai:ml"
html_files = glob.glob(os.path.join(workspace_dir, "*.html"))

print(f"Found {len(html_files)} HTML files in root.")

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_mermaid_div = "class=\"mermaid\"" in content or "class='mermaid'" in content or "class=mermaid" in content
    has_mermaid_script = "mermaid.min.js" in content or "mermaid.esm" in content or "mermaid.js" in content
    has_mermaid_init = "mermaid.initialize" in content
    has_render_mermaid = "renderMermaid" in content
    
    if has_mermaid_div or has_mermaid_script or has_mermaid_init or has_render_mermaid:
        print(f"{filename}:")
        print(f"  has_mermaid_div: {has_mermaid_div}")
        print(f"  has_mermaid_script: {has_mermaid_script}")
        print(f"  has_mermaid_init: {has_mermaid_init}")
        print(f"  has_render_mermaid: {has_render_mermaid}")
        
        # Find script tag line
        script_matches = re.findall(r'<script[^>]*src="[^"]*mermaid[^"]*"[^>]*></script>', content)
        print(f"  Script tags: {script_matches}")
        
        # Find init logic
        init_match = re.search(r'mermaid\.initialize\([^)]*\);?', content)
        if init_match:
            print(f"  Init match: {init_match.group(0)}")
