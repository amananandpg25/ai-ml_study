import os
import re
from bs4 import BeautifulSoup

dir_path = "/Users/amananand/Downloads/SDE/ai:ml"
roadmap_path = os.path.join(dir_path, "roadmap.html")

print("Comparing week titles between week files and roadmap.html...\n")

if os.path.exists(roadmap_path):
    with open(roadmap_path, 'r', encoding='utf-8') as f:
        r_html = f.read()
    r_soup = BeautifulSoup(r_html, 'html.parser')
    
    # Map week numbers to roadmap.html h2 headers
    roadmap_titles = {}
    r_sections = r_soup.find_all(class_='section')
    for sec in r_sections:
        h2 = sec.find('h2')
        if h2:
            h2_text = h2.text.strip()
            # Extract week number
            m = re.search(r'Week\s*(\d+)', h2_text, re.IGNORECASE)
            if m:
                w_num = int(m.group(1))
                roadmap_titles[w_num] = h2_text
                
    for i in range(1, 19):
        w_file = f"week{i}.html"
        w_path = os.path.join(dir_path, w_file)
        if os.path.exists(w_path):
            with open(w_path, 'r', encoding='utf-8') as f:
                w_html = f.read()
            w_soup = BeautifulSoup(w_html, 'html.parser')
            
            # Get navbar brand title
            brand_div = w_soup.find(class_='brand')
            brand_text = brand_div.text.strip() if brand_div else "NO BRAND"
            
            # Get document title
            doc_title = w_soup.title.text.strip() if w_soup.title else "NO TITLE"
            
            # Compare with roadmap.html h2
            r_title = roadmap_titles.get(i, "NOT FOUND IN ROADMAP")
            
            # Clean them for comparison (remove "Week X — " prefix)
            clean_brand = re.sub(r'^Week\s*\d+\s*[\u2014-]\s*', '', brand_text, flags=re.IGNORECASE).strip()
            clean_roadmap = re.sub(r'^Week\s*\d+\s*[\u2014-]\s*', '', r_title, flags=re.IGNORECASE).strip()
            
            # Split off metadata if any
            clean_brand_cmp = clean_brand.split('|')[0].strip().lower()
            clean_roadmap_cmp = clean_roadmap.split('|')[0].strip().lower()
            
            # Normalize spaces
            clean_brand_cmp = re.sub(r'\s+', ' ', clean_brand_cmp)
            clean_roadmap_cmp = re.sub(r'\s+', ' ', clean_roadmap_cmp)
            
            if clean_brand_cmp != clean_roadmap_cmp:
                print(f"❌ INCONSISTENCY IN WEEK {i}:")
                print(f"  Navbar/File Title: '{brand_text}'")
                print(f"  Roadmap Header:    '{r_title}'")
            else:
                print(f"✅ Week {i} Titles Match: '{brand_text}'")
else:
    print("roadmap.html does not exist!")
