import glob
import re

for filepath in sorted(glob.glob('/Users/amananand/Downloads/SDE/ai:ml/week*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix pattern 1: <span class="[MPX]0 XP on completion&lt;/span&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class=" objectives"="">
    # This should be: <span class="meta-badge p">⚡ +150 XP</span>\n</div>\n</div>\n<div class="objectives">
    # Note: Sometimes it's +150 XP, +200 XP, +300 XP, etc. Let's see if we can identify the day's XP from the button or day header.
    # In week 3, days are:
    # Day 17: Earn 150 XP
    # Day 18: Earn 150 XP
    # Day 20: Earn 150 XP
    # Day 21: Earn 300 XP
    # In week 4:
    # Day 26: Earn 200 XP
    # Day 27: Earn 200 XP
    # Day 28: Earn 150 XP
    # In week 6:
    # Day 39: Earn 150 XP
    # Day 41: Earn 150 XP
    # Day 42: Earn 150 XP
    # Day 44: Earn 300 XP
    # In week 7:
    # Day 50: Earn 150 XP

    # Let's do regex replacement for the first pattern:
    # We can match: r'<span class="([MPX])0 XP on completion&lt;/span&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class=" objectives"=""'
    # Based on M0/P0/X0:
    # M0 -> +150 XP
    # P0 -> +200 XP
    # X0 -> +300 XP
    
    def repl_func(match):
        letter = match.group(1)
        xp = "150"
        if letter == "M":
            xp = "150"
        elif letter == "P":
            xp = "200"
        elif letter == "X":
            xp = "300"
        return f'<span class="meta-badge p">⚡ +{xp} XP</span>\n</div>\n</div>\n<div class="objectives">'

    content = re.sub(r'<span class="([MPX])0 XP on completion&lt;/span&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class=" objectives"=""\s*>', repl_func, content)
    content = re.sub(r'<span class="([MPX])0 XP on completion&lt;/span&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class=" objectives"=""\s*>\s*</span></div>', repl_func, content)

    # Let's fix week 4 day 22 specific pattern:
    # line 325: <span callout"="" class="M0 XP on completion&lt;/span&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class=" style="background:rgba(108,140,255,.03); border:1px dashed var(--blue); border-radius:var(--radius);
    # This should be: <span class="meta-badge p">⚡ +150 XP</span>\n</div>\n</div>\n<div class="callout" style="background:rgba(108,140,255,.03); border:1px dashed var(--blue); border-radius:var(--radius);
    content = re.sub(
        r'<span callout"="" class="M0 XP on completion&lt;/span&gt; &lt;/div&gt; &lt;/div&gt; &lt;div class="\s*style="background:rgba\(108,140,255,\.03\);\s*border:1px dashed var\(--blue\);\s*border-radius:var\(--radius\);\s*padding:1\.25rem;\s*margin-bottom:1\.8rem;">',
        '<span class="meta-badge p">⚡ +150 XP</span>\n</div>\n</div>\n<div class="callout" style="background:rgba(108,140,255,.03); border:1px dashed var(--blue); border-radius:var(--radius); padding:1.25rem; margin-bottom:1.8rem;">',
        content
    )

    # Let's fix other patterns:
    # week5.html line 1778: <span class="X0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">Capstone Project</span>\n</div>\n</div>\n<div class="objectives">\n<h3>
    content = re.sub(
        r'<span class="X0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">Capstone Project</span>\s*</div>\s*</div>\s*<div class="objectives">',
        '<span class="meta-badge p">⚡ +300 XP</span>\n<span class="meta-badge t">Capstone Project</span>\n</div>\n</div>\n<div class="objectives">',
        content
    )

    # week7.html line 1191: <span class="P0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">🏆 Kaggle — Titanic/House Prices</span>\n</div>\n</div>\n<div class="objectives">
    content = re.sub(
        r'<span class="P0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">🏆 Kaggle — Titanic/House Prices</span>\s*</div>\s*</div>\s*<div class="objectives">',
        '<span class="meta-badge p">⚡ +200 XP</span>\n<span class="meta-badge t">🏆 Kaggle — Titanic/House Prices</span>\n</div>\n</div>\n<div class="objectives">',
        content
    )

    # week7.html line 1459: <span class="P0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">📡 Telecom Churn Dataset</span>\n</div>\n</div>\n<div class="objectives">
    content = re.sub(
        r'<span class="P0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">📡 Telecom Churn Dataset</span>\s*</div>\s*</div>\s*<div class="objectives">',
        '<span class="meta-badge p">⚡ +200 XP</span>\n<span class="meta-badge t">📡 Telecom Churn Dataset</span>\n</div>\n</div>\n<div class="objectives">',
        content
    )

    # week7.html line 1953: <span class="X0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">💼 Portfolio Project</span>\n</div>\n</div>\n<div class="objectives">
    content = re.sub(
        r'<span class="X0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">💼 Portfolio Project</span>\s*</div>\s*</div>\s*<div class="objectives">',
        '<span class="meta-badge p">⚡ +300 XP</span>\n<span class="meta-badge t">💼 Portfolio Project</span>\n</div>\n</div>\n<div class="objectives">',
        content
    )

    # week8.html line 927: <span b"="" class="P0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="">🧮 Calculus + NumPy</span>\n</div>\n</div>\n<div class="objectives">
    content = re.sub(
        r'<span b"="" class="P0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="">🧮 Calculus \+ NumPy</span>\s*</div>\s*</div>\s*<div class="objectives">',
        '<span class="meta-badge p">⚡ +200 XP</span>\n<span class="meta-badge t">🧮 Calculus + NumPy</span>\n</div>\n</div>\n<div class="objectives">',
        content
    )

    # week8.html line 2142: <span class="X0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">🖼 CIFAR-10 + Flask</span>\n<span class="meta-badge b">📂 Portfolio project</span>\n</div>\n</div>\n<div class="objectives"
    content = re.sub(
        r'<span class="X0 XP on completion&lt;/span&gt; &lt;span class=" meta-badge="" t"="">🖼 CIFAR-10 \+ Flask</span>\s*<span class="meta-badge b">📂 Portfolio project</span>\s*</div>\s*</div>\s*<div class="objectives">',
        '<span class="meta-badge p">⚡ +300 XP</span>\n<span class="meta-badge t">🖼 CIFAR-10 + Flask</span>\n<span class="meta-badge b">📂 Portfolio project</span>\n</div>\n</div>\n<div class="objectives">',
        content
    )

    # Clean up closing </span></div> if any are lingering from the broken patterns:
    # E.g. </ul>\n</span></div>\n<div id=...
    content = re.sub(r'</ul>\s*</span></div>\s*<div id=', '</ul>\n</div>\n<div id=', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {filepath.split("/")[-1]}')
