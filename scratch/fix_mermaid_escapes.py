import os
import glob
import re

workspace_dir = "/Users/amananand/Downloads/SDE/ai:ml"
html_files = glob.glob(os.path.join(workspace_dir, "*.html"))

print("Running Mermaid HTML Entity Fixer...")

def fix_entities_in_mermaid_blocks(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_block(match):
        tag_open = match.group(1)   # e.g., <div class="mermaid">
        block_content = match.group(2)
        tag_close = match.group(3)  # e.g., </div>
        
        # Replace HTML entities with raw characters
        fixed_content = block_content
        fixed_content = fixed_content.replace('&gt;', '>')
        fixed_content = fixed_content.replace('&lt;', '<')
        fixed_content = fixed_content.replace('&amp;', '&')
        
        return f"{tag_open}{fixed_content}{tag_close}"

    # Target both <div class="mermaid"> and <pre class="mermaid">
    pattern = re.compile(r'(<div class="mermaid">)(.*?)(</div>)', re.DOTALL)
    new_content, count1 = pattern.subn(replace_block, content)
    
    pattern_alt = re.compile(r'(<pre class="mermaid">)(.*?)(</pre>)', re.DOTALL)
    new_content, count2 = pattern_alt.subn(replace_block, new_content)
    
    total_replaced = count1 + count2
    if total_replaced > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Fixed {total_replaced} Mermaid block(s) in {filename}")
        return True
    return False

if __name__ == "__main__":
    fixed_files = 0
    for filepath in sorted(html_files):
        if fix_entities_in_mermaid_blocks(filepath):
            fixed_files += 1
            
    print(f"\nCompleted! Fixed entities in {fixed_files} files.")
