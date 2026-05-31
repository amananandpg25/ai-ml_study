content = open("/Users/amananand/Downloads/SDE/ai:ml/week3.html", "r", encoding="utf-8").read()
import re
topnav = re.findall(r"<div class=\"topnav\">.*?</div>", content, re.DOTALL)
if topnav:
    print(topnav[0])
else:
    print("No topnav found!")
