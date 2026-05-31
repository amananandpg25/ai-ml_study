import os
import re
from bs4 import BeautifulSoup

dir_path = "/Users/amananand/Downloads/SDE/ai:ml"
roadmap_path = os.path.join(dir_path, "roadmap.html")

print("Checking section tags and day ranges in the main body of roadmap.html...\n")

if os.path.exists(roadmap_path):
    with open(roadmap_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    # Standard actual ranges:
    actual_ranges = {
        1: "1-7",
        2: "8-14",
        3: "15-21",
        4: "22-30",
        5: "31-37",
        6: "38-44",
        7: "45-51",
        8: "52-58",
        9: "59-65",
        10: "66-72",
        11: "73-79",
        12: "80-86",
        13: "87-93",
        14: "94-100",
        15: "101-107",
        16: "108-117",
        17: "118-124",
        18: "125-135"
    }
    
    # Search for all elements with class section-tag
    tags = soup.find_all(class_='section-tag')
    for idx, t in enumerate(tags):
        text = t.text.strip()
        # Extract week number if possible from nearby headers, or map by index
        # Let's see: we can search up or down to find the nearest h2
        section = t.find_parent(class_='section')
        h2 = section.find('h2') if section else None
        h2_text = h2.text.strip() if h2 else "NO H2"
        print(f"Tag {idx:02d}: section-tag='{text}' | Header: {h2_text}")
        
        # Parse day range from tag text
        # e.g., "DAYS 118–124" (using en-dash or hyphen)
        m = re.search(r'(?:DAYS|Day|Days)\s*(\d+)[\u2013\u2014-](\d+)', text)
        if m:
            found_range = f"{m.group(1)}-{m.group(2)}"
            # Let's find which week this section corresponds to
            wm = re.search(r'Week\s*(\d+)', h2_text, re.IGNORECASE)
            if wm:
                w_num = int(wm.group(1))
                expected = actual_ranges.get(w_num, "")
                if found_range != expected:
                    print(f"  ❌ MISMATCH for Week {w_num}: Tag says {found_range}, actual is {expected}!")
                else:
                    print(f"  ✅ Match for Week {w_num}")
            else:
                print("  ⚠️ Could not parse week number from header")
        else:
            print("  ⚠️ No day range found in tag text")
else:
    print("roadmap.html does not exist!")
