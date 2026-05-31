content = open("/Users/amananand/Downloads/SDE/ai:ml/week7.html").read()
import re
# Find all occurrences of the word 'Day' followed by any digits
matches = re.finditer(r"Day\s*(\d+)", content, re.IGNORECASE)
days_found = set()
for m in matches:
    days_found.add(m.group(0))
print("Days found in week7.html:", sorted(list(days_found)))

# Find if there is any 'Day 43' or '43' in week7
matches_43 = re.finditer(r"43", content)
print("Count of '43' in week7.html:", len(list(matches_43)))
