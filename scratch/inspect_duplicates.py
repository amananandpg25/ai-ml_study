import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def inspect_day(w, d, cls):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        return
    content = open(path, 'r', encoding='utf-8').read()
    
    # Extract day block
    day_marker = f'id="day-{d}"'
    if day_marker not in content:
        day_marker = f"id='day-{d}'"
    parts = content.split(day_marker, 1)
    if len(parts) < 2:
        return
    body = parts[1]
    next_marker = f'id="day-{d+1}"'
    next_marker_alt = f"id='day-{d+1}'"
    end_idx = body.find(next_marker)
    if end_idx == -1:
        end_idx = body.find(next_marker_alt)
    if end_idx == -1:
        end_idx = body.find("</div><!-- /day-")
    if end_idx == -1:
        end_idx = len(body)
    day_body = body[:end_idx]
    
    # Find all elements of that class
    pattern = rf'<div\s+class=["\']{cls}["\'].*?>(.*?)</div>'
    matches = re.findall(pattern, day_body, re.DOTALL)
    print(f"\n=== Week {w} Day {d} Class '{cls}' Matches (Count: {len(matches)}) ===")
    for idx, m in enumerate(matches, 1):
        clean_text = re.sub(r'<[^>]+>', '', m).strip()
        print(f"  Match {idx}: {clean_text[:120]}...")

inspect_day(15, 101, 'analogy')
inspect_day(16, 109, 'misconception')
inspect_day(17, 119, 'misconception')
inspect_day(2, 11, 'misconception')
inspect_day(2, 8, 'analogy')
inspect_day(1, 1, 'hinglish')
inspect_day(1, 1, 'analogy')
