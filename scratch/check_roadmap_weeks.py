import os
import re
from bs4 import BeautifulSoup

dir_path = "/Users/amananand/Downloads/SDE/ai:ml"
weeks = [f"week{i}.html" for i in range(1, 19)]

print("Auditing presence of 'Before You Start Checklist' across all days of all weeks:")
print("-" * 75)

for week_idx, week_file in enumerate(weeks, 1):
    path = os.path.join(dir_path, week_file)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    day_sections = soup.find_all(id=re.compile(r'^day-\d+$'))
    
    total_days = len(day_sections)
    checklist_days = 0
    days_missing = []
    
    for sec in day_sections:
        m = re.match(r'^day-(\d+)$', sec['id'])
        day_num = int(m.group(1)) if m else None
        
        # Check for callout with Before You Start Checklist
        callouts = sec.find_all(class_='callout')
        has_checklist = False
        for c in callouts:
            if "Before You Start Checklist" in c.text or "Before You Start" in c.text:
                has_checklist = True
                break
        if has_checklist:
            checklist_days += 1
        else:
            days_missing.append(day_num)
            
    print(f"=== {week_file} ===")
    print(f"  Total Days: {total_days} | Days with Checklist: {checklist_days} | Missing: {days_missing}")
    print()
