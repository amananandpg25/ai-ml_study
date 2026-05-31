import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

for w in range(1, 18):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # Replace any class="takeaways"> that is NOT preceded by <div
    # We can use regex to find class="takeaways" and check if the preceding characters are "<div "
    # A simpler way is to replace it by looking for patterns like \nclass="takeaways"> or similar,
    # or use a regex with negative lookbehind.
    # Negative lookbehind: (?<!<div\s)class="takeaways"
    new_content, count = re.subn(r'(?<!<div\s)class="takeaways"', r'<div class="takeaways"', content)
    
    if count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {count} malformed takeaways divs in week{w}.html")
