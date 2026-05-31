import re
import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# 1. Verify week5.html Day 32 Worked Example and Prereq check
w5_path = os.path.join(base_dir, "week5.html")
if os.path.exists(w5_path):
    content = open(w5_path, 'r', encoding='utf-8').read()
    print("=== week5.html (ML Fundamentals) ===")
    print("Prereq check present:", "Before You Start Checklist" in content)
    print("Worked example present:", "Hand-Calculated Worked Example" in content)
    # Print a tiny snippet of the worked example to check it
    match = re.search(r"Hand-Calculated Worked Example.*?</pre>", content, re.DOTALL)
    if match:
        print("Example Snippet:\n", match.group(0)[:300])

# 2. Verify week8.html Day 54 (Backpropagation)
w8_path = os.path.join(base_dir, "week8.html")
if os.path.exists(w8_path):
    content = open(w8_path, 'r', encoding='utf-8').read()
    print("\n=== week8.html (Deep Learning) ===")
    print("Prereq check present:", "Before You Start Checklist" in content)
    print("Worked example present:", "Hand-Calculated Worked Example" in content)
    print("Hinglish summaries present:", "Ek line mein:" in content)
    print("ML connection present:", "Autograd" in content or "autograd" in content)
    print("Flashcards present:", "Revision Flashcards" in content)
    print("Predict the output present:", "PREDICT THE OUTPUT" in content)

# 3. Verify week14.html Day 94 (Attention Math)
w14_path = os.path.join(base_dir, "week14.html")
if os.path.exists(w14_path):
    content = open(w14_path, 'r', encoding='utf-8').read()
    print("\n=== week14.html (Transformers) ===")
    print("Attention worked example present:", "Q = [1.0, 0.0]" in content)
    print("Flashcards present:", "Query vector represent in attention" in content)
    print("ML connection present:", "GPT-4" in content)
