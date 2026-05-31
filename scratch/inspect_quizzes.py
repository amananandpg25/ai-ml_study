import re
import collections
import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

def find_duplicate_ids(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        return
        
    content = open(path, 'r', encoding='utf-8').read()
    
    # Match id="something" or id='something'
    id_pattern = re.compile(r'\bid=["\']([a-zA-Z0-9_-]+)["\']')
    all_ids = id_pattern.findall(content)
    
    counts = collections.Counter(all_ids)
    duplicates = {k: v for k, v in counts.items() if v > 1}
    
    print(f"\n===== Duplicate HTML IDs in {filename} =====")
    if duplicates:
        for k, v in sorted(duplicates.items(), key=lambda x: -x[1]):
            print(f"ID '{k}' appears {v} times")
    else:
        print("✅ No duplicate HTML IDs found!")

find_duplicate_ids("week1.html")
find_duplicate_ids("week9.html")
