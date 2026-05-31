import os
import re
from bs4 import BeautifulSoup

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

missing_git_days = {}

for w in range(1, 19):
    fn = f"week{w}.html"
    path = os.path.join(base_dir, fn)
    if not os.path.exists(path):
        continue
    
    html = open(path, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    
    day_sections = soup.find_all(class_=re.compile(r'\bday-section\b'))
    for day_sec in day_sections:
        day_id = day_sec.get('id', 'unknown')
        if day_id == 'unknown' or 'toolkit' in day_id:
            continue
            
        git_blocks = day_sec.find_all(class_=re.compile(r'\bgit-block\b'))
        if not git_blocks:
            if w not in missing_git_days:
                missing_git_days[w] = []
            missing_git_days[w].append(day_id)

print("Days completely missing a git-block:")
for w, days in missing_git_days.items():
    print(f"Week {w}: {', '.join(days)}")
