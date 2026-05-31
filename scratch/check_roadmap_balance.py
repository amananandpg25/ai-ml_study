import os
import re
from bs4 import BeautifulSoup

dir_path = "/Users/amananand/Downloads/SDE/ai:ml"
roadmap_path = os.path.join(dir_path, "roadmap.html")

print("Checking sidebar nav-items and week headers in roadmap.html...")

if os.path.exists(roadmap_path):
    with open(roadmap_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Sidebar items check
    nav_items = soup.find_all(class_='nav-item')
    print("\n=== Sidebar Navigation Items ===")
    for idx, item in enumerate(nav_items):
        href = item.get('href', '')
        # Only show week items
        if 'week' in href:
            dr = item.find(class_='day-range')
            dr_text = dr.text.strip() if dr else "NO DAY RANGE"
            # Get the name of the week
            name_span = item.find(class_='week-name')
            name_text = name_span.text.strip() if name_span else "NO NAME"
            print(f"Index {idx:02d}: href={href} | day-range={dr_text:8} | name={name_text}")
            
    # 2. Main content week cards check
    # Let's search for divs or elements that correspond to each week's main section
    # e.g., <div class="section" id="week-1"> or similar
    print("\n=== Main Content Week Sections ===")
    sections = soup.find_all(class_='section')
    for sec in sections:
        sec_id = sec.get('id', '')
        if sec_id.startswith('week-'):
            h2 = sec.find('h2')
            h2_text = h2.text.strip() if h2 else "NO H2"
            print(f"Section ID: {sec_id:10} | Header: {h2_text}")
else:
    print("roadmap.html does not exist!")
