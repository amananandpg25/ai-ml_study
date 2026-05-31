import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
w16_path = os.path.join(base_dir, "_backup_gemini", "week16.html")

if os.path.exists(w16_path):
    content = open(w16_path, 'r', encoding='utf-8').read()
    idx = content.find('id="day-109"')
    next_idx = content.find('id="day-110"', idx)
    if idx != -1 and next_idx != -1:
        day_body = content[idx:next_idx]
        # Find first <div class="misconception">
        m_idx = 0
        while True:
            m_idx = day_body.find('<div class="misconception">', m_idx)
            if m_idx == -1:
                break
            m_end = day_body.find('</div>', m_idx)
            print("--- MISCONCEPTION BLOCK ---")
            print(day_body[m_idx:m_end+6])
            m_idx = m_end
    else:
        print("Day 109 not found")
else:
    print("Backup week16 not found")
