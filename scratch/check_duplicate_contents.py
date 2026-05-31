import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
    content = open(path, 'r', encoding='utf-8').read()
    
    # Extract days
    day_matches = re.findall(r'id=["\']day-(\d+)["\']', content)
    for d_str in day_matches:
        d = int(d_str)
        # Find day section start
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
        
        # Check for duplicates of specific classes
        for tag in ['analogy', 'hinglish', 'misconception', 'predict-block']:
            # Find all matched blocks
            pattern = rf'<div\s+class=["\']{tag}["\']>(.*?)</div>'
            if tag == 'predict-block':
                # Predict blocks are multiline and complex
                pattern = r'(<div\s+class=["\']predict-block["\'].*?</div>\s*</div>)'
            
            matches = re.findall(pattern, day_body, re.DOTALL)
            if len(matches) > 1:
                # Compare the contents
                unique_matches = set(m.strip() for m in matches)
                print(f"Week {w} Day {d} tag {tag}: matches={len(matches)}, unique={len(unique_matches)}")
                if len(unique_matches) < len(matches):
                    print("  -> Identical duplicate(s) found!")
                else:
                    print("  -> WARNING: Non-identical duplicate(s)!")
                    for idx, m in enumerate(unique_matches):
                        print(f"    [{idx}]: {m[:100]}...")
