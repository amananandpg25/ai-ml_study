base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
import re

content = open(f"{base_dir}/week1.html", "r").read()
scripts = re.findall(r"<script[^>]*>(.*?)</script>", content, re.DOTALL)
script_text = scripts[-1]

lines = script_text.splitlines()
for i in range(330, 375):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}")
