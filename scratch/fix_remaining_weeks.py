import os

# ── 1. Fix week9.html ─────────────────────────────────────────────────────────
path_w9 = "/Users/amananand/Downloads/SDE/ai:ml/week9.html"
if os.path.exists(path_w9):
    html = open(path_w9, 'r', encoding='utf-8').read()
    html = html.replace('https://medium.com/@chengweiwei/cutmix-mixup-and-cutout-augmentation-893f2b6e3e22',
                        'https://keras.io/examples/vision/mixup/')
    with open(path_w9, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Patched week9.html")

# ── 2. Fix week10.html ────────────────────────────────────────────────────────
path_w10 = "/Users/amananand/Downloads/SDE/ai:ml/week10.html"
if os.path.exists(path_w10):
    html = open(path_w10, 'r', encoding='utf-8').read()
    html = html.replace('http://r2rt.com/recurrent-neural-networks-in-tensorflow-i.html',
                        'https://colah.github.io/posts/2015-08-Understanding-LSTMs/')
    html = html.replace('https://www.analyticsvidhya.com/blog/2021/06/text-preprocessing-in-nlp-with-python/',
                        'https://realpython.com/natural-language-processing-spacy-python/')
    with open(path_w10, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Patched week10.html")

# ── 3. Fix week11.html ────────────────────────────────────────────────────────
path_w11 = "/Users/amananand/Downloads/SDE/ai:ml/week11.html"
if os.path.exists(path_w11):
    html = open(path_w11, 'r', encoding='utf-8').read()
    html = html.replace('https://towardsdatascience.com/understanding-generative-adversarial-networks-gans-cd6e4651a29',
                        'https://developers.google.com/machine-learning/gan')
    with open(path_w11, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Patched week11.html")

# ── 4. Fix week12.html ────────────────────────────────────────────────────────
path_w12 = "/Users/amananand/Downloads/SDE/ai:ml/week12.html"
if os.path.exists(path_w12):
    html = open(path_w12, 'r', encoding='utf-8').read()
    html = html.replace('https://towardsdatascience.com/how-to-sample-from-language-models-682b686b245e',
                        'https://huggingface.co/blog/how-to-generate')
    with open(path_w12, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Patched week12.html")

# ── 5. Fix week13.html ────────────────────────────────────────────────────────
path_w13 = "/Users/amananand/Downloads/SDE/ai:ml/week13.html"
if os.path.exists(path_w13):
    html = open(path_w13, 'r', encoding='utf-8').read()
    html = html.replace('https://towardsdatascience.com/tf-idf-explained-and-implemented-with-python-39649541f282',
                        'https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction')
    html = html.replace('https://towardsdatascience.com/conditional-random-fields-explained-e5812c236a85',
                        'https://www.geeksforgeeks.org/conditional-random-fields-crfs-in-nlp/')
    html = html.replace('https://towardsdatascience.com/text-summarization-using-tf-idf-e3db91ecbff9',
                        'https://machinelearningmastery.com/document-summarization-in-python-with-tfidf/')
    with open(path_w13, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Patched week13.html")

# ── 6. Fix week16.html ────────────────────────────────────────────────────────
path_w16 = "/Users/amananand/Downloads/SDE/ai:ml/week16.html"
if os.path.exists(path_w16):
    html = open(path_w16, 'r', encoding='utf-8').read()
    html = html.replace('<div class="quiz-feedback wrong-fb" id="q114-1-wrong">❌ Incorrect.</div>',
                        '<div class="quiz-feedback wrong-fb" id="q114-1-wrong">❌ Incorrect. The Vercel AI SDK provides a unified, production-ready API for streaming text and structured outputs, handling multiple LLM providers (OpenAI, Anthropic, Cohere, etc.) seamlessly in the frontend.</div>')
    html = html.replace('<div class="quiz-feedback wrong-fb" id="q115-1-wrong">❌ Incorrect.</div>',
                        '<div class="quiz-feedback wrong-fb" id="q115-1-wrong">❌ Incorrect. LangSmith is designed for production LLM observability, tracing, debugging, and evaluations, not just API key management.</div>')
    html = html.replace('<div class="quiz-feedback wrong-fb" id="q116-1-wrong">❌ Incorrect.</div>',
                        '<div class="quiz-feedback wrong-fb" id="q116-1-wrong">❌ Incorrect. Faithfulness evaluates grounding: whether the generated answer is strictly based on the retrieved context (no hallucinations).</div>')
    with open(path_w16, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Patched week16.html")

# ── 7. Fix week7.html ─────────────────────────────────────────────────────────
path_w7 = "/Users/amananand/Downloads/SDE/ai:ml/week7.html"
if os.path.exists(path_w7):
    html = open(path_w7, 'r', encoding='utf-8').read()
    
    # sparse_output warning
    html = html.replace("sparse_output=False", "sparse_output=False)  # requires sklearn >= 1.2")
    # Restore the duplicate parenthesis that might occur if we search for the whole line:
    html = open(path_w7, 'r', encoding='utf-8').read()
    html = html.replace("sparse_output=False", "sparse_output=False)  # requires sklearn >= 1.2")
    # Double check to fix extra closing parenthesis that this simple replace introduces:
    # the original was: sparse_output=False))
    # replacing sparse_output=False with sparse_output=False) # requires sklearn >= 1.2
    # makes it: sparse_output=False) # requires sklearn >= 1.2))
    # Let's target the exact line:
    html = open(path_w7, 'r', encoding='utf-8').read()
    html = html.replace("('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))",
                        "('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))  # requires sklearn >= 1.2")

    # Replace the 27 placeholder feedbacks by ID
    replacements = {
        "q45-4": (
            "✅ Correct! Support vectors are the data points closest to the decision boundary. They define the margin and dictate the orientation of the separating hyperplane.",
            "❌ Incorrect. Support vectors are specifically the data points lying on the margin boundaries. They are the only points that determine the SVM decision boundary."
        ),
        "q45-5": (
            "✅ Correct! A large gamma value means the similarity radius of support vectors is small. This causes the model to fit tightly around individual points, leading to high variance (overfitting).",
            "❌ Incorrect. Gamma defines how far the influence of a single training example reaches. A large gamma restricts influence to a small radius, leading to overfitting."
        ),
        "q46-8": (
            "✅ Correct! Gini Impurity decreases after splitting. The weighted average impurity of children is lower than the parent node impurity, showing information gain.",
            "❌ Incorrect. A split is chosen specifically to reduce impurity (increase homogeneity). Calculate the weighted Gini impurity of child nodes to see the reduction."
        ),
        "q46-9": (
            "✅ Correct! max_depth limits the maximum number of splits from root to leaf, directly preventing the tree from growing overly complex and memorizing training noise (overfitting).",
            "❌ Incorrect. max_depth limits tree vertical growth. Lower depth forces generalization; deeper trees overfit."
        ),
        "q46-10": (
            "✅ Correct! Entropy uses logarithms (base 2), which is computationally more expensive than Gini's simple squaring calculations, but it can be more sensitive to class distribution changes.",
            "❌ Incorrect. Entropy calculations involve log2, making them slightly slower than Gini's simple arithmetic operations."
        ),
        "q47-13": (
            "✅ Correct! Random Forest reduces variance by training multiple trees on bootstrap samples (bagging) and averaging their predictions, which smooths out individual tree overfitting.",
            "❌ Incorrect. Random Forest combines multiple high-variance trees. By bagging (bootstrap aggregation), it averages predictions and drastically reduces overall variance."
        ),
        "q47-14": (
            "✅ Correct! The default value for classification is sqrt(d) where d is the number of features. This ensures tree diversity by randomly selecting subsets of features at each split.",
            "❌ Incorrect. For classification tasks, scikit-learn defaults max_features to the square root of the total number of features."
        ),
        "q47-15": (
            "✅ Correct! Random Forest trains trees in parallel, whereas Gradient Boosting trains them sequentially. However, Gradient Boosting typically achieves higher accuracy if tuned well.",
            "❌ Incorrect. Random Forest can be trained in parallel because trees are independent. Gradient Boosting trees are dependent (sequential) and cannot be trained in parallel."
        ),
        "q48-17": (
            "✅ Correct! XGBoost uses regularized objective functions and an approximate split-finding algorithm (histogram-based) that handles sparse data and enables parallel processing.",
            "❌ Incorrect. XGBoost achieves high speed through parallel processing, cache-aware access patterns, and histogram-based split-finding algorithms."
        ),
        "q48-18": (
            "✅ Correct! subsample=0.8 means XGBoost randomly samples 80% of the training data prior to growing each tree, introducing bagging-like regularization to prevent overfitting.",
            "❌ Incorrect. Subsampling columns is colsample_bytree. subsample=0.8 randomly selects 80% of training instances (rows) for each boosting iteration."
        ),
        "q48-19": (
            "✅ Correct! reg_lambda corresponds to L2 regularization on leaf weights, penalizing large weights to prevent extreme values and reduce model variance.",
            "❌ Incorrect. reg_lambda represents L2 regularization on the leaf node weights, which penalizes large predictions to simplify the model."
        ),
        "q48-20": (
            "✅ Correct! Early stopping (e.g., using early_stopping_rounds) halts training when validation loss stops improving, saving computation and preventing overfitting.",
            "❌ Incorrect. If training loss drops but validation loss remains flat, the model is overfitting. Early stopping halts training once validation performance plateaus."
        ),
        "q49-21": (
            "✅ Correct! A churn rate of 27% represents class imbalance (73% non-churn, 27% churn). Standard accuracy is misleading; you must evaluate precision, recall, and AUC.",
            "❌ Incorrect. Class distribution is the most important check. With imbalanced classes (27% churn), standard classification accuracy metrics will be highly misleading."
        ),
        "q49-22": (
            "✅ Correct! Ratio features (total charges divided by tenure) are a type of interaction or domain-specific numerical feature that captures rate of spend.",
            "❌ Incorrect. Dividing total charges by tenure creates a numerical ratio feature (representing average spend per month)."
        ),
        "q49-23": (
            "✅ Correct! Label encoding contracts implies an ordinal order (Two year > One year > Month-to-month), which is mathematically valid since they represent duration.",
            "❌ Incorrect. Label encoding contract durations is appropriate here because there is a logical order of length (Month-to-month < One year < Two year)."
        ),
        "q49-24": (
            "✅ Correct! One-Hot encoding converts categorical columns into multiple binary indicators, making them compatible with linear models that require numerical inputs.",
            "❌ Incorrect. pd.get_dummies() performs One-Hot Encoding on nominal categories to create binary columns."
        ),
        "q49-25": (
            "✅ Correct! Saving to a binary format like pickle or parquet preserves column datatypes (e.g. category vs object), which text-based CSV files lose.",
            "❌ Incorrect. Pickling or saving to Parquet preserves exact Pandas datatypes, preventing the need to re-parse columns when reloading."
        ),
        "q50-26": (
            "✅ Correct! XGBoost/LightGBM with scale_pos_weight or SMOTE are the most effective ensemble techniques for handling imbalanced tabular classifications.",
            "❌ Incorrect. Gradient boosted trees (XGBoost/LightGBM) typically outperform random forests and SVMs on imbalanced tabular datasets."
        ),
        "q50-27": (
            "✅ Correct! SHAP plots show feature importance and direction: a month-to-month contract is highly correlated with positive churn predictions.",
            "❌ Incorrect. High positive SHAP values indicate that the presence of month-to-month contracts directly increases the probability of churn."
        ),
        "q50-28": (
            "✅ Correct! Trade off metrics against compute cost: if XGBoost (AUC=0.91) is too slow or complex for your latency limits, Random Forest (AUC=0.89) is a strong alternative.",
            "❌ Incorrect. Model selection must balance performance improvements against latency, compute costs, and explainability requirements."
        ),
        "q50-29": (
            "✅ Correct! SHAP force plots show how individual feature values act as forces to push the model prediction away from the base value (average prediction).",
            "❌ Incorrect. A force plot visualizes how features pull the prediction higher or lower for a single, specific prediction sample."
        ),
        "q50-30": (
            "✅ Correct! A high false positive rate (40%) means many loyal customers are falsely flagged as churn risks, which could lead to wasted marketing budgets on retention offers.",
            "❌ Incorrect. Flagging 40% of non-churners represents a high False Positive rate, causing unnecessary outreach and budget waste."
        ),
        "q51-31": (
            "✅ Correct! request.get_json() parses the incoming JSON request body and returns a Python dictionary for easy key-value access.",
            "❌ Incorrect. Flask parses JSON inputs into a standard Python dictionary via request.get_json()."
        ),
        "q51-32": (
            "✅ Correct! Wrap predictions in try/except blocks to return a JSON error response (e.g., HTTP 400 Bad Request) instead of crashing with HTTP 500.",
            "❌ Incorrect. Implement error handling with try/except to return structured HTTP error status codes (e.g. 400 Bad Request) to the client."
        ),
        "q51-33": (
            "✅ Correct! Run the Flask app behind Gunicorn (WSGI HTTP Server) and Nginx (reverse proxy) to handle concurrent traffic and SSL securely.",
            "❌ Incorrect. Gunicorn serves WSGI applications concurrently, and Nginx acts as a reverse proxy server for production deployments."
        ),
        "q51-34": (
            "✅ Correct! requirements.txt pins your exact library versions, allowing other developers or deployment servers to replicate your environment.",
            "❌ Incorrect. The requirements.txt file lists all package dependencies to guarantee environment replication."
        ),
        "q51-35": (
            "✅ Correct! MLflow tracking server records parameters, metrics (accuracy, loss), and model artifacts for comparison across all runs.",
            "❌ Incorrect. MLflow is the standard open-source framework for managing the machine learning lifecycle, including experiment tracking."
        )
    }

    for q_id, (corr, wrg) in replacements.items():
        html = html.replace(f'<div class="quiz-feedback correct-fb" id="{q_id}-correct">✅ Correct!</div>',
                            f'<div class="quiz-feedback correct-fb" id="{q_id}-correct">{corr}</div>')
        html = html.replace(f'<div class="quiz-feedback wrong-fb" id="{q_id}-wrong">❌ Incorrect. Review the material and try again.</div>',
                            f'<div class="quiz-feedback wrong-fb" id="{q_id}-wrong">{wrg}</div>')
                            
    with open(path_w7, 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ Patched week7.html (27 quiz placeholders populated + sparse_output warning)")

print("🎉 All remaining week content quality fixes completed successfully!")
