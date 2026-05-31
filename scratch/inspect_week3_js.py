content = open("/Users/amananand/Downloads/SDE/ai:ml/week3.html", "r", encoding="utf-8").read()
import re
scripts = re.findall(r"<script>(.*?)</script>", content, re.DOTALL)
if scripts:
    print(scripts[-1])
else:
    print("No script tag found!")
