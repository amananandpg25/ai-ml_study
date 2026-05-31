import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def fix_file(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # We want to match:
    # 1. <div class="day-section" (followed by spaces and/or newlines)
    # 2. Any HTML content (non-greedily) that contains callouts, misconceptions, etc.
    # 3. id="day-[NUMBER]" (possibly followed by other things and closed with >)
    #
    # Regex structure:
    # <div class="day-section"\s*\n(.*?)\n\s*id="day-(\d+)"\s*>
    #
    # Wait, let's also support optional spacing/newlines before id="day-...":
    pattern = r'<div\s+class="day-section"\s*\n(.*?)\n\s*id="day-(\d+)"\s*>'
    
    matches = list(re.finditer(pattern, content, re.DOTALL))
    if matches:
        print(f"week{w}.html: Found {len(matches)} malformed sections to fix.")
        new_content = content
        for m in reversed(matches):
            start = m.start()
            end = m.end()
            nested_content = m.group(1)
            day_num = m.group(2)
            
            replacement = f'<div class="day-section" id="day-{day_num}">\n{nested_content}'
            new_content = new_content[:start] + replacement + new_content[end:]
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"week{w}.html: Applied fixes.")
    else:
        print(f"week{w}.html: No malformed sections found.")

if __name__ == '__main__':
    for w in range(1, 18):
        fix_file(w)
