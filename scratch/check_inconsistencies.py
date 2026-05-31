import os
import re
from bs4 import BeautifulSoup

dir_path = "/Users/amananand/Downloads/SDE/ai:ml"
weeks = [f"week{i}.html" for i in range(1, 19)]

print("Scanning weeks 1-18 for configuration, key definitions, and content inconsistencies...\n")

for week_file in weeks:
    path = os.path.join(dir_path, week_file)
    if not os.path.exists(path):
        print(f"⚠️ {week_file} does not exist!")
        continue
        
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Day Range and ID checks
    day_sections = soup.find_all(id=re.compile(r'^day-\d+$'))
    day_numbers = []
    for sec in day_sections:
        m = re.match(r'^day-(\d+)$', sec['id'])
        if m:
            day_numbers.append(int(m.group(1)))
            
    # 2. WEEK constant definition
    week_const_match = re.search(r'(?:const|let|var)\s+WEEK\s*=\s*(\d+)', html)
    week_const = int(week_const_match.group(1)) if week_const_match else None
    
    # 3. DAYS array definition
    days_array_match = re.search(r'(?:const|let|var)\s+DAYS\s*=\s*\[([^\]]+)\]', html)
    days_array = [int(x.strip()) for x in days_array_match.group(1).split(',')] if days_array_match else []
    
    # 4. XP values audit
    complete_btns = re.findall(r'completeDay\(\s*[^,]+,\s*(\d+)\s*\)', html)
    xp_values = sorted(list(set(int(x) for x in complete_btns))) if complete_btns else []
    
    # 5. Sidebar next/prev links check
    prev_link = None
    next_link = None
    sidebar = soup.find(class_='sidebar')
    if sidebar:
        links = sidebar.find_all('a')
        for l in links:
            href = l.get('href', '')
            if href.startswith('week'):
                # Check if it contains arrow or label
                text = l.text.lower()
                if '←' in text or 'prev' in text or 'back' in text:
                    prev_link = href
                elif '→' in text or 'next' in text:
                    next_link = href
                elif not prev_link and not next_link:
                    # Generic heuristic
                    if 'week' in href:
                        # Parse the number
                        m = re.search(r'week(\d+)\.html', href)
                        if m:
                            num = int(m.group(1))
                            # Compare with this file's week number
                            this_week_num = int(re.search(r'week(\d+)\.html', week_file).group(1))
                            if num < this_week_num:
                                prev_link = href
                            elif num > this_week_num:
                                next_link = href

    # 6. Check meta description
    meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
    meta_desc = meta_desc_tag.get('content', '') if meta_desc_tag else None

    # 7. Check levels array consistency (first and last elements)
    levels_match = re.search(r'const\s+LEVELS\s*=\s*\[(.*?)\];', html, re.DOTALL)
    levels_count = len(re.findall(r'label\s*:', levels_match.group(1))) if levels_match else 0
    
    # 8. Check document class topnav title
    brand_div = soup.find(class_='brand')
    brand_text = brand_div.text.strip() if brand_div else "NO BRAND"
    
    # 9. Verify if there are missing/placeholder files or references
    todo_count = len(re.findall(r'TODO|PLACEHOLDER|FIXME', html, re.IGNORECASE))
    
    print(f"=== {week_file} ===")
    print(f"  Brand Title: {brand_text}")
    print(f"  Days list: {day_numbers}")
    print(f"  WEEK constant: {week_const} (Expected: {re.search(r'week(\d+)\.html', week_file).group(1)})")
    print(f"  DAYS array: {days_array}")
    print(f"  XP Values: {xp_values}")
    print(f"  Prev Week Link: {prev_link} | Next Week Link: {next_link}")
    print(f"  Levels count: {levels_count} | TODO count: {todo_count}")
    print(f"  Meta Desc: {meta_desc}")
    print()
