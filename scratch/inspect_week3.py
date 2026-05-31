import re

content = open("/Users/amananand/Downloads/SDE/ai:ml/week3.html", "r", encoding="utf-8").read()

print("=== HEAD ===")
head = re.findall(r"<head>.*?</style>", content, re.DOTALL)
if head:
    print(head[0][:600])
    print("...")
    print(head[0][-600:])

print("\n=== TOPNAV ===")
topnav = re.findall(r"<div class=\"topnav\">.*?</div>", content, re.DOTALL)
if topnav:
    print(topnav[0])

print("\n=== WEEK NAV LINKS IN SIDEBAR ===")
aside = re.findall(r"<aside.*?</aside>", content, re.DOTALL)
if aside:
    nav_links = re.findall(r"<div class=\"week-nav-links\">.*?</div>", aside[0], re.DOTALL)
    if nav_links:
        print(nav_links[0])
    else:
        print("No week-nav-links in aside!")

print("\n=== SCRIPT END ===")
script = re.findall(r"<script>.*?</script>", content, re.DOTALL)
if script:
    print("Script length:", len(script[-1]))
    # print last 1000 chars of script
    print(script[-1][-2500:])
