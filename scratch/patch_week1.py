import os

path = "/Users/amananand/Downloads/SDE/ai:ml/week1.html"
html = open(path, 'r', encoding='utf-8').read()

# 1. Day 1: Replace 2024 with 2026
html = html.replace('birth_year = <span class="num">2024</span> - user_age          <span class="cm"># now this works ✅</span>',
                    'birth_year = <span class="num">2026</span> - user_age          <span class="cm"># now this works ✅</span>')
html = html.replace('birth_year = 2024 - age', 'birth_year = 2026 - age')
html = html.replace('birth_year = <span class="num">2024</span> - age', 'birth_year = <span class="num">2026</span> - age')
html = html.replace('Hint: <code>input()</code> se data lo, age ko <code>int()</code> mein convert karo, birth_year = 2024 - age calculate karo, phir f-string se print karo.',
                    'Hint: <code>input()</code> se data lo, age ko <code>int()</code> mein convert karo, birth_year = 2026 - age calculate karo, phir f-string se print karo.')
html = html.replace('Then 2024 - "20" crashes', 'Then 2026 - "20" crashes')

# 2. Day 1: Remove Collections module Section 5
target_collections_d1 = """  <h3 class="sh3">5. The `collections` Module (Advanced Data Structures)</h3>
  <div class="ml-connect">In ML (especially NLP and graphs), built-in dictionaries and lists are sometimes too basic. Python's `collections` module provides specialized, high-performance data structures.</div>
  
  <div class="cb">
    <div class="cb-head"><span class="cb-lang">python</span></div>
    <pre><span class="kw">from</span> collections <span class="kw">import</span> Counter, defaultdict, deque

<span class="cm"># 1. Counter: Automatically counts frequencies (great for NLP token counts)</span>
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)
<span class="bi">print</span>(word_counts)  <span class="cm"># Counter({'apple': 3, 'banana': 2, 'orange': 1})</span>

<span class="cm"># 2. defaultdict: A dict that doesn't throw KeyError if key is missing</span>
graph = defaultdict(<span class="bi">list</span>)
graph['node1'].append('node2')  <span class="cm"># 'node1' automatically created as empty list first!</span>

<span class="cm"># 3. deque: Double-ended queue. Super fast O(1) appends/pops from BOTH ends</span>
<span class="cm"># Standard lists are O(n) for popping from the front.</span>
queue = deque([1, 2, 3])
queue.appendleft(0)  <span class="cm"># Fast insertion at the beginning</span></pre>
  </div>"""

if target_collections_d1 in html:
    html = html.replace(target_collections_d1, '')
    print("✅ Removed collections module from Day 1.")
else:
    # Try alternate without whitespace if needed
    print("⚠️ Day 1 collections section not found directly.")

# 3. Day 2: Append Collections module Section 5 to the end of Day 2 theory
target_d2_misconception_end = """  <div class="misconception">
    <strong>⚠️ Top Mistakes — Day 2:</strong>
    <strong>1. List index out of range:</strong> <code>lst[5]</code> when list has 4 items → IndexError. Fix: check <code>len(lst)</code> first.<br>
    <strong>2. dict KeyError:</strong> <code>d["missing_key"]</code> crashes if key doesn't exist. Fix: use <code>d.get("key", default)</code>.<br>
    <strong>3. Empty set confusion:</strong> <code>{}</code> creates an empty DICT, not a set. Use <code>set()</code> for empty set.<br>
    <strong>4. sort() vs sorted():</strong> <code>list.sort()</code> modifies in place and returns None. <code>sorted(list)</code> returns a new list.
  </div>
  </div>"""

replacement_d2_misconception_end = """  <div class="misconception">
    <strong>⚠️ Top Mistakes — Day 2:</strong>
    <strong>1. List index out of range:</strong> <code>lst[5]</code> when list has 4 items → IndexError. Fix: check <code>len(lst)</code> first.<br>
    <strong>2. dict KeyError:</strong> <code>d["missing_key"]</code> crashes if key doesn't exist. Fix: use <code>d.get("key", default)</code>.<br>
    <strong>3. Empty set confusion:</strong> <code>{}</code> creates an empty DICT, not a set. Use <code>set()</code> for empty set.<br>
    <strong>4. sort() vs sorted():</strong> <code>list.sort()</code> modifies in place and returns None. <code>sorted(list)</code> returns a new list.
  </div>

  <h3 class="sh3">5. The `collections` Module (Advanced Data Structures)</h3>
  <div class="ml-connect">In ML (especially NLP and graphs), built-in dictionaries and lists are sometimes too basic. Python's `collections` module provides specialized, high-performance data structures.</div>
  
  <div class="cb">
    <div class="cb-head"><span class="cb-lang">python — collections_demo.py</span><button class="copy-btn" onclick="copyCode(this)">copy</button><button class="run-btn" onclick="runCode(this)" style="margin-left: 4px;">Run</button></div>
    <pre><span class="kw">from</span> collections <span class="kw">import</span> Counter, defaultdict, deque

<span class="cm"># 1. Counter: Automatically counts frequencies (great for NLP token counts)</span>
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)
<span class="bi">print</span>(word_counts)  <span class="cm"># Counter({'apple': 3, 'banana': 2, 'orange': 1})</span>

<span class="cm"># 2. defaultdict: A dict that doesn't throw KeyError if key is missing</span>
graph = defaultdict(<span class="bi">list</span>)
graph['node1'].append('node2')  <span class="cm"># 'node1' automatically created as empty list first!</span>

<span class="cm"># 3. deque: Double-ended queue. Super fast O(1) appends/pops from BOTH ends</span>
<span class="cm"># Standard lists are O(n) for popping from the front.</span>
queue = deque([1, 2, 3])
queue.appendleft(0)  <span class="cm"># Fast insertion at the beginning</span></pre>
  </div>
  </div>"""

if target_d2_misconception_end in html:
    html = html.replace(target_d2_misconception_end, replacement_d2_misconception_end)
    print("✅ Appended collections module to Day 2.")
else:
    print("❌ Day 2 misconception end not found.")

# 4. Day 2 Quiz empty set feedback update
target_q7_fb = """    <div class="quiz-feedback correct-fb" id="q7-correct">✅ Correct! {} creates an empty DICT, not an empty set. To create an empty set use set(). This is a famous Python gotcha that trips up beginners constantly.</div>
    <div class="quiz-feedback wrong-fb" id="q7-wrong">❌ Tricky! {} creates an empty DICT. For empty set you need set() — because {} is ambiguous and Python chose dict. Answer is B.</div>"""

replacement_q7_fb = """    <div class="quiz-feedback correct-fb" id="q7-correct">✅ Correct! {} creates an empty DICT, not an empty set. To create an empty set, you must use set() — not {}, which makes an empty dict. This is a famous Python gotcha that trips up beginners constantly.</div>
    <div class="quiz-feedback wrong-fb" id="q7-wrong">❌ Tricky! {} creates an empty DICT. To create an empty set, you must use set() — not {}, which makes an empty dict (because {} is ambiguous and Python default-assigned it to dict). Answer is B.</div>"""

html = html.replace(target_q7_fb, replacement_q7_fb)

# 5. Day 3 Predict-the-Output insertion
target_d3_theory_end = """  <strong>range(n) goes 0 to n-1:</strong> range(5) = [0,1,2,3,4], NOT [1,2,3,4,5].<br>
  <strong>Off-by-one in slices:</strong> range(1,11) gives 1 to 10 — the 11 is excluded.</div>

  <h2 class="sh2">✅ Day 3 Quiz</h2>"""

replacement_d3_theory_end = """  <strong>range(n) goes 0 to n-1:</strong> range(5) = [0,1,2,3,4], NOT [1,2,3,4,5].<br>
  <strong>Off-by-one in slices:</strong> range(1,11) gives 1 to 10 — the 11 is excluded.</div>
  </div>

  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre>scores = [<span class="num">10</span>, <span class="num">20</span>, <span class="num">30</span>, <span class="num">40</span>]
passed = [x <span class="kw">for</span> x <span class="kw">in</span> scores <span class="kw">if</span> x &gt; <span class="num">25</span>]
<span class="bi">print</span>(passed)</pre></div>
    <input class="predict-input" id="p3-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p3-1','[30, 40]')">Check Answer</button>
    <div class="predict-result" id="p3-1-result"></div>
  </div>

  <h2 class="sh2">✅ Day 3 Quiz</h2>"""

if target_d3_theory_end in html:
    html = html.replace(target_d3_theory_end, replacement_d3_theory_end)
    print("✅ Injected Day 3 Predict-the-Output.")
else:
    print("❌ Day 3 theory end not found.")

# 6. Day 4 Predict-the-Output insertion
target_d4_theory_end = """  <div class="misconception"><strong>⚠️ Scope Confusion:</strong> Variables defined inside a function don't exist outside it. <code>x = 10</code> inside a function is a local variable — <code>print(x)</code> outside the function crashes with NameError. Use return to pass values out of functions.</div>

  <h2 class="sh2">✅ Quick Quiz</h2>"""

replacement_d4_theory_end = """  <div class="misconception"><strong>⚠️ Scope Confusion:</strong> Variables defined inside a function don't exist outside it. <code>x = 10</code> inside a function is a local variable — <code>print(x)</code> outside the function crashes with NameError. Use return to pass values out of functions.</div>
  </div>

  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre>def calculate(x, y=5):
    return x * y
print(calculate(3))
print(calculate(3, 3))</pre></div>
    <input class="predict-input" id="p4-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p4-1','15\\n9')">Check Answer</button>
    <div class="predict-result" id="p4-1-result"></div>
  </div>

  <h2 class="sh2">✅ Quick Quiz</h2>"""

if target_d4_theory_end in html:
    html = html.replace(target_d4_theory_end, replacement_d4_theory_end)
    print("✅ Injected Day 4 Predict-the-Output.")
else:
    print("❌ Day 4 theory end not found.")

# 7. Day 5 Predict-the-Output and Flashcards insertion
target_d5_theory_end = """  <div class="ml-connect">In ML, you load datasets from CSV/JSON constantly. If a file doesn't exist, if a column is missing, if data is corrupted — your training script should handle it gracefully, not crash. Production ML pipelines have try/except everywhere.</div>

  <h2 class="sh2">✅ Quiz</h2>"""

replacement_d5_theory_end = """  <div class="ml-connect">In ML, you load datasets from CSV/JSON constantly. If a file doesn't exist, if a column is missing, if data is corrupted — your training script should handle it gracefully, not crash. Production ML pipelines have try/except everywhere.</div>
  </div>

  <!-- PREDICT THE OUTPUT -->
  <h2 class="sh2">🔮 Predict the Output</h2>
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT — Q1</div>
    <div class="cb" style="margin:.5rem 0"><div class="cb-head"><span class="cb-lang">python</span></div>
    <pre>try:
    x = 10 / 0
except ZeroDivisionError:
    x = 0
finally:
    x = 99
print(x)</pre></div>
    <input class="predict-input" id="p5-1-input" placeholder="Type your answer here..." />
    <button class="predict-btn" onclick="checkPredict('p5-1','99')">Check Answer</button>
    <div class="predict-result" id="p5-1-result"></div>
  </div>

  <h2 class="sh2">✅ Quiz</h2>"""

if target_d5_theory_end in html:
    html = html.replace(target_d5_theory_end, replacement_d5_theory_end)
    print("✅ Injected Day 5 Predict-the-Output.")
else:
    print("❌ Day 5 theory end not found.")

target_d5_task_start = """  <h2 class="sh2">💻 Task — Dataset Persistence Engine</h2>"""
replacement_d5_task_start = """  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Day 5 Flashcards</h2>
  <p class="flashcard-hint">CLICK TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">with open() context manager advantage?</div><div class="fc-back">Auto-closes the file even if error occurs<br>Prevents memory/resource leaks</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is try/except?</div><div class="fc-back">Error handling blocks<br>Prevents crash by capturing exception</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What does finally block do?</div><div class="fc-back">Always runs, regardless of whether<br>an exception was thrown or caught</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Common file exceptions?</div><div class="fc-back">FileNotFoundError, PermissionError<br>Always catch these during I/O ops</div></div></div>
  </div>

  <h2 class="sh2">💻 Task — Dataset Persistence Engine</h2>"""

if target_d5_task_start in html:
    html = html.replace(target_d5_task_start, replacement_d5_task_start)
    print("✅ Injected Day 5 Flashcards.")
else:
    print("❌ Day 5 task start not found.")

# 8. Day 6 XP calibration (150 -> 200)
html = html.replace('onclick="completeDay(6,150)"', 'onclick="completeDay(6,200)"')
html = html.replace('✅ Mark Day 6 Complete — Earn 150 XP', '✅ Mark Day 6 Complete — Earn 200 XP')
html = html.replace('<div class="meta-row"><span class="meta-badge g">⏱ 4 hours</span><span class="meta-badge o">🔸 Intermediate</span><span class="meta-badge p">⚡ +150 XP</span></div>',
                    '<div class="meta-row"><span class="meta-badge g">⏱ 4 hours</span><span class="meta-badge o">🔸 Intermediate</span><span class="meta-badge p">⚡ +200 XP</span></div>')

# 9. Day 7 Title & Description & NumPy Task insertion
# Rename Day 7 in brand & sidebar
html = html.replace('<div class="brand">Week 1 — Python Basics &amp; Capstone</div>',
                    '<div class="brand">Week 1 — Python Basics &amp; Review</div>')
html = html.replace('<span class="sb-dot" style="background:var(--green)"></span>Day 7 — NumPy + Project',
                    '<span class="sb-dot" style="background:var(--green)"></span>Day 7 — NumPy &amp; Review')

target_d7_header = """    <h1>NumPy + Week 1 Final Project</h1>
    <p>NumPy is the foundation of ALL numerical ML in Python. Tensors in PyTorch, arrays in Pandas, matrices in scikit-learn — everything is NumPy underneath. Aur aaj Week 1 ka final project bhi complete karenge.</p>
    <div class="meta-row"><span class="meta-badge g">⏱ 5 hours</span><span class="meta-badge o">🔸 Intermediate</span><span class="meta-badge p">⚡ +250 XP</span></div>"""

replacement_d7_header = """    <h1>NumPy &amp; Week 1 Review</h1>
    <p>NumPy is the foundation of ALL numerical ML in Python. Tensors in PyTorch, arrays in Pandas, matrices in scikit-learn — everything is NumPy underneath. Today we master NumPy basics and run a comprehensive review of Week 1.</p>
    <div class="meta-row"><span class="meta-badge g">⏱ 4 hours</span><span class="meta-badge o">🔸 Intermediate</span><span class="meta-badge p">⚡ +300 XP</span></div>"""

html = html.replace(target_d7_header, replacement_d7_header)

target_d7_objectives = """  <div class="objectives"><h3>🎯 By end of Day 7:</h3><ul>
    <li>Create NumPy arrays and understand shape, dtype, ndim, size</li>
    <li>Use vectorized operations — why NumPy is 100x faster than Python loops</li>
    <li>Perform array math: sum, mean, std, min, max, dot product</li>
    <li>Reshape, slice, and boolean-index arrays</li>
    <li>Complete the Week 1 CLI Contact Book project</li>
  </ul></div>"""

replacement_d7_objectives = """  <div class="objectives"><h3>🎯 By end of Day 7:</h3><ul>
    <li>Create NumPy arrays and understand shape, dtype, ndim, size</li>
    <li>Use vectorized operations — why NumPy is 100x faster than Python loops</li>
    <li>Perform array math: sum, mean, std, min, max</li>
    <li>Reshape, slice, and boolean-index arrays</li>
    <li>Run a complete recap and review of all Python basics from Week 1</li>
  </ul></div>"""

html = html.replace(target_d7_objectives, replacement_d7_objectives)

# Get Day 7 project block boundaries
# We'll replace it with the new NumPy coding tasks and Day 7 flashcards
target_d7_project = """  <!-- WEEK 1 FINAL PROJECT -->
  <h2 class="sh2">🏆 Week 1 Final Project — CLI Contact Book</h2>
  <div class="task-block">
    <div class="task-header" style="background:rgba(180,124,252,.08);border-color:rgba(180,124,252,.3)" onclick="toggleTask(this)" role="button" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')this.click()" aria-expanded="false">
      <span class="task-badge tb-proj">📦 WEEK PROJECT</span>
      <span class="task-title">CLI Contact Book — All 7 Days Combined</span>
        <span class="task-time">⏱ 3 hours</span>
    </div>
    <div class="task-body">
      <p>Build a command-line contact manager that uses <strong>every concept from Week 1</strong>. This is your first real portfolio project.</p>
      <ul style="padding-left:1.2rem;font-size:13.5px;line-height:2.1">
        <li>✅ <strong>Add contact</strong> — name, phone, email, city (dicts)</li>
        <li>✅ <strong>Search</strong> — by name or city (loops + conditions)</li>
        <li>✅ <strong>Delete</strong> — by name (error handling)</li>
        <li>✅ <strong>List all</strong> — sorted alphabetically (sort + lambda)</li>
        <li>✅ <strong>Save to CSV</strong> — persistent storage (file I/O)</li>
        <li>✅ <strong>Load from CSV</strong> — restore on program start</li>
        <li>✅ <strong>OOP structure</strong> — Contact class + ContactBook class</li>
        <li>✅ <strong>Stats</strong> — NumPy: count by city, average phone length (bonus)</li>
      </ul>
      <button class="solution-toggle" onclick="toggleSolution('sol-d7-project')">👁 Show Complete Solution</button>
      <div class="solution-box" id="sol-d7-project">
        <div class="sol-header">✅ COMPLETE SOLUTION — contact_book.py</div>
        <div class="cb"><div class="cb-head"><span class="cb-lang">python</span><button class="copy-btn" onclick="copyCode(this)">copy</button><button class="run-btn" onclick="runCode(this)" style="margin-left: 4px;">Run</button></div>
        <pre><span class="cm"># contact_book.py — Week 1 Final Project</span>
# Skills: OOP, dicts, lists, file I/O, CSV, exception handling, sort, lambda
import csv, os

class Contact:
    def __init__(self, name, phone, email, city):
        self.name = name.strip().title()
        self.phone = phone.strip()
        self.email = email.strip().lower()
        self.city = city.strip().title()

    def __str__(self):
        return f" {self.name:<18} | {self.phone:<12} | {self.email:<23} | {self.city}"

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
            print(f"Loaded {len(self.contacts)} contacts.")
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
        phone = input("Phone: ")
        email = input("Email: ")
        city = input("City: ")
        self.contacts.append(Contact(name,phone,email,city))
        self.save(); print("✅ Contact added!")

    def search(self):
        q = input("Search (name/city): ").lower()
        results = [c for c in self.contacts if q in c.name.lower() or q in c.city.lower()]
        if results:
            for c in results: print(c)
        else: print("No results found.")

    def delete(self):
        name = input("Delete contact name: ")
        for i, c in enumerate(self.contacts):
            if c.name.lower() == name.lower():
                self.contacts.pop(i)
                self.save(); print("✅ Deleted!"); return
        print("Contact not found!")

    def list_all(self):
        if not self.contacts: print("No contacts yet!"); return
        sorted_c = sorted(self.contacts, key=lambda c: c.name)
        print(f"\\n  {'NAME':20} {'PHONE':13} {'EMAIL':25} CITY")
        print("  " + "─" * 70)
        for c in sorted_c: print(c)
        print(f"\\nTotal: {len(self.contacts)} contacts")


def main():
    book = ContactBook()
    menu = {"1":book.add,"2":book.search,"3":book.delete,"4":book.list_all}
    while True:
        print("\\n📒 CONTACT BOOK | 1.Add 2.Search 3.Delete 4.List 5.Exit")
        choice = input("Choice: ").strip()
        if choice == "5": print("Goodbye!"); break
        action = menu.get(choice)
        if action: action()
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()</pre></div>
      </div>
      <div class="done-when">Program starts, loads existing contacts, all 5 menu options work, contacts persist between runs, duplicate detection works, sorted alphabetically. Push to GitHub with README.</div>
      <div class="git-block">git add . && git commit -m "day7: numpy matrix operations and slicing practice"</div>
    </div>
  </div>"""

replacement_d7_project = """  <!-- CODING TASKS -->
  <h2 class="sh2">💻 Coding Tasks</h2>
  <div class="task-block">
    <div class="task-header" style="background:rgba(79,209,165,.06)" onclick="toggleTask(this)" role="button" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')this.click()" aria-expanded="false">
      <span class="task-badge tb-easy">🟢 EASY</span>
      <span class="task-title">NumPy Array &amp; Matrix Math Practice</span>
        <span class="task-time">⏱ 20 min</span>
    </div>
    <div class="task-body">
      <p>Write a script to practice basic NumPy matrix operations:
      <br>1. Create a 3x3 matrix containing values from 1 to 9.
      <br>2. Print its shape, dimensions, and size.
      <br>3. Extract and print the center element (5) and the entire third row.
      <br>4. Multiply the matrix by 2, add 10, and calculate the sum of all elements.</p>
      <button class="solution-toggle" onclick="toggleSolution('sol-d7t1')">👁 Show Solution</button>
      <div class="solution-box" id="sol-d7t1">
        <div class="sol-header">✅ SOLUTION — numpy_practice.py</div>
        <div class="cb"><div class="cb-head"><span class="cb-lang">python</span><button class="copy-btn" onclick="copyCode(this)">copy</button><button class="run-btn" onclick="runCode(this)" style="margin-left: 4px;">Run</button></div>
        <pre><span class="kw">import</span> numpy <span class="kw">as</span> np

# 1. Create 3x3 matrix
matrix = np.arange(1, 10).reshape(3, 3)
print("Matrix:\\n", matrix)

# 2. Print attributes
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)

# 3. Slicing
center_element = matrix[1, 1]
third_row = matrix[2, :]
print("Center Element:", center_element)
print("Third Row:", third_row)

# 4. Math
new_matrix = matrix * 2 + 10
print("Modified Matrix:\\n", new_matrix)
print("Sum of elements:", np.sum(new_matrix))</pre></div>
      </div>
      <div class="done-when">Your script runs without errors, produces the correct shapes, correct center element, and prints the sum of modified elements (180).</div>
      <div class="git-block">git add numpy_practice.py && git commit -m "day7: numpy matrix operations and slicing practice"</div>
    </div>
  </div>

  <!-- FLASHCARDS -->
  <h2 class="sh2">🃏 Day 7 Flashcards</h2>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is list * 2 behavior in Python?</div><div class="fc-back">Duplicates/repeats the elements, does not multiply!<br>[1, 2] * 2 = [1, 2, 1, 2]</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">What is a NumPy ndarray?</div><div class="fc-back">N-dimensional array. Elements must be of the same type<br>Supports fast vectorized math operations</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">Vectorized operations advantage?</div><div class="fc-back">Runs at C-speed without Python loops<br>e.g. arr * 2 multiplies every element in O(1) loop time</div></div></div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')"><div class="fc-inner"><div class="fc-front">How to check array shape &amp; dimensions?</div><div class="fc-back">arr.shape (tuple of sizes per axis)<br>arr.ndim (number of dimensions)</div></div></div>
  </div>"""

# Try to find target_d7_project in html
# We need to make sure we parse double escapes in regex or do string replacement
if "contact_book.py" in html:
    # Use exact match or simple search to find target block
    # Let's verify we can find it
    start_str = '<!-- WEEK 1 FINAL PROJECT -->'
    end_str = '  <!-- WEEK CHEAT SHEET -->'
    start_idx = html.find(start_str)
    end_idx = html.find(end_str)
    if start_idx != -1 and end_idx != -1:
        target_chunk = html[start_idx:end_idx]
        html = html.replace(target_chunk, replacement_d7_project + "\n\n")
        print("✅ Replaced Day 7 Contact Book with NumPy task and Day 7 Flashcards.")
    else:
        print("❌ Could not locate project block boundaries.")
else:
    print("❌ Day 7 project block not found.")

# Write back changes
with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print("🎉 Successfully patched week1.html!")
