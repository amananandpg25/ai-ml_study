with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'r', encoding='utf-8') as f:
    content = f.read()

day34_start = content.find('<div class="day-section" id="day-34">')
day35_start = content.find('<div class="day-section" id="day-35">')

if day34_start != -1 and day35_start != -1:
    day34_block = content[day34_start:day35_start]
    idx = day34_block.find('<h2 class="sh2">🧠 Theory</h2>')
    if idx != -1:
        print(day34_block[idx:idx+1500])
else:
    print("Could not find Day 34 start/end")
