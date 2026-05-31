import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def count_in_file(path, day, cls):
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        return
    content = open(path, 'r', encoding='utf-8').read()
    day_marker = f'id="day-{day}"'
    if day_marker not in content:
        day_marker = f"id='day-{day}'"
    parts = content.split(day_marker, 1)
    if len(parts) < 2:
        print(f"Day {day} not found in {path}")
        return
    body = parts[1]
    next_marker = f'id="day-{day+1}"'
    next_marker_alt = f"id='day-{day+1}'"
    end_idx = body.find(next_marker)
    if end_idx == -1:
        end_idx = body.find(next_marker_alt)
    if end_idx == -1:
        end_idx = body.find("</div><!-- /day-")
    if end_idx == -1:
        end_idx = len(body)
    day_body = body[:end_idx]
    
    matches = re.findall(rf'class=["\']{cls}["\']', day_body)
    print(f"File: {os.path.basename(path)} | Day {day} | Class {cls} | Count: {len(matches)}")

count_in_file(os.path.join(base_dir, "_backup_gemini", "week16.html"), 109, "misconception")
count_in_file(os.path.join(base_dir, "_backup_gemini", "week17.html"), 119, "misconception")
count_in_file(os.path.join(base_dir, "_backup_gemini", "week16.html"), 109, "takeaways")
count_in_file(os.path.join(base_dir, "_backup_gemini", "week17.html"), 119, "takeaways")
