import os, re

base = "/Users/amananand/Downloads/SDE/ai:ml"

# ── Fix 1: week1.html title v2 ─────────────────────────────────────────────
w1 = os.path.join(base, "week1.html")
c = open(w1).read()
old_title = 'Week 1 — Python Foundations v2 | 135-Day AI/ML Roadmap'
new_title = 'Week 1 — Python Foundations | 135-Day AI/ML Roadmap'
if old_title in c:
    c = c.replace(old_title, new_title)
    open(w1, "w").write(c)
    print("✅ Fixed week1.html title (removed v2)")
else:
    print("⚠️  week1.html title v2 not found (already fixed?)")

# ── Fix 2: roadmap.html sidebar labels ────────────────────────────────────────
rm = os.path.join(base, "roadmap.html")
c = open(rm).read()

# Fix Week 13: NLP -> Natural Language Processing
c = c.replace('>Week 13 — NLP<', '>Week 13 — Natural Language Processing<')

# Fix Week 14: Transformers -> Transformers & Attention
c = c.replace('>Week 14 — Transformers<', '>Week 14 — Transformers &amp; Attention<')

# Fix Week 15: LLMs + GenAI -> LLM Engineering
c = c.replace('>Week 15 — LLMs + GenAI<', '>Week 15 — LLM Engineering<')

# Fix Week 16: RAG + Agents -> Production AI Engineering
c = c.replace('>Week 16 — RAG + Agents<', '>Week 16 — Production AI Engineering<')

# Fix Week 17: "Deploy + Flask+Docker" -> "Week 17 — Deploy + Flask + Docker"
# This one may be in a nav-item linking to week17.html
# First, find what the current label looks like
import re
# Find all nav-items linking to week17.html
w17_links = re.findall(r'(<a class="nav-item"[^>]*href="week17\.html"[^>]*>.*?</a>)', c, re.DOTALL)
print(f"week17 nav-items found: {len(w17_links)}")
for lnk in w17_links:
    print(f"  {lnk[:200]}")

# The "Deploy + Flask+Docker" label (missing "Week 17 —" prefix)
old_label = 'Deploy + Flask+Docker'
new_label = 'Week 17 — Deploy + Flask + Docker'
if old_label in c:
    c = c.replace(old_label, new_label, 1)
    print(f"✅ Fixed Week 17 label: {old_label} -> {new_label}")

# Remove phantom "Capstone + Portfolio" entry / Week 18 entry
# Find and remove it - it's likely a nav-item with no real week file
# Let's find it
capstone_match = re.search(r'<a class="nav-item"[^>]*>.*?Capstone.*?</a>', c, re.DOTALL)
if capstone_match:
    print(f"Found Capstone entry: {capstone_match.group(0)[:200]}")
    c = c[:capstone_match.start()] + c[capstone_match.end():]
    print("✅ Removed phantom Capstone + Portfolio entry")
else:
    # Try simpler search
    if 'Capstone' in c:
        idx = c.find('Capstone')
        print(f"Found 'Capstone' at index {idx}: ...{c[max(0,idx-50):idx+100]}...")
    else:
        print("No Capstone entry found in roadmap.html")

open(rm, "w").write(c)
print("\n✅ roadmap.html saved")

# ── Verify ────────────────────────────────────────────────────────────────────
print("\n--- Verification ---")
c1 = open(w1).read()
title_m = re.search(r'<title>(.*?)</title>', c1)
print(f"week1.html title: {title_m.group(1) if title_m else 'NOT FOUND'}")

rm_c = open(rm).read()
for label in ['Week 13 — Natural Language Processing', 'Week 14 — Transformers',
              'Week 15 — LLM Engineering', 'Week 16 — Production AI Engineering',
              'Week 17 — Deploy']:
    found = label in rm_c
    print(f"  {'✅' if found else '❌'} roadmap has: '{label}'")
print(f"  {'❌ STILL HAS' if 'Capstone + Portfolio' in rm_c else '✅ No'} Capstone entry")
