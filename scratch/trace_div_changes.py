import re

def trace_file(filepath):
    print(f"=== Tracing {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    div_stack = []
    in_style_or_script = False
    
    for line_num, line in enumerate(lines, 1):
        if '<script' in line or '<style' in line:
            in_style_or_script = True
        if '</script>' in line or '</style>' in line:
            in_style_or_script = False
            continue
        if in_style_or_script:
            continue
            
        # We find divs, but we need to match them properly
        # Find all <div... and </div
        # Using a regex to find all start/end div tags
        tags = re.finditer(r'(</?div\b[^>]*>)', line)
        for match in tags:
            tag = match.group(1)
            if tag.startswith('</'):
                if div_stack:
                    open_tag, open_line = div_stack.pop()
                else:
                    print(f"    Extra close tag: {tag} at line {line_num}: {repr(line.strip())}")
            else:
                div_stack.append((tag, line_num))
                
    if div_stack:
        print("  Unclosed divs remaining in stack:")
        for tag, line in div_stack:
            print(f"    - Open tag {tag} at line {line}")
    else:
        print("  All divs matched.")

import sys
if len(sys.argv) > 1:
    trace_file(sys.argv[1])
