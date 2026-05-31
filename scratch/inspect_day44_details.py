path = "/Users/amananand/Downloads/SDE/ai:ml/week6.html"
content = open(path, 'r', encoding='utf-8').read()

day_marker = 'id="day-44"'
parts = content.split(day_marker, 1)
header_and_body = parts[1]
day_end_idx = header_and_body.find('id="day-45"')
if day_end_idx == -1:
    day_end_idx = header_and_body.find("</div><!-- /day-")
day_body = header_and_body[:day_end_idx]

idx = day_body.find('class="takeaways"')
print("Takeaways block content:")
print(day_body[idx:idx+500])
