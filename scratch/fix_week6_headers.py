with open('/Users/amananand/Downloads/SDE/ai:ml/week6.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Day 40
day40_start = content.find('<div class="day-section" id="day-40">')
day41_start = content.find('<div class="day-section" id="day-41">')
if day40_start != -1 and day41_start != -1:
    day40_block = content[day40_start:day41_start]
    new_day40_block = day40_block.replace("Day 38", "Day 40")
    content = content.replace(day40_block, new_day40_block)
    print("Fixed Day 40 headers in week6.html")

# Fix Day 41
# Since we replaced day40_block, we should find the indices again in the updated content
day41_start = content.find('<div class="day-section" id="day-41">')
day42_start = content.find('<div class="day-section" id="day-42">')
if day41_start != -1 and day42_start != -1:
    day41_block = content[day41_start:day42_start]
    new_day41_block = day41_block.replace("Day 39", "Day 41")
    content = content.replace(day41_block, new_day41_block)
    print("Fixed Day 41 headers in week6.html")

# Fix Day 42
day42_start = content.find('<div class="day-section" id="day-42">')
day43_start = content.find('<div class="day-section" id="day-43">')
if day42_start != -1 and day43_start != -1:
    day42_block = content[day42_start:day43_start]
    new_day42_block = day42_block.replace("Day 40", "Day 42")
    content = content.replace(day42_block, new_day42_block)
    print("Fixed Day 42 headers in week6.html")

with open('/Users/amananand/Downloads/SDE/ai:ml/week6.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week6.html")
