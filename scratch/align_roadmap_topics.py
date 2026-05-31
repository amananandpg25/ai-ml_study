import os

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
roadmap_path = os.path.join(base_dir, "roadmap.html")

content = open(roadmap_path, 'r', encoding='utf-8').read()

# 1. Locate Week 6 and replace day cards grid
# Match: <div class="days-grid"> ... </div> under id="m2w6"
# Let's locate the entire block of days-grid under m2w6
start_w6 = content.find('<div id="m2w6"')
if start_w6 == -1:
    print("Error: m2w6 not found")
    exit(1)

grid_w6_start = content.find('<div class="days-grid">', start_w6)
grid_w6_end = content.find('</div>', content.find('</div>', content.find('</div>', grid_w6_start) + 1) + 1)
# Wait, let's find the closing tag of days-grid precisely by matching balanced tags or looking for end of week-content.
# Since it's a fixed template, let's search for the exact HTML string from `<div class="days-grid">` to `</div>\n      </div>\n    </div>\n  </div>`
# Or let's use the unique content strings of Week 6.

old_w6_content = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 38</div>
            <div class="day-title">Logistic Regression — Theory</div>
            <ul class="day-list">
              <li>Sigmoid function: maps any value to 0–1</li>
              <li>Decision boundary, threshold tuning</li>
              <li>Log loss / Binary cross-entropy</li>
              <li>Multinomial logistic regression (softmax)</li>
              <li>Implement binary logistic regression from scratch</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 39</div>
            <div class="day-title">Logistic Regression — Applications</div>
            <ul class="day-list">
              <li>sklearn LogisticRegression with regularisation (C parameter)</li>
              <li>Multiclass classification (OvR, OvO)</li>
              <li>Credit risk / disease prediction project</li>
              <li>ROC curve and AUC analysis</li>
              <li>Interpret model coefficients (feature importance)</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 40</div>
            <div class="day-title">Naive Bayes + KNN</div>
            <ul class="day-list">
              <li>Naive Bayes: Bayes theorem applied to classification</li>
              <li>GaussianNB, MultinomialNB (for text)</li>
              <li>K-Nearest Neighbours: vote by k nearest points</li>
              <li>Choosing optimal K with elbow method</li>
              <li>Practice: Spam email classification with Naive Bayes</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 41–44</div>
            <div class="day-title">Project: Disease Prediction App</div>
            <ul class="day-list">
              <li>Dataset: Pima Indians Diabetes (Kaggle)</li>
              <li>Full pipeline: EDA → preprocessing → Logistic Regression</li>
              <li>Compare: Logistic Reg vs Naive Bayes vs KNN</li>
              <li>Evaluate with precision, recall, F1, ROC-AUC</li>
              <li>Simple Flask API (return prediction as JSON)</li>
              <li>Push to GitHub with full README</li>
            </ul>
            <div class="day-hours">⏱ 5–6 hrs/day</div>
          </div>
        </div>"""

new_w6_content = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 38</div>
            <div class="day-title">Linear Regression — Deep Dive</div>
            <ul class="day-list">
              <li>OLS Equation derivation & residual analysis</li>
              <li>Gradient descent optimization assumptions check</li>
              <li>Practice: Simple linear regression from scratch in Python</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 39</div>
            <div class="day-title">Polynomial Regression & Bias-Variance</div>
            <ul class="day-list">
              <li>Non-linear relations & polynomial feature mapping</li>
              <li>Overfitting detection using train/val curves</li>
              <li>Practice: Fitting non-linear functions & degree selection</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 40</div>
            <div class="day-title">Ridge & Lasso Regularisation (L1/L2)</div>
            <ul class="day-list">
              <li>Shrinkage penalties (L1 Lasso vs L2 Ridge)</li>
              <li>Feature selection properties of Lasso</li>
              <li>Practice: House valuation regularisation tuning</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 41–44</div>
            <div class="day-title">Cross-Validation & Capstone Project</div>
            <ul class="day-list">
              <li>ElasticNet compound regularization</li>
              <li>K-Fold cross-validation & regression metrics</li>
              <li>Capstone: House Price Predictor with scikit-learn</li>
              <li>Simple Flask API deployment with model serialization</li>
            </ul>
            <div class="day-hours">⏱ 5–6 hrs/day</div>
          </div>
        </div>"""

content = content.replace(old_w6_content, new_w6_content)

# 2. Locate Week 8 and replace day cards grid + milestone box
old_w8_content = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 52</div>
            <div class="day-title">Perceptron & Multi-Layer Networks</div>
            <ul class="day-list">
              <li>Algorithm: init centroids → assign → update → repeat</li>
              <li>Choosing K: Elbow method, Silhouette score</li>
              <li>K-Means++ for better initialisation</li>
              <li>Limitations: spherical clusters, sensitive to outliers</li>
              <li>Practice: Customer segmentation project</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 54–55</div>
            <div class="day-title">Other Clustering + Association Rules</div>
            <ul class="day-list">
              <li>Hierarchical clustering (dendrograms)</li>
              <li>DBSCAN for arbitrary shapes + noise</li>
              <li>Association rule mining: Apriori algorithm</li>
              <li>Support, Confidence, Lift metrics</li>
              <li>Practice: Market basket analysis (grocery dataset)</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 56–57</div>
            <div class="day-title">Reinforcement Learning Fundamentals</div>
            <ul class="day-list">
              <li>Agent, Environment, State, Action, Reward</li>
              <li>Markov Decision Process (MDP)</li>
              <li>Q-Learning algorithm (tabular)</li>
              <li>OpenAI Gym basics</li>
              <li>Practice: CartPole with Q-learning</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 58–60</div>
            <div class="day-title">Month 2 Capstone: ML Portfolio Project</div>
            <ul class="day-list">
              <li>Project: End-to-end ML pipeline on real problem</li>
              <li>Options: Stock prediction, movie recommendation, fraud detection</li>
              <li>Include: EDA, preprocessing, 3+ models, evaluation, Flask API</li>
              <li>Deploy on Render.com (free tier)</li>
              <li>Full README with methodology and results</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>
        <div class="milestone">
          <div class="milestone-icon">🎉</div>
          <div class="milestone-content">
            <h4>Month 2 Complete — Machine Learning Mastered!</h4>
            <div class="milestone-checks">
              <span class="check-item">✓ All ML algorithms</span>
              <span class="check-item">✓ Precision/Recall/F1 mastered</span>
              <span class="check-item">✓ Bias-Variance understood</span>
              <span class="check-item">✓ K-Means clustering</span>
              <span class="check-item">✓ RL basics</span>
              <span class="check-item">✓ 3+ ML projects deployed</span>
              <span class="check-item">✓ First Kaggle submission</span>
            </div>
          </div>
        </div>"""

new_w8_content = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 52</div>
            <div class="day-title">Perceptron & Activation Functions</div>
            <ul class="day-list">
              <li>Single-layer perceptron threshold updates</li>
              <li>Activations: Sigmoid, Tanh, ReLU, Softmax</li>
              <li>Vanishing gradients & non-linear mappings</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 53-54</div>
            <div class="day-title">Backpropagation & Autograd Tensors</div>
            <ul class="day-list">
              <li>Math: Chain rule & weight gradient updates</li>
              <li>PyTorch tensors, dynamic computation graphs, autograd</li>
              <li>Accelerating calculations with CUDA GPUs</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 55-57</div>
            <div class="day-title">PyTorch Multi-Layer Perceptron (MLP)</div>
            <ul class="day-list">
              <li>Building an MLP using nn.Module & nn.Sequential</li>
              <li>Loss functions & optimizers (SGD, Adam, learning rates)</li>
              <li>Regularisation: Dropout, weight decay, early stopping</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m2)">
            <div class="day-label">DAY 58</div>
            <div class="day-title">Capstone NN: MNIST Digit Classification</div>
            <ul class="day-list">
              <li>Digit classifier pipeline: load, scale, model, train</li>
              <li>Evaluate accuracy, draw confusion matrices</li>
              <li>Deploy digit recognition spaces on GitHub portfolios</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
        </div>
        <div class="milestone">
          <div class="milestone-icon">🎉</div>
          <div class="milestone-content">
            <h4>Month 2 Complete — Machine Learning Mastered!</h4>
            <div class="milestone-checks">
              <span class="check-item">✓ All classical ML algorithms</span>
              <span class="check-item">✓ Precision/Recall/F1 classification metrics</span>
              <span class="check-item">✓ Regularisation (Ridge/Lasso/ElasticNet)</span>
              <span class="check-item">✓ PyTorch MLP & autograd networks</span>
              <span class="check-item">✓ Backpropagation calculus</span>
              <span class="check-item">✓ Digit recognition Capstone</span>
              <span class="check-item">✓ ML APIs deployed</span>
            </div>
          </div>
        </div>"""

content = content.replace(old_w8_content, new_w8_content)

# Save changes
with open(roadmap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("roadmap.html Day Cards updated successfully!")
