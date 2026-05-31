import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
    content = open(path, 'r', encoding='utf-8').read()
    
    day_matches = re.findall(r'id=["\']day-(\d+)["\']', content)
    for d_str in day_matches:
        d = int(d_str)
        day_marker = f'id="day-{d}"'
        if day_marker not in content:
            day_marker = f"id='day-{d}'"
            
        parts = content.split(day_marker, 1)
        if len(parts) < 2:
            continue
            
        header_and_body = parts[1]
        next_day_marker = f'id="day-{d+1}"'
        next_day_marker_alt = f"id='day-{d+1}'"
        
        day_end_idx = header_and_body.find(next_day_marker)
        if day_end_idx == -1:
            day_end_idx = header_and_body.find(next_day_marker_alt)
        if day_end_idx == -1:
            day_end_idx = header_and_body.find("</div><!-- /day-")
        if day_end_idx == -1:
            day_end_idx = len(header_and_body)
            
        day_body = header_and_body[:day_end_idx]
        
        has_objectives = 'class="objectives"' in day_body or 'By end of today' in day_body or 'By end of Day' in day_body
        if not has_objectives:
            print(f"Week {w} Day {d} is missing objectives.")
