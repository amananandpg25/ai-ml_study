with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'r', encoding='utf-8') as f:
    content = f.read()

day88_start = content.find('id="day-88"')
day89_start = content.find('id="day-89"')
if day88_start != -1 and day89_start != -1:
    print(repr(content[day88_start:day89_start]))
else:
    print("Not found start/end for Day 88")
