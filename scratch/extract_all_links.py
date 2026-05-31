import os
import re
from bs4 import BeautifulSoup

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
output_file = "/Users/amananand/Downloads/SDE/ai:ml/scratch/extracted_links.txt"

all_links = []

for w in range(1, 19):
    fn = f"week{w}.html"
    path = os.path.join(base_dir, fn)
    if not os.path.exists(path):
        continue
    
    html = open(path, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    
    for a in soup.find_all('a'):
        href = a.get('href', '')
        if href.startswith('http'):
            text = a.get_text().strip()
            # Find parent day-section
            parent_day = "global"
            parent = a.find_parent(class_=re.compile(r'\bday-section\b'))
            if parent:
                parent_day = parent.get('id', 'unknown')
            all_links.append((w, parent_day, href, text))

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(f"Week\tDay\tURL\tText\n")
    for item in all_links:
        f.write(f"Week {item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\n")

print(f"Extracted {len(all_links)} links. Saved to {output_file}")
