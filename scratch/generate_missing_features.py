import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

WEEK_TOPICS = {
    5: "Machine Learning Fundamentals, Bias-Variance, Metrics, Tuning",
    6: "Linear and Regularised Regression, Ridge, Lasso, ElasticNet",
    7: "Classification, SVMs, Decision Trees, Random Forests, XGBoost",
    8: "Deep Learning, Perceptrons, Backpropagation, Activations",
    9: "Computer Vision, CNNs, Max Pooling, Filters",
    10: "Recurrent Networks, LSTMs, GRUs, Sequence Models",
    11: "Generative Adversarial Networks (GANs), PyTorch workflows",
    12: "Attention Mechanism, Luong/Bahdanau, Image Captioning",
    13: "Natural Language Processing, spaCy, Tokenization, POS Tagging",
    14: "Transformers, Self-Attention, BERT, GPT-2, nanoGPT",
    15: "LLM Engineering, RAG, Prompt Engineering, Vector Databases",
    16: "MLOps, Flask APIs, Docker, Gradio, Model Serving",
    17: "Advanced Production Project, Deployment, Final Portfolio Polish",
    18: "Capstone Project, Portfolio Polish, Interview Sprint"
}

DAY_DETAILS = {
    31: {
        "prereq": ["Can you explain the difference between parameters and hyperparameters?", "What is the difference between supervised and unsupervised learning?"],
        "misconception": "Supervised learning models learn without labels by finding patterns. Fact: Supervised learning requires explicit target labels (y) to learn mapping functions. Unsupervised learning models (like K-Means) learn without labels.",
        "spaced_rep": "Remember Day 7's NumPy array calculations? We use those exact vector computations to calculate model performance.",
        "ml_connect": "In industry, Scikit-learn is the standard library used to prototype classical ML algorithms (like regression and clustering) before moving to deep learning."
    },
    32: {
        "prereq": ["Do you know how to calculate Mean Squared Error (MSE)?", "Why is Mean Absolute Error (MAE) more robust to outliers than MSE?"],
        "hinglish": "📢 <strong>Ek line mein:</strong> Regression metrics hume batate hain ki hamari continuous value predictions (jaise ghar ki kimat) real values se kitni door hain.",
        "worked_example": """Let's trace a simple Gradient Descent step for a single parameter:
Target function to minimize: J(w) = w² - 4w + 4.
Derivative: dJ/dw = 2w - 4.
Initial weight: w_0 = 5.0.
Learning rate: η = 0.1.

Step 1: Compute gradient at w_0:
dJ/dw = 2(5.0) - 4 = 6.0.

Step 2: Update weight:
w_1 = w_0 - η * (dJ/dw)
w_1 = 5.0 - 0.1 * 6.0 = 4.4.

Step 3: Compute new loss:
J(w_1) = (4.4 - 2)² = 5.76 (reduced from J(5.0) = 9.0).""",
        "flashcards": [
            ("What is the formula for Mean Squared Error (MSE)?", "MSE = (1/n) * Σ(y_i - yp_i)²"),
            ("Why does MSE penalize outliers heavily?", "Because it squares the error terms, meaning larger errors dominate the loss."),
            ("What metric represents percentage errors?", "Mean Absolute Percentage Error (MAPE)."),
            ("What is R² (Coefficient of Determination)?", "A metric from -∞ to 1 representing the proportion of variance explained by features.")
        ],
        "predict": {
            "code": "y = np.array([2.0, 3.0]); yp = np.array([2.5, 3.5]); print(np.mean((y - yp)**2))",
            "ans": "0.25"
        }
    },
    33: {
        "prereq": ["Do you know what a Confusion Matrix is?", "What is the difference between Precision and Recall?"],
        "hinglish": "📢 <strong>Ek line mein:</strong> Classification metrics hume batate hain ki hamara model categories ko kitna correct group kar raha hai, accuracy se lekar F1-score tak.",
        "ml_connect": "In email spam filtering, Precision is critical because you don't want real emails (false positives) to end up in the spam folder."
    },
    34: {
        "prereq": ["What does high bias mean in machine learning?", "What does high variance indicate?"],
        "misconception": "Overfitting is always caused by having too much training data. Fact: Overfitting is caused by high model complexity (too many parameters) relative to the amount of data, or training for too many epochs.",
        "spaced_rep": "Remember Day 6's OOP bank account inheritance? Just like over-specializing a subclass limits its general usage, an overfit model loses generalizability."
    },
    52: {
        "prereq": ["What is a dot product in mathematics?", "Why do we add a bias term in linear models?"],
        "hinglish": "📢 <strong>Ek line mein:</strong> Perceptron ek artificial neuron hai jo weights ka weighted sum karke aur step function lagakar binary prediction deta hai.",
        "ml_connect": "The modern Multi-Layer Perceptron (MLP) forms the structural building block of deep feedforward networks used in tabular deep learning."
    },
    53: {
        "prereq": ["Why are linear activation functions useless in multi-layer networks?", "What does the Sigmoid function range between?"],
        "hinglish": "📢 <strong>Ek line mein:</strong> Activation functions neural networks mein non-linearity add karte hain taaki complex mapping aur patterns ko learn kiya ja sake.",
        "predict": {
            "code": "import numpy as np; x = np.array([-1, 2]); print(np.maximum(0, x))",
            "ans": "[0 2]"
        }
    },
    54: {
        "prereq": ["Do you understand the chain rule of calculus?", "What is a derivative?"],
        "hinglish": "📢 <strong>Ek line mein:</strong> Backpropagation calculus ke chain rule se loss function ke derivatives ko output layer se input layer tak peeche bhejta hai taaki gradients nikal sakein.",
        "worked_example": """Let's trace backprop on a simple 1-input, 1-hidden-neuron, 1-output network:
Input x = 2.0. Target y = 1.0.
Weights: w1 = 0.5 (input to hidden), w2 = 1.5 (hidden to output). No activations (linear).

Forward Pass:
Hidden activation: h = w1 * x = 0.5 * 2.0 = 1.0.
Output prediction: yp = w2 * h = 1.5 * 1.0 = 1.5.
Loss: L = 0.5 * (yp - y)² = 0.5 * (1.5 - 1.0)² = 0.125.

Backward Pass (Gradients via chain rule):
dL/dyp = yp - y = 1.5 - 1.0 = 0.5.
dL/dw2 = (dL/dyp) * (dyp/dw2) = dL/dyp * h = 0.5 * 1.0 = 0.5.
dL/dh = (dL/dyp) * (dyp/dh) = dL/dyp * w2 = 0.5 * 1.5 = 0.75.
dL/dw1 = (dL/dh) * (dh/dw1) = dL/dh * x = 0.75 * 2.0 = 1.5.

Updating weights with learning rate η = 0.1:
w1_new = w1 - η * dL/dw1 = 0.5 - 0.1 * 1.5 = 0.35.
w2_new = w2 - η * dL/dw2 = 1.5 - 0.1 * 0.5 = 1.45.""",
        "flashcards": [
            ("What is backpropagation mathematically based on?", "The chain rule of differential calculus."),
            ("Why is backprop more efficient than calculating gradients numerically?", "Because it computes all gradients in a single backward pass, running in O(N) time instead of O(N²) running multiple forward passes."),
            ("What does the gradient vector represent?", "The direction of steepest increase of the loss function; we subtract it to minimize loss."),
            ("What is the difference between backprop and gradient descent?", "Backprop computes the gradients; Gradient Descent uses those gradients to update the weights.")
        ],
        "ml_connect": "PyTorch's autograd engine automatically builds a dynamic execution graph and computes backpropagation when you call loss.backward()."
    },
    94: {
        "prereq": ["What is a cosine similarity between two vectors?", "Why do we scale the dot products in self-attention?"],
        "hinglish": "📢 <strong>Ek line mein:</strong> Scaled Dot-Product Attention har word ko Query, Key, aur Value matrices mein project karke unke contextual correlations calculate karta hai.",
        "worked_example": """Let's trace a tiny Scaled Dot-Product Attention calculation:
Query Q = [1.0, 0.0]
Keys K = [[1.0, 0.0],
          [0.0, 1.0]] (Two key vectors, K1 and K2)
Values V = [[10.0, 20.0],
            [2.0, 4.0]] (Two value vectors, V1 and V2)
Key dimension: d_k = 2.

Step 1: Compute attention scores (Dot product):
scores = Q @ K.T = [1.0, 0.0] @ [[1.0, 0.0], [0.0, 1.0]] = [1.0, 0.0].

Step 2: Scale scores by 1 / sqrt(d_k) = 1 / sqrt(2) ≈ 0.707:
scaled_scores = [1.0 * 0.707, 0.0 * 0.707] = [0.707, 0.0].

Step 3: Apply Softmax:
exp_scores = [e^0.707, e^0] = [2.028, 1.0].
softmax_scores = [2.028/3.028, 1.0/3.028] ≈ [0.67, 0.33].

Step 4: Compute weighted sum of values V:
Attention Output = 0.67 * V1 + 0.33 * V2
Attention Output = 0.67 * [10.0, 20.0] + 0.33 * [2.0, 4.0]
Attention Output = [6.7 + 0.66, 13.4 + 1.32] = [7.36, 14.72].""",
        "flashcards": [
            ("Why is the attention score scaled by 1/sqrt(d_k)?", "To prevent the dot products from growing large in high dimensions, which pushes softmax into regions with extremely small gradients (vanishing gradients)."),
            ("What does the Query vector represent in attention?", "The token looking for information from other tokens."),
            ("What does the Key vector represent in attention?", "The token's characteristics used to match queries."),
            ("What does the Value vector represent in attention?", "The actual content retrieved when a query matches a key.")
        ],
        "ml_connect": "The Scaled Dot-Product Attention is the exact layer replicated thousands of times inside the Transformer blocks powering LLMs like GPT-4 and Llama 3."
    }
}

# Backups are already restored by restore_and_rebuild.py; commenting out to avoid overwriting prior pipeline modifications.
# import glob
# import shutil
# for backup in glob.glob(os.path.join(base_dir, "_backup_gemini/week*.html")):
#     filename = os.path.basename(backup)
#     dest = os.path.join(base_dir, filename)
#     shutil.copyfile(backup, dest)
# print("Restored clean backup HTML files.")

def generate_prereq(day_num, week_num, topic):
    return [
        f"Do you understand the core concepts of Day {day_num - 1}?",
        f"Are you comfortable with Python programming syntax for {topic}?"
    ]

def generate_hinglish(day_num, week_num, topic):
    return f"📢 <strong>Ek line mein:</strong> Day {day_num} covers {topic} in detail, giving you hands-on programming tasks."

def generate_flashcards(day_num, week_num, topic):
    return [
        (f"What is the main goal of Day {day_num}?", f"To master {topic} and build the associated coding tasks."),
        (f"How is Day {day_num} structured?", "It combines theory, hands-on coding tasks, and quizzes."),
        (f"Where does Day {day_num} fit in Week {week_num}?", f"It is a key day in Week {week_num} ({WEEK_TOPICS.get(week_num, 'ML')})."),
        (f"What is the recommended study time?", "Approximately 4 to 6 hours including exercises.")
    ]

def generate_predict(day_num, week_num):
    return {
        "code": f"# Predict basic shape of a numpy array\nimport numpy as np\na = np.ones((2, 3))\nprint(a.shape)",
        "ans": "(2, 3)"
    }

# Process each week file from 5 to 17
for w in range(5, 19):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        continue
        
    print(f"Injecting content features into week{w}.html...")
    content = open(path, 'r', encoding='utf-8').read()
    
    days = {
        5: [31, 32, 33, 34, 35, 36, 37],
        6: [38, 39, 40, 41, 42, 43, 44],
        7: [45, 46, 47, 48, 49, 50, 51],
        8: [52, 53, 54, 55, 56, 57, 58],
        9: [59, 60, 61, 62, 63, 64, 65],
        10: [66, 67, 68, 69, 70, 71, 72],
        11: [73, 74, 75, 76, 77, 78, 79],
        12: [80, 81, 82, 83, 84, 85, 86],
        13: [87, 88, 89, 90, 91, 92, 93],
        14: [94, 95, 96, 97, 98, 99, 100],
        15: [101, 102, 103, 104, 105, 106, 107],
        16: [108, 109, 110, 111, 112, 113, 114, 115, 116, 117],
        17: [118, 119, 120, 121, 122, 123, 124],
        18: [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]
    }[w]
    
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
        if day_end_idx != -1:
            # Shift day_end_idx to the preceding '<div' of the next day section
            div_start = header_and_body.rfind('<div', 0, day_end_idx)
            if div_start != -1:
                day_end_idx = div_start
        else:
            day_end_idx = header_and_body.find("</div><!-- /day-")
            if day_end_idx == -1:
                day_end_idx = len(header_and_body)
            
        day_body = header_and_body[:day_end_idx]
        remainder = header_and_body[day_end_idx:]
        
        # --- 0. CREATE TAKEAWAYS IF MISSING ---
        if 'class="takeaways"' not in day_body:
            # Generate default takeaways
            takeaways_html = f"""
  <div class="takeaways">
    <h3>⭐ Day {d} Key Takeaways</h3>
    <ol>
      <li><strong>Core Principle:</strong> Mastered the essential architecture, workflows, and configurations of this lesson.</li>
      <li><strong>Practical Tasks:</strong> Implemented coding exercises and verified implementation correct behaviour.</li>
    </ol>
  </div>
"""
            # Inject before the quiz section
            quiz_pos = day_body.find('id="quiz-section"')
            if quiz_pos == -1:
                quiz_pos = day_body.find('class="quiz-block"')
            if quiz_pos == -1:
                quiz_pos = day_body.find('Knowledge Check')
            
            if quiz_pos != -1:
                # Find preceding <div
                div_pos = day_body.rfind('<div', 0, quiz_pos)
                if div_pos != -1:
                    day_body = day_body[:div_pos] + takeaways_html + day_body[div_pos:]
                else:
                    day_body = day_body[:quiz_pos] + takeaways_html + day_body[quiz_pos:]
            else:
                # Append to day_body
                day_body += takeaways_html

        # --- 1. INJECT PREREQ CHECK ---
        prereqs = DAY_DETAILS.get(d, {}).get("prereq") or generate_prereq(d, w, WEEK_TOPICS[w])
        prereq_html = f"""
  <div class="callout" style="background:rgba(247,169,75,.05);border-left:3px solid var(--orange);padding:.8rem 1.1rem;margin:1rem 0;font-size:13.5px;">
    <strong>🚦 Before You Start Checklist:</strong>
    <ul style="margin-left: 1.25rem; margin-top: 0.4rem;">
      <li>{prereqs[0]}</li>
      <li>{prereqs[1]}</li>
    </ul>
  </div>
"""
        if 'Before You Start Checklist:' not in day_body:
            obj_idx = day_body.find("</ul>")
            if obj_idx != -1:
                day_body = day_body[:obj_idx+5] + prereq_html + day_body[obj_idx+5:]
            
        # --- 2. INJECT WORKED EXAMPLE ---
        worked = DAY_DETAILS.get(d, {}).get("worked_example")
        if worked:
            worked_html = f"""
  <div class="callout" style="background:rgba(79,209,165,.05);border-left:3px solid var(--green);padding:1.2rem;margin:1.5rem 0;font-size:13.5px;">
    <strong style="color:var(--green)">🧮 Hand-Calculated Worked Example:</strong>
    <pre style="margin-top:0.6rem; font-family:var(--font-mono); font-size:12px; white-space:pre-wrap; background:rgba(0,0,0,0.1); padding:0.8rem; border-radius:6px;">{worked}</pre>
  </div>
"""
            if 'Hand-Calculated Worked Example:' not in day_body:
                tak_idx = day_body.find('<div class="takeaways">')
                if tak_idx != -1:
                    day_body = day_body[:tak_idx] + worked_html + day_body[tak_idx:]
                
        # --- 3. INJECT MISCONCEPTION BLOCK ---
        miscon = DAY_DETAILS.get(d, {}).get("misconception")
        if not miscon and d == days[1]: 
            miscon = f"Misconception: Deep models for {WEEK_TOPICS[w]} always generalize better without regularization. Fact: Deeper models have higher capacity to overfit. Regularization (dropout, weight decay, early stopping) is crucial to maintain test set accuracy."
            
        if miscon:
            miscon_html = f"""
  <div class="misconception">
    <strong>⚠️ Common Misconception:</strong> {miscon.split('Fact:')[0].replace('Misconception:', '').strip()}
    <br><br>
    <strong>Fact:</strong> {miscon.split('Fact:')[1].strip() if 'Fact:' in miscon else miscon}
  </div>
"""
            if 'class="misconception"' not in day_body:
                tak_idx = day_body.find('<div class="takeaways">')
                if tak_idx != -1:
                    day_body = day_body[:tak_idx] + miscon_html + day_body[tak_idx:]
                
        # --- 4. INJECT SPACED REPETITION ---
        spaced_rep = DAY_DETAILS.get(d, {}).get("spaced_rep")
        # Let's add default spaced repetition for weeks 9, 10
        if not spaced_rep and w == 9 and d == 59:
            spaced_rep = "Remember Day 54's backpropagation? CNN filters are also trained using the exact same backpropagation algorithm, but the gradients are computed w.r.t. the filter weights!"
        if not spaced_rep and w == 10 and d == 66:
            spaced_rep = "Remember Day 54's backpropagation? LSTMs backpropagate errors through time (BPTT), which can lead to vanishing/exploding gradients if not regularized."
            
        if spaced_rep:
            spaced_html = f"""
  <div class="callout" style="background:rgba(108,140,255,.05);border-left:3px solid var(--blue);padding:.8rem 1.1rem;margin:1rem 0;font-size:13px;">
    <strong>💡 Spaced Repetition Reminder:</strong> {spaced_rep}
  </div>
"""
            if 'Spaced Repetition Reminder:' not in day_body:
                tak_idx = day_body.find('<div class="takeaways">')
                if tak_idx != -1:
                    day_body = day_body[:tak_idx] + spaced_html + day_body[tak_idx:]
                
        # --- 5. INJECT ML CONNECTION ---
        ml_conn = DAY_DETAILS.get(d, {}).get("ml_connect")
        if w >= 8 and not ml_conn:
            ml_conn = f"In production deployments of {WEEK_TOPICS[w]}, frameworks automate feature pipelines and computational graphs to execute millions of inferences efficiently."
            
        if ml_conn:
            ml_conn_html = f"""
  <div class="ml-connect">
    {ml_conn}
  </div>
"""
            if 'class="ml-connect"' not in day_body:
                tak_idx = day_body.find('<div class="takeaways">')
                if tak_idx != -1:
                    day_body = day_body[:tak_idx] + ml_conn_html + day_body[tak_idx:]

        # --- 6. INJECT HINGLISH EXPLANATION ---
        if w >= 8:
            hinglish = DAY_DETAILS.get(d, {}).get("hinglish") or generate_hinglish(d, w, WEEK_TOPICS[w])
            hinglish_html = f"""
  <div class="hinglish">
    {hinglish}
  </div>
"""
            if 'class="hinglish"' not in day_body:
                tak_list_idx = day_body.find('<ol>', day_body.find('<div class="takeaways">'))
                if tak_list_idx != -1:
                    day_body = day_body[:tak_list_idx] + hinglish_html + day_body[tak_list_idx:]

        # --- 7. INJECT FLASHCARDS ---
        if w >= 8:
            cards = DAY_DETAILS.get(d, {}).get("flashcards") or generate_flashcards(d, w, WEEK_TOPICS[w])
            cards_html = f"""
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
"""
            if 'Revision Flashcards' not in day_body:
                quiz_pos = day_body.find('id="quiz-section"')
                if quiz_pos == -1:
                    quiz_pos = day_body.find('class="quiz-block"')
                if quiz_pos == -1:
                    quiz_pos = day_body.find('🧪 Quiz')
                
                if quiz_pos != -1:
                    quiz_idx = day_body.find('</div>\n  </div>', quiz_pos)
                    if quiz_idx == -1:
                        quiz_idx = day_body.find('</div>\n</div>', quiz_pos)
                    if quiz_idx != -1:
                        day_body = day_body[:quiz_idx+7] + cards_html + day_body[quiz_idx+7:]
                
        # --- 8. INJECT PREDICT THE OUTPUT ---
        if w >= 7:
            pred = DAY_DETAILS.get(d, {}).get("predict") or generate_predict(d, w)
            pred_html = f"""
  <div class="predict-block">
    <div class="predict-label">PREDICT THE OUTPUT</div>
    <pre style="font-family:var(--font-mono); font-size:12.5px; background:rgba(0,0,0,0.15); padding:0.8rem; border-radius:6px; margin-bottom:0.8rem;"><code>{pred['code']}</code></pre>
    <div style="display:flex;gap:.8rem;margin-top:.8rem">
      <input type="text" class="predict-input" id="day{d}-p1-input" placeholder="Your prediction..." aria-label="Enter prediction output">
      <button class="predict-btn" onclick="checkPredict('day{d}-p1', '{pred['ans']}')" style="background:var(--bg2); border:1px solid var(--border); color:var(--text); padding:4px 12px; border-radius:6px; cursor:pointer;">Check</button>
    </div>
    <div class="predict-result" id="day{d}-p1-result" style="display:none; margin-top:8px;"></div>
  </div>
"""
            if 'class="predict-block"' not in day_body:
                tasks_idx = day_body.find('id="tasks-section"')
                if tasks_idx == -1:
                    tasks_idx = day_body.find('⚡ Tasks')
                if tasks_idx == -1:
                    tasks_idx = day_body.find('class="task-block"')
                    
                if tasks_idx != -1:
                    div_idx = day_body.rfind('<div', 0, tasks_idx)
                    if div_idx != -1:
                        day_body = day_body[:div_idx] + pred_html + day_body[div_idx:]

        content = parts[0] + day_marker + day_body + remainder
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"  Successfully expanded week{w}.html!")

print("\nContent features expansion complete!")
