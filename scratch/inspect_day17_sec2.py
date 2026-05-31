with open('/Users/amananand/Downloads/SDE/ai:ml/week3.html', 'r', encoding='utf-8') as f:
    content = f.read()

day17_start = content.find('<div class="day-section" id="day-17">')
day18_start = content.find('<div class="day-section" id="day-18">')

if day17_start != -1 and day18_start != -1:
    day17_block = content[day17_start:day18_start]
    sec2_start = day17_block.find('<h3 class="sh3">2. StandardScaler (Z-score Normalization)</h3>')
    sec3_start = day17_block.find('<h3 class="sh3">3. Outlier Detection — IQR Method</h3>')
    if sec2_start != -1 and sec3_start != -1:
        print(day17_block[sec2_start:sec3_start])
    else:
        print("Could not find section 2 or 3 start")
else:
    print("Could not find Day 17 start/end")
