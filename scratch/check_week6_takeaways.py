import re

content = open("/Users/amananand/Downloads/SDE/ai:ml/week6.html", "r", encoding="utf-8").read()

# Let's search for all takeaways in week6.html
takeaways = re.findall(r"<h3>(.*?)Takeaways</h3>", content, re.IGNORECASE)
print("Takeaways found in week6.html:")
for t in takeaways:
    print("  ", t.strip())

# Let's check where they are located
matches = re.finditer(r"<div class=\"day-section(.*?)\".*?<h3>(.*?)Takeaways</h3>", content, re.DOTALL)
# Actually, let's just find the day section wrapper first, and see what takeaways are in each day section.
day_sections = re.findall(r"<div class=\"day-section\" id=\"day-(\d+)\">.*?<h3>(.*?Takeaways)</h3>", content, re.DOTALL)
print("\nDay sections and takeaways:")
for day, tak in day_sections:
    print(f"  Day {day} section has takeaway: {tak.strip()}")
