import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

WEEKS_DAYS = {
    1: [1, 2, 3, 4, 5, 6, 7],
    2: [8, 9, 10, 11, 12, 13, 14],
    3: [15, 16, 17, 18, 19, 20, 21],
    4: [22, 23, 24, 25, 26, 27, 28, 29, 30]
}

def calibrate_weeks():
    for w in range(1, 5):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        print(f"\nProcessing week{w}.html...")
        content = open(path, 'r', encoding='utf-8').read()
        
        days = WEEKS_DAYS[w]
        for d in days:
            day_marker = f'id="day-{d}"'
            if day_marker not in content:
                day_marker = f"id='day-{d}'"
                if day_marker not in content:
                    continue
                    
            parts = content.split(day_marker, 1)
            if len(parts) < 2:
                continue
                
            header_and_body = parts[1]
            next_day_marker = f'id="day-{d+1}"'
            next_day_marker_alt = f"id='day-{d+1}'"
            
            day_end_idx = header_and_body.find(next_day_marker)
            if day_end_idx == -1:
                day_end_idx = header_and_body.find(next_day_marker_alt)
            if day_end_idx == -1:
                day_end_idx = header_and_body.find("</div><!-- /day-")
            if day_end_idx == -1:
                day_end_idx = len(header_and_body)
                
            day_body = header_and_body[:day_end_idx]
            remainder = header_and_body[day_end_idx:]
            
            # 1. INJECT GLOBAL DIFFICULTY LEGEND
            tasks_hdr_idx = day_body.find('id="tasks-section"')
            if tasks_hdr_idx != -1 and 'Global Task Difficulty Scale' not in day_body:
                legend_html = """
  <div class="callout" style="background:rgba(255,255,255,.02);border:1px solid var(--border);padding:0.8rem;margin:1rem 0;font-size:12px;border-radius:8px;">
    <strong>💡 Global Task Difficulty Scale:</strong>
    <span style="margin-left:10px;color:var(--green)">🟢 EASY (15-30 min)</span> | 
    <span style="margin-left:10px;color:var(--orange)">🟡 MEDIUM (45-75 min)</span> | 
    <span style="margin-left:10px;color:var(--pink)">🔴 HARD (90-180 min)</span>
  </div>
"""
                hdr_close_div = day_body.find('</div>', tasks_hdr_idx)
                if hdr_close_div != -1:
                    day_body = day_body[:hdr_close_div+6] + legend_html + day_body[hdr_close_div+6:]
            
            # 2. STANDARDISE INDIVIDUAL TASK TIMES
            def repl_task_time(m):
                badge_content = m.group(1)
                time_span = m.group(2)
                
                new_time = "⏱ 30 min" # Default
                if 'tb-easy' in badge_content or 'EASY' in badge_content or '🟢' in badge_content:
                    new_time = "⏱ 25 min"
                elif 'tb-med' in badge_content or 'MEDIUM' in badge_content or '🟡' in badge_content:
                    new_time = "⏱ 45 min"
                elif 'tb-hard' in badge_content or 'HARD' in badge_content or '🔴' in badge_content:
                    new_time = "⏱ 90 min"
                elif 'tb-proj' in badge_content or 'tb-challenge' in badge_content or 'PROJ' in badge_content or 'CHALLENGE' in badge_content or 'PORTFOLIO' in badge_content or '🔵' in badge_content:
                    new_time = "⏱ 3 hours"
                
                return f'{badge_content}\n        <span class="task-time">{new_time}</span>'
            
            day_body = re.sub(
                r'(<span class="task-badge\s+[^"]+">.*?</span>\s*<span class="task-title">.*?</span>)\s*(<span class="task-time">.*?</span>)',
                repl_task_time,
                day_body,
                flags=re.DOTALL
            )
            
            content = parts[0] + day_marker + day_body + remainder
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Finished modifying week{w}.html!")

if __name__ == '__main__':
    calibrate_weeks()
    print("Calibration of Weeks 1-4 completed!")
