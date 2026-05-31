import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

for w in [9, 10, 11]:
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
        
        # Extract the objectives block
        obj_m = re.search(r'(<div class="objectives">.*?</div>)', day_body, re.DOTALL)
        if obj_m:
            obj_content = obj_m.group(1)
            # Count the number of bullet points (li tags)
            li_count = len(re.findall(r'<li>', obj_content))
            print(f"Week {w} Day {d} has objectives with {li_count} items.")
            # Print a snippet
            snippet = re.sub('<[^<]+?>', '', obj_content).strip().replace('\n', ' ')
            print(f"  Snippet: {snippet[:80]}...")
        else:
            print(f"Week {w} Day {d} has NO objectives block.")
