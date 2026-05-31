with open('/Users/amananand/Downloads/SDE/ai:ml/week5.html', 'r', encoding='utf-8') as f:
    content = f.read()

day33_start = content.find('<div class="day-section" id="day-33">')
day34_start = content.find('<div class="day-section" id="day-34">')

if day33_start != -1 and day34_start != -1:
    day33_block = content[day33_start:day34_start]
    idx = day33_block.find('<h2 class="sh2">🧠 Theory</h2>')
    if idx != -1:
        print(day33_block[idx:idx+1500])
else:
    print("Could not find Day 33 start/end")
