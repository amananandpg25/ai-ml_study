import os
import re
from bs4 import BeautifulSoup

dir_path = "/Users/amananand/Downloads/SDE/ai:ml"
dash_path = os.path.join(dir_path, "dashboard.html")

print("Checking week names and structure inside dashboard.html...\n")

if os.path.exists(dash_path):
    with open(dash_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check if there are cards or items corresponding to each week in dashboard
    # Let's search for text patterns or elements
    week_items = soup.find_all(class_=re.compile(r'week|card|row|item', re.I))
    
    # We can search for any element containing week names or labels
    # e.g., "Week 1", "Week 2", etc.
    elements = soup.find_all(text=re.compile(r'Week\s*\d+', re.I))
    for el in elements:
        parent = el.parent
        print(f"Parent tag: <{parent.name}> | Class: {parent.get('class')} | Text: '{el.strip()}'")
        
    print("\nSearch for references to week files in dashboard.html:")
    links = soup.find_all('a', href=re.compile(r'^week\d+\.html$'))
    for l in links:
        print(f"Link: href={l['href']} | Text: '{l.text.strip()}'")
else:
    print("dashboard.html does not exist!")
