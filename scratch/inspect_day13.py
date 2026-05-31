with open('/Users/amananand/Downloads/SDE/ai:ml/week2.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<div class="day-section" id="day-13">')
end_idx = content.find('<div class="day-section" id="day-14">')

if start_idx != -1 and end_idx != -1:
    day_13_block = content[start_idx:end_idx]
    import re
    res_cards = re.findall(r'<a class="res-card[^>]*href="([^"]+)"[^>]*>.*?<span class="res-title">([^<]+)</span>', day_13_block, re.DOTALL)
    print("Resource cards in Day 13:")
    for href, title in res_cards:
        print(f"  - {title.strip()} ({href})")
else:
    print("Could not find Day 13 block.")
