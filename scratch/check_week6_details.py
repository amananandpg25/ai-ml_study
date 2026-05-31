import re

content = open("/Users/amananand/Downloads/SDE/ai:ml/week6.html", "r", encoding="utf-8").read()

day_sections = re.findall(r"<div class=\"day-section[^\"]*\" id=\"day-(\d+)\">", content)
print("Day section IDs:", day_sections)

# Find all <h3>⭐ Day ... Key Takeaways</h3> in the file
takeaway_headers = re.findall(r"<h3>⭐ Day (\d+) Key Takeaways</h3>", content)
print("Takeaway headers for Days:", takeaway_headers)

# Let's see if we can find any other takeaway headers
all_tak = re.findall(r"<h3>⭐ (.*?)</h3>", content)
print("All ⭐ headers:")
for h in all_tak:
    print("  ", h)
