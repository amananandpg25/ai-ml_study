with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'r', encoding='utf-8') as f:
    content = f.read()

day60_start = content.find('<div class="day-section" id="day-60">')
day61_start = content.find('<div class="day-section" id="day-61">')

if day60_start != -1 and day61_start != -1:
    day60_block = content[day60_start:day61_start]
    idx = day60_block.find('<div class="mermaid">')
    if idx != -1:
        print(repr(day60_block[idx:idx+400]))
    else:
        print("Mermaid not found in Day 60 block")
else:
    print("Day 60 start/end not found")
