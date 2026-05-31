import re

content = open("/Users/amananand/Downloads/SDE/ai:ml/week6.html", "r", encoding="utf-8").read()

# Let's split content by day sections
sections = re.split(r"<div class=\"day-section[^\"]*\" id=\"day-", content)
print("Number of split sections:", len(sections))

for i in range(1, len(sections)):
    sec_content = sections[i]
    # get first line or day number
    day_num = sec_content.split('"', 1)[0]
    # find all <h3>⭐ ... Key Takeaways</h3> inside this section
    t_headers = re.findall(r"<h3>⭐ (.*?)</h3>", sec_content)
    print(f"Section day-{day_num}:")
    for th in t_headers:
        print(f"  - {th}")
