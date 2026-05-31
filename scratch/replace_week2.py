with open('/Users/amananand/Downloads/SDE/ai:ml/week2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update SQL Links
print("Updating SQL links in week2.html...")
content = content.replace(
    "Mode Analytics SQL Tutorial &rarr; <strong>mode.com/sql-tutorial/</strong>",
    "DataLemur SQL Tutorial &rarr; <strong>datalemur.com/sql-tutorial</strong>"
)
content = content.replace(
    "Mode Analytics SQL Tutorial → <strong>mode.com/sql-tutorial/</strong>",
    "DataLemur SQL Tutorial → <strong>datalemur.com/sql-tutorial</strong>"
)
content = content.replace(
    "Go to <strong>mode.com/sql-tutorial/</strong>.",
    "Go to <strong>datalemur.com/sql-tutorial</strong>."
)

# Replace the resource cards
old_card = """  <a class="res-card type-web-card" href="https://mode.com/sql-tutorial/" target="_blank">
      <div class="res-icon type-web">&#127891;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Course &middot; 4 hours</div>
        <span class="res-title">Mode Analytics SQL Tutorial</span>
        <div class="res-desc">Excellent interactive SQL course covering basic SELECT/WHERE queries up to joins.</div>
        <div class="res-why">&#10026; Practical</div>
      </div>
    </a>"""

new_card = """  <a class="res-card type-web-card" href="https://datalemur.com/sql-tutorial" target="_blank">
      <div class="res-icon type-web">&#127891;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Course &middot; 4 hours</div>
        <span class="res-title">DataLemur SQL Tutorial</span>
        <div class="res-desc">Excellent interactive SQL course covering basic SELECT/WHERE queries up to intermediate concepts.</div>
        <div class="res-why">&#10026; Practical</div>
      </div>
    </a>"""

content = content.replace(old_card, new_card)

# 2. Update Day 13 Git Resources
print("Updating Day 13 Git resources...")

# Let's locate the resources section in Day 13 block
# We know Day 13 block starts at <div class="day-section" id="day-13">
# We want to replace the resource cards inside this block.
day13_start = content.find('<div class="day-section" id="day-13">')
day14_start = content.find('<div class="day-section" id="day-14">')

if day13_start != -1 and day14_start != -1:
    day13_block = content[day13_start:day14_start]
    
    # We want to replace the resources-grid in day13_block
    res_grid_start = day13_block.find('<div class="resources-grid">')
    res_grid_end = day13_block.find('</div>\n  </div>\n</section>', res_grid_start)
    if res_grid_start != -1 and res_grid_end != -1:
        old_grid = day13_block[res_grid_start:res_grid_end+6]
        
        new_grid = """<div class="resources-grid">
    <a class="res-card type-doc-card" href="https://learngitbranching.js.org/" target="_blank">
      <div class="res-icon type-doc">&#128214;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--doc)">Interactive &middot; 30 min</div>
        <span class="res-title">Learn Git Branching</span>
        <div class="res-desc">The most visual and interactive way to learn Git branching, merges, rebases, and commits.</div>
        <div class="res-why">&#10026; Recommended</div>
      </div>
    </a>
    <a class="res-card type-web-card" href="https://git-scm.com/docs/gittutorial" target="_blank">
      <div class="res-icon type-web">&#127891;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Tutorial &middot; 15 min</div>
        <span class="res-title">Official Git Tutorial</span>
        <div class="res-desc">The official introduction to Git commands and standard collaborative developer workflows.</div>
        <div class="res-why">&#10026; Docs</div>
      </div>
    </a>
    <a class="res-card type-web-card" href="https://github.com/git-guides" target="_blank">
      <div class="res-icon type-web">&#127891;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Guide &middot; 10 min</div>
        <span class="res-title">GitHub Guides</span>
        <div class="res-desc">GitHub's own beginner-friendly quickstart guides for essential Git operations and workflows.</div>
        <div class="res-why">&#10026; Essential</div>
      </div>
    </a>
    <a class="res-card type-web-card" href="https://ohshitgit.com/" target="_blank">
      <div class="res-icon type-web">&#127891;</div>
      <div class="res-body">
        <div class="res-type" style="color:var(--web)">Guide &middot; 5 min</div>
        <span class="res-title">Oh Shit, Git!?!</span>
        <div class="res-desc">Practical recipes and explanations for getting out of common Git states and mistakes.</div>
        <div class="res-why">&#10026; Cheat Sheet</div>
      </div>
    </a>
  </div>"""
        
        # Replace only in the Day 13 block
        new_day13_block = day13_block.replace(old_grid, new_grid)
        content = content.replace(day13_block, new_day13_block)
        print("Successfully updated Day 13 resources in week2.html!")
    else:
        print("Could not find resources-grid in Day 13 block.")
else:
    print("Could not find Day 13 start/end.")

with open('/Users/amananand/Downloads/SDE/ai:ml/week2.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished saving week2.html")
