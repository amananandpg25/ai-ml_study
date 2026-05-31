import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
path = os.path.join(base_dir, "week9.html")
content = open(path, 'r', encoding='utf-8').read()

day_marker = 'id="day-59"'
parts = content.split(day_marker, 1)
header_and_body = parts[1]

day_end_idx = header_and_body.find('id="day-60"')
if day_end_idx == -1:
    day_end_idx = header_and_body.find("</div><!-- /day-")
day_body = header_and_body[:day_end_idx]

print("--- Day 59 Content ---")
print(day_body[:300])
print("...")
print(day_body[-600:])
