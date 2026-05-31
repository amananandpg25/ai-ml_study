import re

for w in [14, 15, 16, 17]:
    path = f"/Users/amananand/Downloads/SDE/ai:ml/week{w}.html"
    content = open(path, 'r', encoding='utf-8').read()
    
    pills = re.findall(r"id=\"pill-(\d+)\"", content)
    sections = re.findall(r"id=\"day-(\d+)\"", content)
    sb_items = re.findall(r"id=\"sb-(\d+)\"", content)
    
    print(f"=== week{w}.html ===")
    print("Pills:", pills)
    print("Sections:", sections)
    print("Sidebar items:", sb_items)
