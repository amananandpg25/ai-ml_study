import os

path = "/Users/amananand/Downloads/SDE/ai:ml/week2.html"
html = open(path, 'r', encoding='utf-8').read()

# 1. Day 8 Slicing Caution injection
target_d8_end = """  <div class="ml-connect">cut() and qcut() are core feature engineering tools. Age groups, salary bands, and risk tiers are all created this way before feeding data into ML models.</div>
  </div><!-- /theory -->"""

replacement_d8_end = """  <div class="ml-connect">cut() and qcut() are core feature engineering tools. Age groups, salary bands, and risk tiers are all created this way before feeding data into ML models.</div>

  <h3 class="sh3">9. Slicing Caution: SettingWithCopyWarning &amp; .copy()</h3>
  <p>
    When you slice a subset of a DataFrame (e.g. <code>subset = df[df["salary"] > 55000]</code>) and then try to modify it (e.g. <code>subset["bonus"] = 100</code>), Pandas will frequently throw a <code>SettingWithCopyWarning</code>. 
    This happens because Pandas is unsure whether your slice is a <strong>View</strong> (points to the original data) or a <strong>Copy</strong> (a separate object in memory). Modifying a view modifies the original, while modifying a copy does not.
  </p>
  <div class="misconception">
    <strong>⚠️ SettingWithCopyWarning is NOT a crash:</strong>
    It is a warning to prevent you from writing code that might fail to update the original DataFrame or update it accidentally.
  </div>
  <p>
    <strong>How to fix it:</strong> 
    If you want a completely independent copy to modify safely, explicitly use <code>.copy()</code>:
  </p>
  <div class="cb">
    <div class="cb-head"><span class="cb-lang">python — safe_copy.py</span><button class="copy-btn" onclick="copyCode(this)">copy</button><button class="run-btn" onclick="runCode(this)" style="margin-left: 4px;">Run</button></div>
    <pre><span class="cm"># Safe way to modify a sliced subset without warnings</span>
high_earners = df[df[<span class="str">"salary"</span>] &gt; <span class="num">55000</span>].copy()
high_earners[<span class="str">"bonus"</span>] = high_earners[<span class="str">"salary"</span>] * <span class="num">0.1</span>  <span class="cm"># Safe! No warning.</span>

<span class="cm"># If you WANT to modify the original DataFrame, use .loc:</span>
df.loc[df[<span class="str">"salary"</span>] &gt; <span class="num">55000</span>, <span class="str">"bonus"</span>] = df[<span class="str">"salary"</span>] * <span class="num">0.1</span>  <span class="cm"># Safe and direct!</span></pre>
  </div>
  </div><!-- /theory -->"""

# 2. Day 9 inplace replacements
target_d9_inplace1 = """<span class="cm"># Fill nulls with a constant</span>
df[<span class="str">"age"</span>].fillna(<span class="num">0</span>, inplace=<span class="kw">True</span>)      <span class="cm"># not ideal — zeros skew stats</span>

<span class="cm"># Fill with mean (better for numeric data)</span>
mean_score = df[<span class="str">"score"</span>].mean()
df[<span class="str">"score"</span>].fillna(mean_score, inplace=<span class="kw">True</span>)  <span class="cm"># fills 87.5</span>

<span class="cm"># Fill with forward fill (use previous row's value)</span>
df[<span class="str">"score"</span>].ffill(inplace=<span class="kw">True</span>)   <span class="cm"># useful for time series</span>"""

replacement_d9_inplace1 = """<span class="cm"># Fill nulls with a constant</span>
df[<span class="str">"age"</span>] = df[<span class="str">"age"</span>].fillna(<span class="num">0</span>)      <span class="cm"># Reassignment is best practice</span>

<span class="cm"># Fill with mean (better for numeric data)</span>
mean_score = df[<span class="str">"score"</span>].mean()
df[<span class="str">"score"</span>] = df[<span class="str">"score"</span>].fillna(mean_score)  <span class="cm"># fills 87.5</span>

<span class="cm"># Fill with forward fill (use previous row's value)</span>
df[<span class="str">"score"</span>] = df[<span class="str">"score"</span>].ffill()   <span class="cm"># useful for time series</span>"""

target_d9_inplace2 = """<span class="cm"># Remove duplicate rows</span>
df.drop_duplicates(inplace=<span class="kw">True</span>)               <span class="cm"># removes identical rows</span>
df.drop_duplicates(subset=[<span class="str">"name"</span>], keep=<span class="str">"first"</span>)  <span class="cm"># dedupe by name</span>

<span class="cm"># Rename columns</span>
df.rename(columns={<span class="str">"name"</span>: <span class="str">"student_name"</span>, <span class="str">"age"</span>: <span class="str">"student_age"</span>}, inplace=<span class="kw">True</span>)"""

replacement_d9_inplace2 = """<span class="cm"># Remove duplicate rows</span>
df = df.drop_duplicates()                      <span class="cm"># Reassignment avoids inplace</span>
df = df.drop_duplicates(subset=[<span class="str">"name"</span>], keep=<span class="str">"first"</span>)  <span class="cm"># dedupe by name</span>

<span class="cm"># Rename columns</span>
df = df.rename(columns={<span class="str">"name"</span>: <span class="str">"student_name"</span>, <span class="str">"age"</span>: <span class="str">"student_age"</span>})"""

# 3. Add inplace misconception block on Day 9
target_d9_misconception_spot = """  <h3 class="sh3">3. apply() and map() — Transforming Data</h3>"""
replacement_d9_misconception_spot = """  <div class="misconception">
    <strong>⚠️ Deprecation Warning: Avoid <code>inplace=True</code></strong><br>
    Many Pandas methods accept <code>inplace=True</code>. However, in modern Pandas (2.0+), <strong>inplace is discouraged and slated for eventual deprecation</strong>. Under the hood, it does not actually save memory (it still copies the data), it prevents method chaining, and it can cause silent bugs. Always prefer assignment: <code>df = df.method()</code>.
  </div>

  <h3 class="sh3">3. apply() and map() — Transforming Data</h3>"""

# 4. Day 12 set_index inplace replacement
target_d12_inplace = """df.set_index(<span class="str">"date"</span>, inplace=<span class="kw">True</span>)"""
replacement_d12_inplace = """df = df.set_index(<span class="str">"date"</span>)"""

# 5. Day 14 Titanic project cleaning inplace replacement
target_d14_inplace = """df[<span class="str">"Age"</span>].fillna(df[<span class="str">"Age"</span>].median(), inplace=<span class="kw">True</span>)   <span class="cm"># median: robust to outliers</span>
df.drop(columns=[<span class="str">"Cabin"</span>], inplace=<span class="kw">True</span>)          <span class="cm"># 77% null — unusable</span>
df.drop_duplicates(inplace=<span class="kw">True</span>)
df[<span class="str">"Embarked"</span>].fillna(df[<span class="str">"Embarked"</span>].mode()[<span class="num">0</span>], inplace=<span class="kw">True</span>)"""

replacement_d14_inplace = """df[<span class="str">"Age"</span>] = df[<span class="str">"Age"</span>].fillna(df[<span class="str">"Age"</span>].median())   <span class="cm"># median: robust to outliers</span>
df = df.drop(columns=[<span class="str">"Cabin"</span>])          <span class="cm"># 77% null — unusable</span>
df = df.drop_duplicates()
df[<span class="str">"Embarked"</span>] = df[<span class="str">"Embarked"</span>].fillna(df[<span class="str">"Embarked"</span>].mode()[<span class="num">0</span>])"""

# Apply modifications
modifications = [
    (target_d8_end, replacement_d8_end, "Day 8 Slicing Caution"),
    (target_d9_inplace1, replacement_d9_inplace1, "Day 9 fillna/ffill inplace"),
    (target_d9_inplace2, replacement_d9_inplace2, "Day 9 drop_duplicates/rename inplace"),
    (replacement_d9_inplace2, replacement_d9_inplace2 + "\n", "Verifying replacement is correct"), # dummy to ensure ordering
    (target_d9_misconception_spot, replacement_d9_misconception_spot, "Day 9 inplace Misconception"),
    (target_d12_inplace, replacement_d12_inplace, "Day 12 set_index inplace"),
    (target_d14_inplace, replacement_d14_inplace, "Day 14 Titanic inplace")
]

all_ok = True
for target, replacement, label in modifications:
    if target in html:
        html = html.replace(target, replacement)
        print(f"✅ Applied: {label}")
    else:
        # Check if already applied
        if replacement in html:
            print(f"ℹ️ Already applied: {label}")
        else:
            print(f"❌ Target not found: {label}")
            all_ok = False

if all_ok:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("🎉 Successfully patched week2.html!")
else:
    print("⚠️ Some targets were not found. Patch aborted.")
