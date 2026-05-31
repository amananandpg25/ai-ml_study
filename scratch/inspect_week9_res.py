with open('/Users/amananand/Downloads/SDE/ai:ml/week9.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect resources section in day-63, day-64, day-65
import re
days = ["day-63", "day-64", "day-65"]
for i in range(len(days)):
    day_id = days[i]
    start_tag = f'<div class="day-section" id="{day_id}">'
    # Let's find the day section index
    day_start = content.find(start_tag)
    if day_start != -1:
        day_end = content.find('id="day-', day_start + 10)
        if day_end == -1:
            day_end = content.find('</main>')
        block = content[day_start:day_end]
        print(f"=== {day_id} ===")
        # Print the resources section
        res_idx = block.find('id="resources-section"')
        if res_idx != -1:
            print(block[res_idx:res_idx+1200])
        else:
            print("No resources-section found")
