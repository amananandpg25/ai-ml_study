with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'r', encoding='utf-8') as f:
    content = f.read()

days_res = ["Day 63 Resources — Transfer Learning", "Day 64 Resources — Data Augmentation", "Day 65 Resources — Vision Capstone"]
for dr in days_res:
    idx = content.find(dr)
    if idx != -1:
        print(f"=== {dr} ===")
        # Print up to next </div>\n</div> or similar
        print(content[idx:idx+1200])
    else:
        print(f"Not found {dr}")
