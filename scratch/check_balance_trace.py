import re

def trace_file(filepath):
    print(f"=== Tracing {filepath} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    depth = 0
    day_id = "header"
    
    for line_num, line in enumerate(lines, 1):
        # Update day_id if we encounter a day section
        day_match = re.search(r'id="day-([^"]+)"', line)
        if day_match and 'class="day-section' in line:
            print(f"  Day transition: {day_id} -> {day_match.group(1)} (depth before: {depth})")
            day_id = day_match.group(1)
        
        # Tokenize div tags in this line
        tags = re.findall(r'</?div\b[^>]*>', line)
        for tag in tags:
            if tag.startswith('</'):
                depth -= 1
            else:
                depth += 1
            if depth < 0:
                print(f"    WARNING: depth dropped to {depth} at line {line_num}: {repr(line.strip())}")

    print(f"  Final depth at end of file: {depth}")

import sys
if len(sys.argv) > 1:
    trace_file(sys.argv[1])
else:
    for f in ['week7.html', 'week10.html', 'week16.html']:
        trace_file(f)
