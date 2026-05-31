import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
path = os.path.join(base_dir, "week5.html")
content = open(path, 'r', encoding='utf-8').read()

day_marker = 'id="day-37"'
parts = content.split(day_marker, 1)
header_and_body = parts[1]

# Find next day or end of file
day_end_idx = header_and_body.find('id="day-38"')
if day_end_idx == -1:
    day_end_idx = header_and_body.find("</div><!-- /day-")
day_body = header_and_body[:day_end_idx]

print("--- Day 37 Content ---")
print("Length of day_body:", len(day_body))
print("Last 800 chars of day_body:")
print(day_body[-800:])
