with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

days_res = ["Day 90 Resources", "Day 91 Resources"]
for dr in days_res:
    idx = content.find(dr)
    if idx != -1:
        print(f"=== {dr} ===")
        print(content[idx:idx+1000])
    else:
        print(f"Not found {dr}")
