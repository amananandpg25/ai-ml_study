import os
import re
from bs4 import BeautifulSoup

dir_path = "/Users/amananand/Downloads/SDE/ai:ml"
weeks = [f"week{i}.html" for i in range(1, 19)]

print("Auditing deviations from standard 3-tier XP system (+150, +200, +300):")
print("-" * 75)

total_days = 0
standard_count = 0
non_standard_count = 0

# Week days configuration: which day numbers are capstones?
# Capstone is normally the last day of the week
capstone_days = {
    1: 7,
    2: 14,
    3: 21,
    4: 30,
    5: 37,
    6: 44,
    7: 51,
    8: 58,
    9: 65,
    10: 72,
    11: 79,
    12: 86,
    13: 93,
    14: 100,
    15: 107,
    16: 117,
    17: 124,
    18: 135
}

for week_idx, week_file in enumerate(weeks, 1):
    path = os.path.join(dir_path, week_file)
    if not os.path.exists(path):
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    buttons = soup.find_all(class_='complete-btn')
    
    for btn in buttons:
        onclick = btn.get('onclick', '')
        m = re.search(r'completeDay\(\s*(\d+)\s*,\s*(\d+)\s*\)', onclick)
        if m:
            day_num = int(m.group(1))
            xp_val = int(m.group(2))
            total_days += 1
            
            is_capstone = (day_num == capstone_days.get(week_idx))
            
            # Check standard rule
            if is_capstone:
                # Capstone should be 300 XP
                if xp_val != 300:
                    print(f"❌ NON-STANDARD CAPSTONE: Week {week_idx:02d} Day {day_num:03d} Capstone has +{xp_val} XP (Expected: +300)")
                    non_standard_count += 1
                else:
                    standard_count += 1
            else:
                # Non-capstone should be 150 or 200 XP
                if xp_val not in [150, 200]:
                    print(f"❌ NON-STANDARD DAY: Week {week_idx:02d} Day {day_num:03d} has +{xp_val} XP (Expected: +150 or +200)")
                    non_standard_count += 1
                else:
                    standard_count += 1
        else:
            print(f"⚠️ Mismatched complete button on {week_file}: onclick='{onclick}'")

print("-" * 75)
print(f"Total days audited: {total_days}")
print(f"Standard days (+150/+200/+300 cap): {standard_count}")
print(f"Non-standard days: {non_standard_count}")
