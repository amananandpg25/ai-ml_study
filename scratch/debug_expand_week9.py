import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
path = os.path.join(base_dir, "week9.html")
content = open(path, 'r', encoding='utf-8').read()

d = 59
day_marker = f'id="day-{d}"'
parts = content.split(day_marker, 1)
if len(parts) < 2:
    print("Day marker not found")
else:
    header_and_body = parts[1]
    next_day_marker = f'id="day-{d+1}"'
    day_end_idx = header_and_body.find(next_day_marker)
    print(f"day_end_idx: {day_end_idx}")
    day_body = header_and_body[:day_end_idx]
    
    print(f"Is 'class=\"takeaways\"' in day_body? {'class=\"takeaways\"' in day_body}")
    
    quiz_pos = day_body.find('id="quiz-section"')
    print(f"quiz_pos: {quiz_pos}")
    
    if quiz_pos == -1:
        quiz_pos = day_body.find('class="quiz-block"')
        print(f"quiz_pos (quiz-block): {quiz_pos}")
    if quiz_pos == -1:
        quiz_pos = day_body.find('Knowledge Check')
        print(f"quiz_pos (Knowledge Check): {quiz_pos}")
        
    takeaways_html = "<!-- TEST TAKEAWAYS -->"
    if quiz_pos != -1:
        div_pos = day_body.rfind('<div', 0, quiz_pos)
        print(f"div_pos: {div_pos}")
        if div_pos != -1:
            new_day_body = day_body[:div_pos] + takeaways_html + day_body[div_pos:]
            print("Successfully inserted at div_pos")
        else:
            new_day_body = day_body[:quiz_pos] + takeaways_html + day_body[quiz_pos:]
            print("Successfully inserted at quiz_pos")
    else:
        new_day_body = day_body + takeaways_html
        print("Successfully appended")
        
    print(f"Length diff: {len(new_day_body) - len(day_body)}")
