import os, re

base = "/Users/amananand/Downloads/SDE/ai:ml"

# Week summary template
def make_week_summary(w, topic, max_day):
    return f"""
<div class="week-summary">
  <div class="ws-icon">🎉</div>
  <div class="ws-content">
    <h3>Week {w} Complete — {topic}!</h3>
    <p>You've finished all {max_day - (max_day % 7 if max_day % 7 != 0 else 7) + 1} days of Week {w}. Your understanding of <strong>{topic}</strong> is now solid. Push everything to GitHub and take a rest day — you've earned it!</p>
    <div class="ws-checks">
      <span class="ws-check">✅ All days completed</span>
      <span class="ws-check">✅ Flashcards reviewed</span>
      <span class="ws-check">✅ Code pushed to GitHub</span>
    </div>
    <a href="roadmap.html" class="ws-btn">View Full Roadmap →</a>
  </div>
</div>"""

# CSS to add if not present
WEEK_SUMMARY_CSS = """
/* Week summary */
.week-summary{background:linear-gradient(135deg,rgba(79,209,165,0.08),rgba(108,140,255,0.08));border:1px solid var(--green);border-radius:14px;padding:2rem;margin:2.5rem 0;display:flex;gap:1.5rem;align-items:flex-start}
.ws-icon{font-size:2.5rem;flex-shrink:0}
.ws-content h3{color:var(--green);margin:0 0 .5rem}
.ws-content p{color:var(--muted);margin:0 0 1rem;line-height:1.6}
.ws-checks{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:1rem}
.ws-check{background:rgba(79,209,165,0.12);color:var(--green);padding:.2rem .7rem;border-radius:20px;font-size:.8rem}
.ws-btn{display:inline-block;background:var(--green);color:#0d1117;padding:.4rem 1.2rem;border-radius:8px;text-decoration:none;font-size:.85rem;font-weight:600;transition:opacity .2s}
.ws-btn:hover{opacity:.85}
"""

# Week topics (from brand labels)
week_topics = {
    5: "ML Fundamentals", 6: "Regression", 7: "Classification",
    8: "Neural Networks & Deep Learning", 9: "CNNs & Computer Vision",
    10: "RNNs & Sequential Data", 11: "GANs & PyTorch",
    12: "Attention & Image Captioning", 13: "Natural Language Processing",
    14: "Transformers & Attention", 15: "LLM Engineering",
    16: "Production AI Engineering", 17: "Deploy + Flask + Docker",
    18: "Capstone & Portfolio"
}

for w in range(5, 19):
    fn = f"week{w}.html"
    path = os.path.join(base, fn)
    c = open(path).read()

    if 'class="week-summary"' in c:
        print(f"  ⏭  {fn}: already has week-summary")
        continue

    # Add CSS if not present
    if '.week-summary{' not in c and '.week-summary {' not in c:
        # Insert CSS before </style>
        c = c.replace('</style>', WEEK_SUMMARY_CSS + '\n</style>', 1)

    # Find the last day's closing </div> just before </main> or </div><!-- layout -->
    # Strategy: insert the week-summary just before the final </div> that closes the layout
    # The layout div closes with </div>\n</div>\n  </main> or similar
    # Better: find the last occurrence of </section> or last </div> before <script>
    
    # Find all day IDs to get the last day
    day_ids = sorted(set(int(d) for d in re.findall(r'id="day-(\d+)"', c)))
    last_day = day_ids[-1] if day_ids else None

    if last_day is None:
        print(f"  ❌ {fn}: No day IDs found!")
        continue

    # Find the complete-btn for the last day (it marks the end of that day's content)
    # Pattern: completeDay(last_day, XP) ... then some closing divs
    # We want to insert AFTER the complete-btn div of the last day but BEFORE the layout closes
    
    # Strategy: find </main> and insert just before it
    if '</main>' in c:
        idx = c.rfind('</main>')
        topic = week_topics.get(w, "Advanced Topics")
        summary_html = make_week_summary(w, topic, last_day)
        c = c[:idx] + summary_html + '\n' + c[idx:]
        open(path, "w").write(c)
        print(f"  ✅ {fn}: Added week-summary before </main>")
    else:
        # Try inserting before </div><!-- /layout --> or closing div of layout
        # Find the line with <div class="layout">
        layout_match = re.search(r'<div class="layout">', c)
        if layout_match:
            # Find the last </div> before <script>
            script_idx = c.find('<script>')
            if script_idx == -1:
                script_idx = len(c)
            # Insert just before the <script>
            topic = week_topics.get(w, "Advanced Topics")
            summary_html = make_week_summary(w, topic, last_day)
            c = c[:script_idx] + summary_html + '\n' + c[script_idx:]
            open(path, "w").write(c)
            print(f"  ✅ {fn}: Added week-summary before <script> (no </main> found)")
        else:
            print(f"  ❌ {fn}: Could not find insertion point!")

print("\nDone!")
