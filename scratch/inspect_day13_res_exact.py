with open('/Users/amananand/Downloads/SDE/ai:ml/week2.html', 'r', encoding='utf-8') as f:
    content = f.read()

day13_start = content.find('<div class="day-section" id="day-13">')
day14_start = content.find('<div class="day-section" id="day-14">')

if day13_start != -1 and day14_start != -1:
    day13_block = content[day13_start:day14_start]
    # Find all occurrences of '<div class="resources-grid">' in day13_block
    idx = day13_block.find('<div class="resources-grid">')
    if idx != -1:
        print("Found resources-grid at index:", idx)
        # Print up to next </section> or </div>
        print(day13_block[idx:idx+1500])
    else:
        print("resources-grid not found in Day 13 block.")
else:
    print("Day 13 start/end not found.")
