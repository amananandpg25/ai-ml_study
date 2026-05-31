with open('/Users/amananand/Downloads/SDE/ai:ml/week10.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect Day 70
day70_start = content.find('<div class="day-section" id="day-70">')
day71_start = content.find('<div class="day-section" id="day-71">')
day72_start = content.find('<div class="day-section" id="day-72">')
day73_start = content.find('<!-- ── FOOTER ── -->')
if day73_start == -1:
    day73_start = content.find('</main>')

if day70_start != -1 and day71_start != -1:
    print("=== Day 70 block length:", day71_start - day70_start)
    print(content[day70_start:day70_start+1500])

if day72_start != -1 and day73_start != -1:
    print("=== Day 72 block length:", day73_start - day72_start)
    print(content[day72_start:day72_start+1500])
