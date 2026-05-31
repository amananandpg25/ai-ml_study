import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def fix_file(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # Let's write a regex to find the malformed tags and fix them.
    # The malformed pattern:
    # <div class="day-section" id="day-XXX"
    #   <div class="[CLASS]">...</div>
    # >
    # We want to replace it with:
    # <div class="day-section" id="day-XXX">
    #   <div class="[CLASS]">...</div>
    
    # We use re.DOTALL so that we can match across lines.
    # Let's match:
    # group 1: id="day-XXX" (or just the day number)
    # group 2: the whole content of the inner div (which starts with <div class="..." and ends with </div>)
    pattern = r'(<div class="day-section" id="day-\d+")\s*(\n\s*<div class="(?:analogy|misconception|ml-connect|callout)"[^>]*>.*?</div>)\s*\n\s*>'
    
    matches = list(re.finditer(pattern, content, re.DOTALL))
    if not matches:
        # Let's try matching a generic version if any file differs slightly
        # e.g., missing ID or different class
        pattern = r'(<div class="day-section"[^>]*?)\s*(\n\s*<div class="(?:analogy|misconception|ml-connect|callout)"[^>]*>.*?</div>)\s*\n\s*>'
        matches = list(re.finditer(pattern, content, re.DOTALL))
        
    if matches:
        print(f"week{w}.html: Found {len(matches)} malformed sections to fix.")
        new_content = content
        
        # We do replacement from end to start to avoid index shifting issues
        for m in reversed(matches):
            start = m.start()
            end = m.end()
            g1 = m.group(1)
            g2 = m.group(2)
            
            # The fixed replacement puts '>' at the end of the day-section tag
            replacement = f"{g1}>\n{g2.strip()}"
            
            new_content = new_content[:start] + replacement + new_content[end:]
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"week{w}.html: Applied fixes.")
    else:
        print(f"week{w}.html: No malformed sections found using regex.")

if __name__ == '__main__':
    for w in range(1, 18):
        fix_file(w)
