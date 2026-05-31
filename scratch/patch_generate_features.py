import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
target_file = os.path.join(base_dir, "scratch", "generate_missing_features.py")

if os.path.exists(target_file):
    content = open(target_file, 'r', encoding='utf-8').read()
    
    # 1. Update Prereqs check
    old_prereq = """        obj_idx = day_body.find("</ul>")
        if obj_idx != -1:
            day_body = day_body[:obj_idx+5] + prereq_html + day_body[obj_idx+5:]"""
            
    new_prereq = """        if 'Before You Start Checklist:' not in day_body:
            obj_idx = day_body.find("</ul>")
            if obj_idx != -1:
                day_body = day_body[:obj_idx+5] + prereq_html + day_body[obj_idx+5:]"""
                
    content = content.replace(old_prereq, new_prereq)
    
    # 2. Update Worked Example check
    old_worked = """            tak_idx = day_body.find('<div class="takeaways">')
            if tak_idx != -1:
                day_body = day_body[:tak_idx] + worked_html + day_body[tak_idx:]"""
                
    new_worked = """            if 'Hand-Calculated Worked Example:' not in day_body:
                tak_idx = day_body.find('<div class="takeaways">')
                if tak_idx != -1:
                    day_body = day_body[:tak_idx] + worked_html + day_body[tak_idx:]"""
                    
    content = content.replace(old_worked, new_worked)
    
    # 3. Update Misconception check
    old_miscon = """        if miscon:
            miscon_html = f\"\"\"
  <div class="misconception">
    <strong>⚠️ Common Misconception:</strong> {miscon.split('Fact:')[0].replace('Misconception:', '').strip()}
    <br><br>
    <strong>Fact:</strong> {miscon.split('Fact:')[1].strip() if 'Fact:' in miscon else miscon}
  </div>
\"\"\"
            tak_idx = day_body.find('<div class="takeaways">')
            if tak_idx != -1:
                day_body = day_body[:tak_idx] + miscon_html + day_body[tak_idx:]"""
                
    new_miscon = """        if miscon:
            miscon_html = f\"\"\"
  <div class="misconception">
    <strong>⚠️ Common Misconception:</strong> {miscon.split('Fact:')[0].replace('Misconception:', '').strip()}
    <br><br>
    <strong>Fact:</strong> {miscon.split('Fact:')[1].strip() if 'Fact:' in miscon else miscon}
  </div>
\"\"\"
            if 'class="misconception"' not in day_body:
                tak_idx = day_body.find('<div class="takeaways">')
                if tak_idx != -1:
                    day_body = day_body[:tak_idx] + miscon_html + day_body[tak_idx:]"""
                    
    content = content.replace(old_miscon, new_miscon)
    
    # 4. Update Spaced Repetition check
    old_spaced = """        if spaced_rep:
            spaced_html = f\"\"\"
  <div class="callout" style="background:rgba(108,140,255,.05);border-left:3px solid var(--blue);padding:.8rem 1.1rem;margin:1rem 0;font-size:13px;">
    <strong>💡 Spaced Repetition Reminder:</strong> {spaced_rep}
  </div>
\"\"\"
            tak_idx = day_body.find('<div class="takeaways">')
            if tak_idx != -1:
                day_body = day_body[:tak_idx] + spaced_html + day_body[tak_idx:]"""
                
    new_spaced = """        if spaced_rep:
            spaced_html = f\"\"\"
  <div class="callout" style="background:rgba(108,140,255,.05);border-left:3px solid var(--blue);padding:.8rem 1.1rem;margin:1rem 0;font-size:13px;">
    <strong>💡 Spaced Repetition Reminder:</strong> {spaced_rep}
  </div>
\"\"\"
            if 'Spaced Repetition Reminder:' not in day_body:
                tak_idx = day_body.find('<div class="takeaways">')
                if tak_idx != -1:
                    day_body = day_body[:tak_idx] + spaced_html + day_body[tak_idx:]"""
                    
    content = content.replace(old_spaced, new_spaced)
    
    # 5. Update ML Connection check
    old_mlconn = """        if ml_conn:
            ml_conn_html = f\"\"\"
  <div class="ml-connect">
    {ml_conn}
  </div>
\"\"\"
            tak_idx = day_body.find('<div class="takeaways">')
            if tak_idx != -1:
                day_body = day_body[:tak_idx] + ml_conn_html + day_body[tak_idx:]"""
                
    new_mlconn = """        if ml_conn:
            ml_conn_html = f\"\"\"
  <div class="ml-connect">
    {ml_conn}
  </div>
\"\"\"
            if 'class="ml-connect"' not in day_body:
                tak_idx = day_body.find('<div class="takeaways">')
                if tak_idx != -1:
                    day_body = day_body[:tak_idx] + ml_conn_html + day_body[tak_idx:]"""
                    
    content = content.replace(old_mlconn, new_mlconn)
    
    # 6. Update Hinglish Explanation check
    old_hinglish = """        if w >= 8:
            hinglish = DAY_DETAILS.get(d, {}).get("hinglish") or generate_hinglish(d, w, WEEK_TOPICS[w])
            hinglish_html = f\"\"\"
  <div class="hinglish">
    {hinglish}
  </div>
\"\"\"
            tak_list_idx = day_body.find('<ol>', day_body.find('<div class="takeaways">'))
            if tak_list_idx != -1:
                day_body = day_body[:tak_list_idx] + hinglish_html + day_body[tak_list_idx:]"""
                
    new_hinglish = """        if w >= 8:
            hinglish = DAY_DETAILS.get(d, {}).get("hinglish") or generate_hinglish(d, w, WEEK_TOPICS[w])
            hinglish_html = f\"\"\"
  <div class="hinglish">
    {hinglish}
  </div>
\"\"\"
            if 'class="hinglish"' not in day_body:
                tak_list_idx = day_body.find('<ol>', day_body.find('<div class="takeaways">'))
                if tak_list_idx != -1:
                    day_body = day_body[:tak_list_idx] + hinglish_html + day_body[tak_list_idx:]"""
                    
    content = content.replace(old_hinglish, new_hinglish)
    
    # 7. Update Flashcards check
    old_flashcards = """        if w >= 8:
            cards = DAY_DETAILS.get(d, {}).get("flashcards") or generate_flashcards(d, w, WEEK_TOPICS[w])
            cards_html = f\"\"\"
  <h2 class="sh2">🃏 Revision Flashcards — Day {d}</h2>
  <p class="flashcard-hint" style="font-size:10px; font-family:var(--font-mono); color:var(--muted); text-transform:uppercase; margin-bottom:8px;">CLICK EACH CARD TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[0][0]}</div>
        <div class="fc-back">{cards[0][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[1][0]}</div>
        <div class="fc-back">{cards[1][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[2][0]}</div>
        <div class="fc-back">{cards[2][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[3][0]}</div>
        <div class="fc-back">{cards[3][1]}</div>
      </div>
    </div>
  </div>
\"\"\"
            quiz_idx = day_body.find('</div>\\n  </div>', day_body.find('id="quiz-section"'))
            if quiz_idx == -1:
                quiz_idx = day_body.find('</div>\\n</div>', day_body.find('id="quiz-section"'))
            if quiz_idx != -1:
                day_body = day_body[:quiz_idx+7] + cards_html + day_body[quiz_idx+7:]"""
                
    new_flashcards = """        if w >= 8:
            cards = DAY_DETAILS.get(d, {}).get("flashcards") or generate_flashcards(d, w, WEEK_TOPICS[w])
            cards_html = f\"\"\"
  <h2 class="sh2">🃏 Revision Flashcards — Day {d}</h2>
  <p class="flashcard-hint" style="font-size:10px; font-family:var(--font-mono); color:var(--muted); text-transform:uppercase; margin-bottom:8px;">CLICK EACH CARD TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[0][0]}</div>
        <div class="fc-back">{cards[0][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[1][0]}</div>
        <div class="fc-back">{cards[1][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[2][0]}</div>
        <div class="fc-back">{cards[2][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[3][0]}</div>
        <div class="fc-back">{cards[3][1]}</div>
      </div>
    </div>
  </div>
\"\"\"
            if 'Revision Flashcards' not in day_body:
                quiz_idx = day_body.find('</div>\\n  </div>', day_body.find('id="quiz-section"'))
                if quiz_idx == -1:
                    quiz_idx = day_body.find('</div>\\n</div>', day_body.find('id="quiz-section"'))
                if quiz_idx != -1:
                    day_body = day_body[:quiz_idx+7] + cards_html + day_body[quiz_idx+7:]"""
                    
    content = content.replace(old_flashcards, new_flashcards)
    
    # 8. Update Predict Block check
    old_predict = """        if w >= 8:
            pred = DAY_DETAILS.get(d, {}).get("predict") or generate_predict(d, w)
            pred_html = f\"\"\"
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT</div>
    <pre style="font-family:var(--font-mono); font-size:12.5px; background:rgba(0,0,0,0.15); padding:0.8rem; border-radius:6px; margin-bottom:0.8rem;"><code>{pred['code']}</code></pre>
    <div style="display:flex;gap:.8rem;margin-top:.8rem">
      <input type="text" class="predict-input" id="day{d}-p1-input" placeholder="Your prediction..." aria-label="Enter prediction output">
      <button class="predict-btn" onclick="checkPredict('day{d}-p1', '{pred['ans']}')" style="background:var(--bg2); border:1px solid var(--border); color:var(--text); padding:4px 12px; border-radius:6px; cursor:pointer;">Check</button>
    </div>
    <div class="predict-result" id="day{d}-p1-result" style="display:none; margin-top:8px;"></div>
  </div>
\"\"\"
            tasks_idx = day_body.find('id="tasks-section"')
            if tasks_idx != -1:
                div_idx = day_body.rfind('<div', 0, tasks_idx)
                if div_idx != -1:
                    day_body = day_body[:div_idx] + pred_html + day_body[div_idx:]"""
                    
    new_predict = """        if w >= 8:
            pred = DAY_DETAILS.get(d, {}).get("predict") or generate_predict(d, w)
            pred_html = f\"\"\"
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT</div>
    <pre style="font-family:var(--font-mono); font-size:12.5px; background:rgba(0,0,0,0.15); padding:0.8rem; border-radius:6px; margin-bottom:0.8rem;"><code>{pred['code']}</code></pre>
    <div style="display:flex;gap:.8rem;margin-top:.8rem">
      <input type="text" class="predict-input" id="day{d}-p1-input" placeholder="Your prediction..." aria-label="Enter prediction output">
      <button class="predict-btn" onclick="checkPredict('day{d}-p1', '{pred['ans']}')" style="background:var(--bg2); border:1px solid var(--border); color:var(--text); padding:4px 12px; border-radius:6px; cursor:pointer;">Check</button>
    </div>
    <div class="predict-result" id="day{d}-p1-result" style="display:none; margin-top:8px;"></div>
  </div>
\"\"\"
            if 'class="predict-block"' not in day_body:
                tasks_idx = day_body.find('id="tasks-section"')
                if tasks_idx != -1:
                    div_idx = day_body.rfind('<div', 0, tasks_idx)
                    if div_idx != -1:
                        day_body = day_body[:div_idx] + pred_html + day_body[div_idx:]"""
                        
    content = content.replace(old_predict, new_predict)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Successfully patched generate_missing_features.py for idempotency!")
else:
    print("generate_missing_features.py not found")
