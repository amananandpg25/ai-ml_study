import os

path = "/Users/amananand/Downloads/SDE/ai:ml/week2.html"
html = open(path, 'r', encoding='utf-8').read()

# 1. Replace Concept Map
old_map = """    <div class="concept-map-flow" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11.5px; margin-bottom:0.75rem;">
      <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Comprehensions</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Generators & Decorators</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">SQL Basics</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Aggregations</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Joins</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Git Basics</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Git Collab</span>
    </div>"""

new_map = """    <div class="concept-map-flow" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11.5px; margin-bottom:0.75rem;">
      <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Pandas Series &amp; DataFrames</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Data Cleaning</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">GroupBy &amp; Aggregation</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">SQL Basics</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">SQL Advanced</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">Git Workflow</span>
    <span style="color:var(--muted); font-weight:bold;">➔</span>
    <span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">EDA Project</span>
    </div>"""

html = html.replace(old_map, new_map)

# 2. Day 8 sorting with df = prefix
old_sort = """df.sort_values("salary", ascending=False)          # highest first
df.sort_values(["city", "salary"], ascending=[True, False])  # multi-col sort

# sort_index — sort by the index labels
df.sort_index()          # useful after groupby/reset_index shuffles rows
df.sort_index(ascending=False)"""

new_sort = """df = df.sort_values("salary", ascending=False)          # highest first
df = df.sort_values(["city", "salary"], ascending=[True, False])  # multi-col sort

# sort_index — sort by the index labels
df = df.sort_index()          # useful after groupby/reset_index shuffles rows
df = df.sort_index(ascending=False)"""

html = html.replace(old_sort, new_sort)

# 3. iloc vs loc diagram insertion
old_hinglish = '<div class="hinglish">💡 Ek line mein: DataFrame = Excel ka sheet Python mein. iloc = position se select (0,1,2...), loc = label se select ("name","age"). Boolean indexing = conditions lagao jaise SQL WHERE clause.</div>'

iloc_loc_diagram = """  <div class="diagram">
    <pre>
    iloc vs loc Selection Mechanics
    =================================
    DataFrame index labels = ["a", "b", "c"]
    
    Index Labels      Data Columns
    (loc looks here)   (iloc looks here)
          ↓                 ↓
        +---+       +---------+-------+
    "a" | 0 | ----> | "Rahul" | 50000 |  <--- df.iloc[0] or df.loc["a"]
        +---+       +---------+-------+
    "b" | 1 | ----> | "Priya" | 65000 |  <--- df.iloc[1] or df.loc["b"]
        +---+       +---------+-------+
    "c" | 2 | ----> | "Arjun" | 45000 |  <--- df.iloc[2] or df.loc["c"]
        +---+       +---------+-------+
    </pre>
    <div class="diagram-cap">Visual mapping of label-based indexing (loc) vs integer position-based indexing (iloc).</div>
  </div>
"""

html = html.replace(old_hinglish, iloc_loc_diagram + "\n  " + old_hinglish)

# 4. Day 8 CLI Contact Book Warm-up Task
old_d8_tasks_start = """  <div id="day-8-tasks-section">
  <h2 class="sh2">💻 Coding Tasks</h2>

  <div class="task-block">"""

new_d8_tasks_start = """  <div id="day-8-tasks-section">
  <h2 class="sh2">💻 Coding Tasks</h2>

  <!-- Day 8 Python Warm-up Project (moved from Day 7) -->
  <div class="task-block">
    <div class="task-header" style="background:rgba(180,124,252,.08);border-color:rgba(180,124,252,.3)" onclick="toggleTask(this)" role="button" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')this.click()" aria-expanded="false">
      <span class="task-badge tb-proj">📦 PYTHON REFRESHER</span>
      <span class="task-title">CLI Contact Book — Python Recap Warm-up</span>
      <span class="task-time">⏱ 2.5 hours</span>
    </div>
    <div class="task-body">
      <p>Before diving into Pandas, recap your Python basics by building a command-line contact manager that uses <strong>OOP, lists, dicts, file I/O, exceptions, and lambdas</strong>. This cements your foundations.</p>
      <ul style="padding-left:1.2rem;font-size:13.5px;line-height:2.1">
        <li>✅ <strong>Add contact</strong> — name, phone, email, city (stored as object)</li>
        <li>✅ <strong>Search</strong> — by name or city (loops + conditions)</li>
        <li>✅ <strong>Delete</strong> — by name with custom error validation</li>
        <li>✅ <strong>List all</strong> — sorted alphabetically using <code>sorted()</code> and a <code>lambda</code></li>
        <li>✅ <strong>Persist</strong> — save/load to CSV on startup/exit</li>
      </ul>
      <button class="solution-toggle" onclick="toggleSolution('sol-d8-warmup')">👁 Show Contact Book Solution</button>
      <div class="solution-box" id="sol-d8-warmup">
        <div class="sol-header">✅ COMPLETE SOLUTION — contact_book.py</div>
        <div class="cb"><div class="cb-head"><span class="cb-lang">python</span><button class="copy-btn" onclick="copyCode(this)">copy</button><button class="run-btn" onclick="runCode(this)" style="margin-left: 4px;">Run</button></div>
        <pre><span class="cm"># contact_book.py — Python Review Warm-up</span>
import csv, os

class Contact:
    def __init__(self, name, phone, email, city):
        self.name = name.strip().title()
        self.phone = phone.strip()
        self.email = email.strip().lower()
        self.city = city.strip().title()

    def __str__(self):
        return f"{self.name:<18} | {self.phone:<12} | {self.email:<23} | {self.city}"

    def to_dict(self):
        return {"name":self.name,"phone":self.phone,"email":self.email,"city":self.city}

class ContactBook:
    FIELDS = ["name","phone","email","city"]

    def __init__(self, filename="contacts.csv"):
        self.filename = filename
        self.contacts = []
        self.load()

    def load(self):
        if not os.path.exists(self.filename): return
        try:
            with open(self.filename,"r") as f:
                for row in csv.DictReader(f):
                    self.contacts.append(Contact(row["name"],row["phone"],row["email"],row["city"]))
        except Exception as e:
            print(f"Load error: {e}")

    def save(self):
        with open(self.filename,"w",newline="") as f:
            w = csv.DictWriter(f,fieldnames=self.FIELDS)
            w.writeheader()
            w.writerows([c.to_dict() for c in self.contacts])

    def add(self):
        name = input("Name: ")
        if any(c.name.lower()==name.lower() for c in self.contacts):
            print("Contact already exists!"); return
        self.contacts.append(Contact(name, input("Phone: "), input("Email: "), input("City: ")))
        self.save(); print("✅ Contact added!")

    def search(self):
        q = input("Search (name/city): ").lower()
        results = [c for c in self.contacts if q in c.name.lower() or q in c.city.lower()]
        for c in results: print(c)

    def delete(self):
        name = input("Delete contact name: ")
        for i, c in enumerate(self.contacts):
            if c.name.lower() == name.lower():
                self.contacts.pop(i)
                self.save(); print("✅ Deleted!"); return
        print("Contact not found!")

    def list_all(self):
        if not self.contacts: print("No contacts yet!"); return
        for c in sorted(self.contacts, key=lambda c: c.name): print(c)

def main():
    book = ContactBook()
    menu = {"1":book.add,"2":book.search,"3":book.delete,"4":book.list_all}
    while True:
        print("\\n📒 1.Add 2.Search 3.Delete 4.List 5.Exit")
        choice = input("Choice: ").strip()
        if choice == "5": break
        if choice in menu: menu[choice]()

if __name__ == "__main__":
    main()</pre></div>
      </div>
      <div class="done-when">Your contact book loads existing CSV entries, allows adding/deleting, and list sorted contacts alphabetically.</div>
      <div class="git-block">git add contact_book.py && git commit -m "feat: add CLI contact book python refresher project"</div>
    </div>
  </div>

  <div class="task-block">"""

html = html.replace(old_d8_tasks_start, new_d8_tasks_start)

# 5. Day 9 Merge Diagram
old_d9_connect = '<div class="ml-connect">In ML, you\'ll often merge feature tables with label tables using an ID key — like merging a customer features table with a churn label table. Knowing merge types (inner vs left) prevents data leakage and silent row drops.</div>'

merge_diagram = """  <div class="diagram">
    <pre>
    Merge Types Diagram (how = ...)
    =================================
    Left DataFrame: [id, name] (id = 1, 2, 3)
    Right DataFrame: [id, score] (id = 1, 2, 4)

    1. inner: Only rows with keys present in BOTH DataFrames.
       +----+--------+-------+
       | id |  name  | score |
       +----+--------+-------+
       |  1 | Rahul  |  85.0 |
       |  2 | Priya  |  92.0 |
       +----+--------+-------+

    2. left: All rows from Left, plus matching columns from Right.
       +----+--------+-------+
       | id |  name  | score |
       +----+--------+-------+
       |  1 | Rahul  |  85.0 |
       |  2 | Priya  |  92.0 |
       |  3 | Arjun  |   NaN |   &lt;--- No match in Right DataFrame
       +----+--------+-------+

    3. right: All rows from Right, plus matching columns from Left.
       +----+--------+-------+
       | id |  name  | score |
       +----+--------+-------+
       |  1 | Rahul  |  85.0 |
       |  2 | Priya  |  92.0 |
       |  4 |   NaN  |  78.0 |   &lt;--- No match in Left DataFrame
       +----+--------+-------+

    4. outer: All rows from Left and Right (Full Union).
       +----+--------+-------+
       | id |  name  | score |
       +----+--------+-------+
       |  1 | Rahul  |  85.0 |
       |  2 | Priya  |  92.0 |
       |  3 | Arjun  |   NaN |
       |  4 |   NaN  |  78.0 |
       +----+--------+-------+
    </pre>
    <div class="diagram-cap">Visual comparison of inner, left, right, and outer merge output rows.</div>
  </div>
"""

html = html.replace(old_d9_connect, merge_diagram + "\n  " + old_d9_connect)

# 6. Day 9 SettingWithCopyWarning Hint
old_d9_task2_desc = '<p>Take titanic.csv. Clean it completely: (1) fill Age nulls with median by Pclass (advanced — use groupby fillna), (2) fill Embarked nulls with mode, (3) drop Cabin column (too many nulls), (4) create a new column "FamilySize" = SibSp + Parch + 1, (5) apply a lambda to create "IsAlone" = 1 if FamilySize==1. Save cleaned CSV.</p>'

new_d9_task2_desc = """<p>Take titanic.csv. Clean it completely: (1) fill Age nulls with median by Pclass (advanced — use groupby fillna), (2) fill Embarked nulls with mode, (3) drop Cabin column (too many nulls), (4) create a new column "FamilySize" = SibSp + Parch + 1, (5) apply a lambda to create "IsAlone" = 1 if FamilySize==1. Save cleaned CSV.</p>
      <p><strong>💡 Hint:</strong> If you get a <code>SettingWithCopyWarning</code>, add <code>.copy()</code> when creating your subset — this was covered in Day 8.</p>"""

html = html.replace(old_d9_task2_desc, new_d9_task2_desc)

# 7. Inject Day 9-13 resources sections
# Place before <div class="takeaways"> on each day
old_d9_takeaways = '  <div class="takeaways">\n    <h3>⚡ Key Takeaways — Day 9</h3>'
new_d9_resources = """  <div id="day-9-resources-section">
  <h2 class="sh2">📚 Day 9 Resources</h2>
  <div class="resources-grid">
    <a class="resource-card" href="https://pandas.pydata.org/docs/user_guide/missing_data.html" target="_blank">
      <div class="rc-type">OFFICIAL DOCS</div>
      <div class="rc-title">Pandas Missing Data Handling</div>
      <div class="rc-sub">Official guide on fillna, dropna, and interpolation methods.</div>
    </a>
    <a class="resource-card" href="https://www.kaggle.com/code/alexisbcook/data-cleaning-challenge-handling-missing-values" target="_blank">
      <div class="rc-type">INTERACTIVE TUTORIAL</div>
      <div class="rc-title">Kaggle Data Cleaning Course</div>
      <div class="rc-sub">Hands-on micro-course on handling missing values and scaling.</div>
    </a>
  </div>
  </div>

  <div class="takeaways">
    <h3>⚡ Key Takeaways — Day 9</h3>"""

html = html.replace(old_d9_takeaways, new_d9_resources)

old_d10_takeaways = '  <div class="takeaways" id="day-10-takeaways">\n    <h3>⚡ Key Takeaways — Day 10</h3>'
if old_d10_takeaways not in html:
    old_d10_takeaways = '  <div class="takeaways">\n    <h3>⚡ Key Takeaways — Day 10</h3>'

new_d10_resources = """  <div id="day-10-resources-section">
  <h2 class="sh2">📚 Day 10 Resources</h2>
  <div class="resources-grid">
    <a class="resource-card" href="https://pandas.pydata.org/docs/user_guide/groupby.html" target="_blank">
      <div class="rc-type">OFFICIAL DOCS</div>
      <div class="rc-title">Pandas GroupBy: Split-Apply-Combine</div>
      <div class="rc-sub">Official user guide explaining how groupby works under the hood.</div>
    </a>
    <a class="resource-card" href="https://realpython.com/pandas-groupby/" target="_blank">
      <div class="rc-type">EXPLAINER ARTICLE</div>
      <div class="rc-title">Real Python: Pandas GroupBy Deep Dive</div>
      <div class="rc-sub">A highly detailed, practical guide to grouping and aggregating data.</div>
    </a>
  </div>
  </div>

  <div class="takeaways">
    <h3>⚡ Key Takeaways — Day 10</h3>"""

html = html.replace(old_d10_takeaways, new_d10_resources)

old_d11_takeaways = '  <div class="takeaways" id="day-11-takeaways">\n    <h3>⚡ Key Takeaways — Day 11</h3>'
if old_d11_takeaways not in html:
    old_d11_takeaways = '  <div class="takeaways">\n    <h3>⚡ Key Takeaways — Day 11</h3>'

new_d11_resources = """  <div id="day-11-resources-section">
  <h2 class="sh2">📚 Day 11 Resources</h2>
  <div class="resources-grid">
    <a class="resource-card" href="https://www.thoughtspot.com/sql-tutorial" target="_blank">
      <div class="rc-type">INTERACTIVE TUTORIAL</div>
      <div class="rc-title">ThoughtSpot/Mode SQL Tutorial</div>
      <div class="rc-sub">The classic SQL tutorial. Complete SELECT, WHERE, and aggregations.</div>
    </a>
    <a class="resource-card" href="https://sqlzoo.net/" target="_blank">
      <div class="rc-type">PRACTICE ENVIRONMENT</div>
      <div class="rc-title">SQLZoo Interactive Exercises</div>
      <div class="rc-sub">Excellent sandbox to write queries against real databases.</div>
    </a>
    <a class="resource-card" href="https://pgexercises.com/" target="_blank">
      <div class="rc-type">POSTGRESQL PRACTICE</div>
      <div class="rc-title">PGExercises (PostgreSQL-focused)</div>
      <div class="rc-sub">A structured, PostgreSQL-based set of problems from easy to advanced.</div>
    </a>
  </div>
  </div>

  <div class="takeaways">
    <h3>⚡ Key Takeaways — Day 11</h3>"""

html = html.replace(old_d11_takeaways, new_d11_resources)

old_d12_takeaways = '  <div class="takeaways" id="day-12-takeaways">\n    <h3>⚡ Key Takeaways — Day 12</h3>'
if old_d12_takeaways not in html:
    old_d12_takeaways = '  <div class="takeaways">\n    <h3>⚡ Key Takeaways — Day 12</h3>'

new_d12_resources = """  <div id="day-12-resources-section">
  <h2 class="sh2">📚 Day 12 Resources</h2>
  <div class="resources-grid">
    <a class="resource-card" href="https://www.postgresql.org/docs/current/tutorial-window.html" target="_blank">
      <div class="rc-type">OFFICIAL DOCS</div>
      <div class="rc-title">PostgreSQL Window Functions Tutorial</div>
      <div class="rc-sub">Official guide on window calculations like ROW_NUMBER and RANK.</div>
    </a>
    <a class="resource-card" href="https://www.stratascratch.com/" target="_blank">
      <div class="rc-type">INTERVIEW PROBLEMS</div>
      <div class="rc-title">StrataScratch Interview Practice</div>
      <div class="rc-sub">Real SQL queries from top companies like Airbnb and Netflix.</div>
    </a>
  </div>
  </div>

  <div class="takeaways">
    <h3>⚡ Key Takeaways — Day 12</h3>"""

html = html.replace(old_d12_takeaways, new_d12_resources)

old_d13_takeaways = '  <div class="takeaways" id="day-13-takeaways">\n    <h3>⚡ Key Takeaways — Day 13</h3>'
if old_d13_takeaways not in html:
    old_d13_takeaways = '  <div class="takeaways">\n    <h3>⚡ Key Takeaways — Day 13</h3>'

new_d13_resources = """  <div id="day-13-resources-section">
  <h2 class="sh2">📚 Day 13 Resources</h2>
  <div class="resources-grid">
    <a class="resource-card" href="https://git-scm.com/book/en/v2" target="_blank">
      <div class="rc-type">OFFICIAL BOOK</div>
      <div class="rc-title">Pro Git Book (Free Online)</div>
      <div class="rc-sub">The authoritative guide to everything Git has to offer.</div>
    </a>
    <a class="resource-card" href="https://www.atlassian.com/git/tutorials" target="_blank">
      <div class="rc-type">GUIDE</div>
      <div class="rc-title">Atlassian Git Tutorial</div>
      <div class="rc-sub">Visual explanations of branching, merging, and git workflows.</div>
    </a>
  </div>
  </div>

  <div class="takeaways">
    <h3>⚡ Key Takeaways — Day 13</h3>"""

html = html.replace(old_d13_takeaways, new_d13_resources)

# 8. Day 14 Revision Flashcards
old_d14_takeaways = '  <div class="takeaways">\n    <h3>⚡ Key Takeaways — Day 14</h3>'
new_d14_flashcards = """  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Week 2 Recap Flashcards</h2>
  <p class="flashcard-hint">CLICK TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">df.copy() vs direct slicing assignment?</div><div class="fc-back">.copy() creates a new object in memory<br>Avoids SettingWithCopyWarning</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is Pandas GroupBy pattern?</div><div class="fc-back">Split-Apply-Combine:<br>Split by key, run aggregation, concat back</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">SQL SELECT execution order?</div><div class="fc-back">FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Window function (OVER) purpose?</div><div class="fc-back">Calculates values across rows without<br>collapsing them into a single row</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Git merge vs rebase?</div><div class="fc-back">Merge combines branches via commit history;<br>rebase rewrites history to be linear</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">How does git branch work internally?</div><div class="fc-back">A simple 41-character pointer file<br>pointing to a specific commit hash</div></div></div>
  </div>

  <div class="takeaways">
    <h3>⚡ Key Takeaways — Day 14</h3>"""

html = html.replace(old_d14_takeaways, new_d14_flashcards)

# 9. Replace Mode SQL Redirect Links
html = html.replace('mode.com/sql-tutorial/', 'www.thoughtspot.com/sql-tutorial')
html = html.replace('https://mode.com/sql-tutorial/', 'https://www.thoughtspot.com/sql-tutorial')

# Write back changes
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("🎉 Successfully patched week2.html!")
