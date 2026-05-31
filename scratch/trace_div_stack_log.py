import re
import sys

def trace_file(filepath):
    print(f"=== Logging pushes/pops for {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    stack = []
    in_style_or_script = False
    
    for line_num, line in enumerate(lines, 1):
        if '<script' in line or '<style' in line:
            in_style_or_script = True
        if '</script>' in line or '</style>' in line:
            in_style_or_script = False
            continue
        if in_style_or_script:
            continue
            
        tags = re.finditer(r'(</?div\b[^>]*>)', line)
        for m in tags:
            tag = m.group(1)
            if tag.startswith('</'):
                if stack:
                    op_tag, op_line = stack.pop()
                    # If we just popped a day-section or layout or main tag, print it!
                    if 'class="day-section"' in op_tag or 'class="layout"' in op_tag or 'class="main"' in op_tag:
                        print(f"  Line {line_num}: Popped structural tag {op_tag} (from line {op_line}) early!")
                else:
                    print(f"  Line {line_num}: EXTRA CLOSE {tag}!")
            else:
                stack.append((tag, line_num))

if __name__ == '__main__':
    trace_file('week4.html')
