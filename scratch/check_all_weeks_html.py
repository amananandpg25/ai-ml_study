import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def check_file(w):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # Check for unclosed day-section tags specifically
    # Find all "<div class="day-section"" occurrences
    # and extract the first 200 chars of each to see if it closes with a ">" before the next "<div" or "</div" or "<section" or "<main"
    malformed_sections = []
    matches = list(re.finditer(r'<div\s+class="day-section"', content))
    for m in matches:
        start_idx = m.start()
        # Find next "<" after this one
        first_bracket = content.find('<', start_idx + 1)
        # Find next ">" after this one
        closing_bracket = content.find('>', start_idx)
        
        if closing_bracket == -1 or (first_bracket != -1 and first_bracket < closing_bracket):
            # The next tag starts before this tag closes!
            snippet = content[start_idx:start_idx+150].replace('\n', ' ')
            malformed_sections.append(snippet)
            
    if malformed_sections:
        print(f"  MALFORMED DAY-SECTION DECLS FOUND:")
        for ms in malformed_sections:
            print(f"    - {ms}")
            
    # Count div balances
    lines = content.splitlines()
    depth = 0
    in_style_or_script = False
    first_neg = None
    
    for line_num, line in enumerate(lines, 1):
        if '<script' in line or '<style' in line:
            in_style_or_script = True
        if '</script>' in line or '</style>' in line:
            in_style_or_script = False
            continue
        if in_style_or_script:
            continue
            
        tags = re.findall(r'</?div\b[^>]*>', line)
        for tag in tags:
            if tag.startswith('</'):
                depth -= 1
            else:
                depth += 1
            if depth < 0 and first_neg is None:
                first_neg = (line_num, line.strip())
                
    if first_neg:
        print(f"  First negative depth at line {first_neg[0]}: {first_neg[1]} (depth={depth})")
    print(f"  Final div depth = {depth}")

if __name__ == '__main__':
    for w in range(1, 19):
        print(f"\n--- week{w}.html ---")
        check_file(w)
