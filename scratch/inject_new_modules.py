import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# ══════════════════════════════════════════════════════════════════════════════
# DATA DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

WEEK_CONCEPTS = {
    1: (
        ['Setup & Variables', 'Data Structures', 'Control Flow', 'Functions', 'Files & Errors', 'OOP Basics', 'NumPy Arrays'],
        "Variables and core data structures enable conditional execution and functions, which form the building blocks of classes and multi-dimensional array calculations in NumPy."
    ),
    2: (
        ['Comprehensions', 'Generators & Decorators', 'SQL Basics', 'Aggregations', 'Joins', 'Git Basics', 'Git Collab'],
        "Advanced syntax allows writing cleaner code, SQL queries load datasets from relational tables, and Git version control manages code modifications for team collaboration."
    ),
    3: (
        ['Pandas DataFrames', 'Filtering & Sorting', 'Imputing & Cleaning', 'Matplotlib Plots', 'Seaborn Styling', 'EDA Process'],
        "Loading tabular data into Pandas DataFrames enables cleaning and aggregation, which are plotted using Matplotlib/Seaborn to conduct full Exploratory Data Analysis."
    ),
    4: (
        ['Vectors & Matrices', 'Matrix Operations', 'Eigenvalues', 'Calculus Limits', 'Derivatives', 'Vector Calculus', 'Optimization'],
        "Matrix mathematics models feature vectors and coordinates in space, while derivatives calculate the gradient slopes necessary for training and parameter optimization."
    ),
    5: (
        ['ML Paradigms', 'Train-Test Splits', 'Bias & Variance', 'Evaluation Metrics', 'KNN Classifier', 'Hyperparameter Tuning'],
        "Splitting datasets allows measuring bias and variance, using standard evaluation metrics to optimize distance-based classifiers like K-Nearest Neighbors."
    ),
    6: (
        ['Linear Regression', 'Cost Functions', 'Gradient Descent', 'Multiple Regression', 'L2 Ridge', 'L1 Lasso'],
        "Fitting simple lines scales to multi-feature spaces, which require optimization via gradient descent and regularization (Ridge/Lasso) to prevent overfitting."
    ),
    7: (
        ['Logistic Classification', 'SVM Margins', 'Decision Trees', 'Ensemble Bagging', 'Gradient Boosting', 'Tuning & CV'],
        "Decision tree boundaries are scaled to robust forests via bootstrapping (bagging) and sequence learning (boosting) to build competitive tabular classifiers."
    ),
    8: (
        ['Perceptron Concept', 'Hidden Layers', 'Activation Functions', 'Forward Pass', 'Backprop Calculus', 'PyTorch Tensors'],
        "Layered neurons use non-linear activations to map predictions, computing parameter derivatives via backpropagation to optimize networks inside PyTorch."
    ),
    9: (
        ['Image Tensors', 'Conv Filters', 'Pooling Layers', 'Deep ResNets', 'Object Detection', 'Transfer Learning'],
        "Local spatial filters extract features which are downsampled by pooling, building deep representations for CV classifiers and object detection."
    ),
    10: (
        ['Sequence Data', 'Recurrent Memory', 'Vanishing Gradients', 'LSTM Gates', 'GRU Optimizations', 'Encoder-Decoder'],
        "Recurrence maintains temporal memory states, protected by mathematical gates (LSTMs/GRUs) to model complex sequence relationships."
    ),
    11: (
        ['Data Loaders', 'Discriminator', 'Generator', 'Minimax Training', 'DCGAN Transpose', 'Mode Collapse'],
        "Custom data pipelines feed adversarial Generator-Discriminator pairs that undergo minimax optimization to synthesize realistic data patterns."
    ),
    12: (
        ['Seq2Seq Bottleneck', 'Bahdanau Additive', 'Luong Multiplicative', 'Alignment Weights', 'Context Vectors', 'Attention Models'],
        "Attention weights resolve information bottlenecks by letting the decoder dynamically query the encoder's intermediate sequence representations."
    ),
    13: (
        ['spaCy Pipelines', 'POS Tagging', 'Named Entity Recognition', 'Dependency Parsing', 'TF-IDF Vectors', 'Word2Vec Embeddings'],
        "Tokenization feeds syntactic parsers and semantic representations (TF-IDF/embeddings) to map natural text to ML classifiers."
    ),
    14: (
        ['Self-Attention', 'Positional Embeddings', 'Transformer Block', 'BERT Encoder', 'GPT Decoder', 'Model Pre-training'],
        "Scaled self-attention calculates relationships across sequences, stacked into encoder-decoder blocks to power models like BERT and GPT."
    ),
    15: (
        ['LLM APIs', 'Vector Embeddings', 'Vector Store Indexes', 'Retrieval Logic', 'LangChain Integrations', 'RAG Evaluation'],
        "Vectorizing document chunks enables semantic search in vector databases, retrieving relevant context to feed into LLM prompts to prevent hallucinations."
    ),
    16: (
        ['Model Serialization', 'Flask REST API', 'WSGI Gunicorn', 'Docker Containers', 'Docker Compose', 'Gradio UI'],
        "Serializing models lets Flask APIs serve queries, packaged with Gunicorn inside Docker containers for cloud deployments."
    ),
    17: (
        ['Microservices', 'Docker Compose Network', 'Prometheus Metrics', 'CI/CD Pipelines', 'Cloud Deployment', 'Portfolio Polish'],
        "Multi-container compose services set up monitoring endpoints and automated deployment tasks to run within continuous deployment setups."
    ),
    18: (
        ['Kubernetes Basics', 'Cloud Deployment', 'MLOps & MLflow', 'Capstone spec', 'Model Pipeline', 'FastAPI & Docker', 'Cloud Deploy & stream', 'GitHub Polish', 'Resume & LinkedIn', 'Mock Drills I', 'Mock Drills II'],
        "Containers are orchestrated with Kubernetes, deployed to cloud systems, tracked with MLflow, and integrated into final portfolio projects."
    )
}

WEEK_BRIDGES = {
    1: "Next week, we will write advanced Python structures (like decorators and generators) and interface with SQL databases. Make sure you are comfortable with list manipulation and writing basic functions!",
    2: "Next week, we will transition into data analysis and visualization using Pandas, Matplotlib, and Seaborn. Make sure you are comfortable writing SQL JOIN statements and basic Git commits!",
    3: "Next week, we will dive deep into the essential mathematics of machine learning: Linear Algebra and Calculus. Make sure you are comfortable indexing and slicing Pandas DataFrames!",
    4: "Next week, we start Machine Learning Fundamentals! We will build regression and classification systems and evaluate their generalizability. Make sure you understand vector dot products and partial derivatives!",
    5: "Next week, we study Linear and Regularized Regressions under the hood. Make sure you understand the bias-variance tradeoff and how classification metrics differ from regression metrics!",
    6: "Next week, we explore tree-based models and classification: Support Vector Machines, Decision Trees, and Random Forests. Make sure you understand the difference between Ridge (L2) and Lasso (L1) regularization!",
    7: "Next week, we transition into Deep Learning! We will write multi-layer perceptrons, backpropagation, and explore PyTorch tensors. Make sure you are comfortable with basic optimization concepts!",
    8: "Next week, we enter the world of Computer Vision! We will work with Convolutional Neural Networks (CNNs), kernels, and image tensors. Make sure you understand the chain rule and forward/backward passes!",
    9: "Next week, we start Sequence Models and Recurrent Networks! We will analyze text and time-series data using RNNs, LSTMs, and GRUs. Make sure you understand channel dimensions in PyTorch tensors!",
    10: "Next week, we explore Generative Models and GANs! We will build adversarial neural networks that generate synthetic images. Make sure you are comfortable with multi-stage training loops in PyTorch!",
    11: "Next week, we explore Attention Mechanisms and Sequence Alignment. Make sure you understand the difference between sequence processing with RNNs and generative modeling!",
    12: "Next week, we study Natural Language Processing using spaCy, tokenization, entity recognition, and word vector spaces. Make sure you understand text representations and embeddings!",
    13: "Next week, we study Transformers and LLM architectures: Self-Attention, BERT, GPT, and pre-training. Make sure you understand how Word2Vec represents semantic vectors in space!",
    14: "Next week, we explore LLM Engineering, Vector Databases, Prompt Engineering, and RAG architectures! Make sure you are comfortable with the basic transformer attention calculations!",
    15: "Next week, we look at MLOps and Deployment: packaging models inside Flask APIs, Docker containers, and creating Gradio interfaces. Make sure you are comfortable handling environment variables and APIs!",
    16: "Next week is the final week! We will build our capstone stack, integrate CI/CD deployment pipelines, set up Prometheus monitoring, and polish our portfolios!",
    17: "Congratulations on completing the 135-Day AI/ML Roadmap! You have mastered Python, statistics, tabular ML, CNNs, LSTMs, GANs, Transformers, RAG, and MLOps. Time to share your portfolio and build great things! 🎉",
    18: "Congratulations! You have completed the entire 135-day roadmap and are now ready to tackle real-world AI and ML engineering challenges! 🎉"
}

WEEK_DEBUGGING = {
    1: (
        "List Multiplication Misconception",
        "A learner wants to double every element in a list of measurements, but the list repeats its structure instead of multiplying the values.",
        """# Multiply all elements of a list by 2
data = [1.2, 3.4, 5.6]
doubled = data * 2
print(doubled) # Expected: [2.4, 6.8, 11.2]""",
        "Multiplying a standard Python list by an integer N performs list repetition (duplicating the list N times), not element-wise multiplication. To perform element-wise arithmetic, you must use a list comprehension or convert the list to a NumPy array.",
        """import numpy as np
data = np.array([1.2, 3.4, 5.6])
doubled = data * 2
print(doubled) # Correct: [2.4, 6.8, 11.2]"""
    ),
    2: (
        "Broken Aggregate Query",
        "The query fails when trying to count orders placed by each customer.",
        """-- Select customer ID and count of their orders
SELECT customer_id, COUNT(order_id)
FROM orders
WHERE order_date >= '2026-01-01';""",
        "When using aggregate functions (like COUNT, SUM, AVG) alongside a non-aggregate column (like customer_id), you must group by the non-aggregate column. Otherwise, the database engine does not know how to associate the aggregate calculation with individual records.",
        """SELECT customer_id, COUNT(order_id)
FROM orders
WHERE order_date >= '2026-01-01'
GROUP BY customer_id;"""
    ),
    3: (
        "SettingWithCopy Warning in Pandas",
        "Modifying values on a filtered DataFrame yields a warning and fails to update the original dataset.",
        """import pandas as pd
df = pd.DataFrame({'age': [20, 25, None, 30]})
# Replace missing ages with the average age
df_missing = df[df['age'].isna()]
df_missing['age'] = df['age'].mean()""",
        "Filtering a DataFrame with brackets returns a slice, which might be a view or a copy. Attempting to assign values directly to it triggers the SettingWithCopy warning. Use .fillna() or .loc to modify the original DataFrame directly.",
        """import pandas as pd
df = pd.DataFrame({'age': [20, 25, None, 30]})
# Update original DataFrame in-place safely
df['age'] = df['age'].fillna(df['age'].mean())"""
    ),
    4: (
        "Element-wise vs Matrix Multiplication",
        "A script attempts to multiply a weight matrix and a feature matrix, but crashes with a shape mismatch error.",
        """import numpy as np
X = np.array([[1, 2], [3, 4], [5, 6]]) # Shape (3, 2)
W = np.array([[0.5, 0.1], [0.2, 0.9]]) # Shape (2, 2)
# Attempt matrix multiplication
out = X * W""",
        "The * operator in NumPy performs element-wise multiplication, which requires arrays to have compatible broadcast shapes. For true mathematical matrix multiplication (dot product), you must use the @ operator or np.dot().",
        """import numpy as np
X = np.array([[1, 2], [3, 4], [5, 6]]) # Shape (3, 2)
W = np.array([[0.5, 0.1], [0.2, 0.9]]) # Shape (2, 2)
# Correct matrix multiplication
out = X @ W # Output shape is (3, 2)"""
    ),
    5: (
        "KNN Scale Insensitivity",
        "KNN classifier predictions are completely unaffected by differences in age because salary values are in a much larger range.",
        """from sklearn.neighbors import KNeighborsClassifier
# Features: [salary, age]
X_train = [[50000, 22], [90000, 45], [15000, 21]]
y_train = [1, 0, 1]
knn = KNeighborsClassifier(n_neighbors=1).fit(X_train, y_train)
# Predict on new user: 51000 salary, 45 age (should be closer to class 0 user based on age)
print(knn.predict([[51000, 45]])) # Yields [1] due to salary weight""",
        "KNN calculates distances in vector space. Features with larger scales (like salary) dominate the distance metric, making features with smaller scales (like age) irrelevant. You must normalize or scale features before training distance-based models.",
        """from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
X_train = [[50000, 22], [90000, 45], [15000, 21]]
y_train = [1, 0, 1]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
knn = KNeighborsClassifier(n_neighbors=1).fit(X_scaled, y_train)
X_test = scaler.transform([[51000, 45]])
print(knn.predict(X_test)) # Correctly yields [0]"""
    ),
    6: (
        "Dummy Variable Trap in Regression",
        "Linear regression outputs wild, unstable coefficients and fits poorly because categories are one-hot encoded redundantly.",
        """import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.DataFrame({'color': ['red', 'blue', 'green'], 'price': [100, 150, 120]})
# One-hot encode without dropping categories
X = pd.get_dummies(df['color'])
model = LinearRegression().fit(X, df['price'])""",
        "If you one-hot encode all categories, the columns become perfectly collinear because their sum is always a vector of ones (which matches the intercept column). This multicollinearity destabilizes linear regressions. You must drop one category to serve as the baseline.",
        """import pandas as pd
from sklearn.linear_model import LinearRegression
df = pd.DataFrame({'color': ['red', 'blue', 'green'], 'price': [100, 150, 120]})
# Drop the first category to avoid multicollinearity
X = pd.get_dummies(df['color'], drop_first=True)
model = LinearRegression().fit(X, df['price'])"""
    ),
    7: (
        "Decision Tree Categorical crash",
        "The classifier crashes when passing categorical values directly during training.",
        """from sklearn.tree import DecisionTreeClassifier
# Features: [location, rating]
X = [['Delhi', 4.5], ['Mumbai', 3.8], ['Delhi', 4.0]]
y = [1, 0, 1]
clf = DecisionTreeClassifier().fit(X, y)""",
        "Scikit-learn's DecisionTreeClassifier expects numeric feature arrays. Direct string representations cannot be parsed by numerical algorithms. You must encode categorical text features first using OrdinalEncoder or OneHotEncoder.",
        """from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
X = [['Delhi', 4.5], ['Mumbai', 3.8], ['Delhi', 4.0]]
y = [1, 0, 1]
encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X)
clf = DecisionTreeClassifier().fit(X_encoded, y)"""
    ),
    8: (
        "Accumulating Gradients in PyTorch",
        "The PyTorch training loop loss stays high or converges to NaN because the weights updates behave erratically.",
        """import torch
X = torch.randn(10, 2)
y = torch.randn(10, 1)
model = torch.nn.Linear(2, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
for epoch in range(5):
    out = model(X)
    loss = torch.nn.functional.mse_loss(out, y)
    loss.backward()
    optimizer.step()""",
        "In PyTorch, gradients are accumulated in the .grad buffers of parameters whenever .backward() is called. If you do not clear these gradients, they sum up across epochs/batches, leading to incorrect updates. You must call optimizer.zero_grad() before computing gradients.",
        """import torch
X = torch.randn(10, 2)
y = torch.randn(10, 1)
model = torch.nn.Linear(2, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
for epoch in range(5):
    optimizer.zero_grad() # Clear gradients from previous iteration
    out = model(X)
    loss = torch.nn.functional.mse_loss(out, y)
    loss.backward()
    optimizer.step()"""
    ),
    9: (
        "Fully-Connected Input Shape Mismatch",
        "A custom CNN model crashes on the first forward pass when transitioning from convolutional layers to linear layers.",
        """import torch
import torch.nn as nn
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        # Input shape: [Batch, 3, 32, 32]
        self.conv = nn.Conv2d(3, 16, kernel_size=3) # Output shape: [Batch, 16, 30, 30]
        self.fc = nn.Linear(16 * 32 * 32, 10) # Incorrect input size
    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1) # Flatten
        return self.fc(x)
model = SimpleCNN()
model(torch.randn(1, 3, 32, 32))""",
        "A conv layer with a kernel of size 3 reduces the height and width of a 32x32 image by 2 pixels (since there is no padding), leaving a 30x30 spatial dimension. Flattening 16 channels yields 16 * 30 * 30 = 14400 features, not 16 * 32 * 32 = 16384 features.",
        """import torch
import torch.nn as nn
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 16, kernel_size=3)
        # Set linear input shape based on exact output spatial dimensions
        self.fc = nn.Linear(16 * 30 * 30, 10)
    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)"""
    ),
    10: (
        "Leaking Recurrent State Gradients",
        "Training RNN on sequences throws a graph backward error when moving from one batch to the next.",
        """import torch
rnn = torch.nn.RNN(10, 20, batch_first=True)
h = torch.zeros(1, 32, 20) # Recurrent hidden state
for x_batch in batches: # Process sequence steps
    out, h = rnn(x_batch, h) # Reusing h directly
    loss = out.sum()
    loss.backward() # Backprops through all previous batches""",
        "When you pass the hidden state h from one batch directly to the next, PyTorch maintains the computational graph across all processed batches. This leads to excessive memory use and gradient calculation conflicts. You must detach h from the history graph between batches.",
        """import torch
rnn = torch.nn.RNN(10, 20, batch_first=True)
h = torch.zeros(1, 32, 20)
for x_batch in batches:
    # Detach state to cut computation history
    h = h.detach()
    out, h = rnn(x_batch, h)
    loss = out.sum()
    loss.backward()"""
    ),
    11: (
        "Shared GAN Optimizers",
        "The Generative Adversarial Network fails to learn, and both generator and discriminator losses stay completely flat.",
        """import torch
# Instantiating a single optimizer for both models
optimizer = torch.optim.Adam(
    list(generator.parameters()) + list(discriminator.parameters()),
    lr=0.001
)""",
        "In GAN training, the Generator and Discriminator compete. Their loss functions push them in opposite directions. Training them with a single shared optimizer updates both models in lockstep, breaking the minimax optimization dynamics. They must have separate optimizers.",
        """import torch
# Declare separate optimizers to allow independent updates
opt_g = torch.optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
opt_d = torch.optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))"""
    ),
    12: (
        "Softmax Axis Mismatch in Attention",
        "The attention weights do not represent a valid probability distribution over the input sequence, resulting in chaotic translations.",
        """import torch
# Q: [Batch, Head, Seq_Len, Dim], K: [Batch, Head, Seq_Len, Dim]
scores = torch.matmul(Q, K.transpose(-2, -1)) # Shape [Batch, Head, Seq_Len, Seq_Len]
# Apply softmax over the query/batch dimensions
attn_weights = torch.softmax(scores, dim=1)""",
        "Attention weights must sum to 1 over the keys sequence length (the target sequence being searched). Thus, softmax must be applied along the very last dimension (dim=-1 or dim=3 in a 4D tensor). Applying it along dim=1 normalizes across heads.",
        """import torch
scores = torch.matmul(Q, K.transpose(-2, -1))
# Correctly normalize weights across target sequence tokens
attn_weights = torch.softmax(scores, dim=-1)"""
    ),
    13: (
        "TF-IDF Input Type Mismatch",
        "The Scikit-learn TF-IDF Vectorizer throws an attribute error when passing pre-tokenized documents during fitting.",
        """from sklearn.feature_extraction.text import TfidfVectorizer
# Documents tokenized into lists of words
docs = [["machine", "learning", "is", "cool"], ["i", "love", "python"]]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)""",
        "By default, TfidfVectorizer expects raw string documents because its internal analyzer handles lowercasing and tokenization. Passing a list of word lists causes it to fail. You must either join the tokens into sentences or pass a dummy function for analyzer/tokenizer.",
        """from sklearn.feature_extraction.text import TfidfVectorizer
docs = [["machine", "learning", "is", "cool"], ["i", "love", "python"]]
# Join tokens into space-separated string sentences
docs_joined = [" ".join(doc) for doc in docs]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs_joined)"""
    ),
    14: (
        "Missing Attention Scaling Factor",
        "The self-attention output gradients vanish quickly during training, causing parameters to stop updating.",
        """import torch
import math
Q = torch.randn(1, 8, 64) # Q shape
K = torch.randn(1, 8, 64) # K shape
# Compute raw dot-product attention weights
scores = torch.matmul(Q, K.transpose(-2, -1))
weights = torch.softmax(scores, dim=-1)""",
        "As the embedding dimension d_k grows large, the dot products grow large in magnitude, pushing the softmax function into regions with extremely small gradients. Dividing scores by sqrt(d_k) keeps logits scaled and prevents vanishing gradients.",
        """import torch
import math
Q = torch.randn(1, 8, 64)
K = torch.randn(1, 8, 64)
d_k = Q.size(-1)
# Scale scores by dividing by square root of key dimensions
scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
weights = torch.softmax(scores, dim=-1)"""
    ),
    15: (
        "Embedding Dimension Mismatch in Vector DB",
        "Querying the vector store returns a dimensionality mismatch error or fails to load vectors.",
        """from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
# Index documents with OpenAI (1536 dimensions)
db = Chroma.from_texts(["Text content"], OpenAIEmbeddings())
# Query the database with HuggingFace embeddings (384 dimensions)
retriever = db.as_retriever(search_kwargs={"embeddings": HuggingFaceEmbeddings()})""",
        "A vector database operates inside a metric space of a specific dimension. The vectors you query must reside in the exact same dimension and vector space as the vectors indexed. Using different embedding models for index and search causes dimensionality conflicts.",
        """from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
# Use identical embedding models for both database creation and retrieval
db = Chroma.from_texts(["Text content"], embeddings)
retriever = db.as_retriever()"""
    ),
    16: (
        "Method Not Allowed in Flask API",
        "The prediction endpoint returns a 405 status code when users attempt to send data payloads for scoring.",
        """from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/predict')
def predict():
    data = request.get_json()
    return jsonify({"pred": int(data['value'] * 2)})""",
        "By default, Flask routing endpoints only accept GET requests. To parse incoming JSON payloads (which require POST requests), you must explicitly register acceptable HTTP methods in the @app.route decorator.",
        """from flask import Flask, request, jsonify
app = Flask(__name__)
# Register POST method support to allow incoming scoring payloads
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    return jsonify({"pred": int(data['value'] * 2)})"""
    ),
    17: (
        "Database Connection Refused in Compose Container",
        "A containerized API fails to connect to the database container, throwing a connection refused exception.",
        """# Configuration inside compose container trying to reach database service
DB_URL = "postgresql://user:pass@127.0.0.1:5432/dbname\"""",
        "Each container in Docker runs on its own isolated loopback network. Using 127.0.0.1 inside a container resolves to that container itself, not the host machine or other containers. In Docker Compose networks, containers communicate using service names as hostname aliases.",
        """# Connect using the compose service name ('db') instead of localhost
DB_URL = "postgresql://user:pass@db:5432/dbname\""""
    ),
    18: (
        "Missing Docker CMD Instruction",
        "A student built a multi-stage Dockerfile for their FastAPI app. However, the container exits immediately with code 0.",
        """# Stage 2: Runtime
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000""",
        "A Docker container will exit immediately if there is no foreground blocking process keeping it alive. Forgetting to specify the CMD or ENTRYPOINT instruction leaves the container without a run target, so it shuts down immediately with exit code 0. You must specify CMD to start uvicorn.",
        """# Stage 2: Runtime
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]"""
    )
}

WEEKS_DAYS = {
    1: (1, 7),
    2: (8, 14),
    3: (15, 21),
    4: (22, 30),
    5: (31, 37),
    6: (38, 44),
    7: (45, 51),
    8: (52, 58),
    9: (59, 65),
    10: (66, 72),
    11: (73, 79),
    12: (80, 86),
    13: (87, 93),
    14: (94, 100),
    15: (101, 107),
    16: (108, 117),
    17: (118, 124),
    18: (125, 135)
}

# ══════════════════════════════════════════════════════════════════════════════
# MAIN PROCESSING LOGIC
# ══════════════════════════════════════════════════════════════════════════════

def process_files():
    for w in range(1, 19):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        print(f"\nProcessing week{w}.html...")
        content = open(path, 'r', encoding='utf-8').read()
        
        # 1. INJECT DEBUGGING CSS STYLES TO WEEKS 7-17
        if '.debug-block' not in content:
            print(f"  Injecting debugging block CSS into week{w}.html...")
            content = content.replace('</style>', """
/* ── DEBUG CHALLENGE ── */
.debug-block{background:rgba(229,107,140,.04);border:1px solid rgba(229,107,140,.2);border-radius:var(--radius);padding:1.1rem 1.3rem;margin:1.2rem 0}
.debug-label{font-family:var(--font-mono);font-size:9px;color:var(--pink);letter-spacing:1px;margin-bottom:.6rem}
</style>""")

        w_start, w_end = WEEKS_DAYS[w]
        
        # ──────────────────────────────────────────────────────────────────────
        # A. INJECT VISUAL CONCEPT MAP (First Day of the Week)
        # ──────────────────────────────────────────────────────────────────────
        day_marker = f'id="day-{w_start}"'
        if day_marker not in content:
            day_marker = f"id='day-{w_start}'"
            
        if day_marker in content:
            parts = content.split(day_marker, 1)
            header_and_body = parts[1]
            
            # Find boundary of day section
            next_day_marker = f'id="day-{w_start+1}"'
            next_day_marker_alt = f"id='day-{w_start+1}'"
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
            
            if 'Weekly Concept Map & Dependency Flow' not in day_body:
                print(f"  Injecting Visual Concept Map to Day {w_start}...")
                concepts, desc = WEEK_CONCEPTS[w]
                
                # Build Flow HTML
                flow_pills = ""
                for idx, c in enumerate(concepts):
                    flow_pills += f'<span style="background:var(--bg3); border:1px solid var(--border); padding:5px 10px; border-radius:6px; color:var(--text); white-space:nowrap;">{c}</span>'
                    if idx < len(concepts) - 1:
                        flow_pills += '\n    <span style="color:var(--muted); font-weight:bold;">➔</span>\n    '
                        
                map_html = f"""
  <div class="callout" style="background:rgba(108,140,255,.03); border:1px dashed var(--blue); border-radius:var(--radius); padding:1.25rem; margin-bottom:1.8rem;">
    <strong style="color:var(--blue); font-family:var(--font-head); font-size:14px; display:block; margin-bottom:0.75rem;">🗺️ Weekly Concept Map & Dependency Flow</strong>
    <div class="concept-map-flow" style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; font-family:var(--font-mono); font-size:11.5px; margin-bottom:0.75rem;">
      {flow_pills}
    </div>
    <p style="font-size:12px; color:var(--muted); margin:0; line-height:1.5;">
      <strong>How it fits together:</strong> {desc}
    </p>
  </div>
"""
                # Insert right before the objectives box
                obj_idx = day_body.find('class="objectives"')
                if obj_idx != -1:
                    div_start = day_body.rfind('<div', 0, obj_idx)
                    if div_start != -1:
                        day_body = day_body[:div_start] + map_html + day_body[div_start:]
                    else:
                        day_body = map_html + day_body
                else:
                    # Fallback to appending right after header
                    hdr_close = day_body.find('</div>\n  </div>')
                    if hdr_close == -1:
                        hdr_close = day_body.find('</div>\n</div>')
                    if hdr_close != -1:
                        day_body = day_body[:hdr_close+14] + map_html + day_body[hdr_close+14:]
                    else:
                        day_body = map_html + day_body
                        
            content = parts[0] + day_marker + day_body + remainder

        # ──────────────────────────────────────────────────────────────────────
        # B. INJECT DEBUGGING CHALLENGE & NEXT-WEEK BRIDGE (Last Day of the Week)
        # ──────────────────────────────────────────────────────────────────────
        day_marker = f'id="day-{w_end}"'
        if day_marker not in content:
            day_marker = f"id='day-{w_end}'"
            
        if day_marker in content:
            parts = content.split(day_marker, 1)
            header_and_body = parts[1]
            
            # Find boundary of day section
            next_day_marker = f'id="day-{w_end+1}"'
            next_day_marker_alt = f"id='day-{w_end+1}'"
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
            
            # B1. INJECT WEEKLY DEBUGGING CHALLENGE
            if 'WEEKLY DEBUGGING CHALLENGE' not in day_body:
                print(f"  Injecting Weekly Debugging Challenge to Day {w_end}...")
                title, symptom, broken, expl, fixed = WEEK_DEBUGGING[w]
                
                # HTML escape code blocks
                broken_esc = broken.replace('<', '&lt;').replace('>', '&gt;')
                fixed_esc = fixed.replace('<', '&lt;').replace('>', '&gt;')
                
                debug_html = f"""
  <div class="debug-block">
    <div class="debug-label">🛠️ WEEKLY DEBUGGING CHALLENGE</div>
    <h4 style="font-family:var(--font-head); font-size:14px; margin-bottom:0.5rem; color:var(--pink);">Debug: {title}</h4>
    <p style="font-size:13px; margin-bottom:0.8rem; line-height:1.6;">{symptom}</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python</span></div>
      <pre><code class="language-python">{broken_esc}</code></pre>
    </div>
    <button class="solution-toggle" onclick="toggleSolution('debug-sol-{w}')">
      <span>🔍 Reveal Bug &amp; Fix</span>
    </button>
    <div class="solution-box" id="debug-sol-{w}">
      <div class="sol-header">SOLUTION &amp; EXPLANATION</div>
      <div style="padding:1rem; background:rgba(0,0,0,0.2); font-size:13px; line-height:1.6;">
        <strong>The Bug:</strong> {expl}
        <br><br>
        <strong>The Fix:</strong>
        <div class="cb">
          <pre><code class="language-python">{fixed_esc}</code></pre>
        </div>
      </div>
    </div>
  </div>
"""
                # Insert before takeaways or fallback to resources section
                tak_idx = day_body.find('class="takeaways"')
                if tak_idx == -1:
                    tak_idx = day_body.find("class='takeaways'")
                if tak_idx == -1:
                    # Look for resources section
                    tak_idx = day_body.find('📚')
                if tak_idx != -1:
                    div_start = day_body.rfind('<div', 0, tak_idx)
                    if div_start != -1:
                        day_body = day_body[:div_start] + debug_html + day_body[div_start:]
                    else:
                        day_body = day_body[:tak_idx] + debug_html + day_body[tak_idx:]
                else:
                    # Fallback to before complete button
                    btn_idx = day_body.find('class="complete-btn"')
                    if btn_idx == -1:
                        btn_idx = day_body.find("class='complete-btn'")
                    if btn_idx != -1:
                        button_start = day_body.rfind('<button', 0, btn_idx)
                        if button_start != -1:
                            day_body = day_body[:button_start] + debug_html + day_body[button_start:]
                        else:
                            day_body = day_body[:btn_idx] + debug_html + day_body[btn_idx:]
                    else:
                        day_body += debug_html

            # B2. INJECT CONNECT TO NEXT WEEK BRIDGE
            if 'Connect to Next Week' not in day_body and 'Connect to Next Week:' not in day_body:
                print(f"  Injecting Connect to Next Week bridge to Day {w_end}...")
                bridge_text = WEEK_BRIDGES[w]
                
                bridge_html = f"""
  <div class="callout" style="background:rgba(79,209,165,.05); border-left:3px solid var(--green); padding:1rem; margin:1.5rem 0; font-size:13.5px;">
    <strong>🚀 Connect to Next Week:</strong>
    <p style="margin-top:0.4rem; margin-bottom:0; line-height:1.6;">
      {bridge_text}
    </p>
  </div>
"""
                # Insert right before the complete button
                btn_idx = day_body.find('class="complete-btn"')
                if btn_idx == -1:
                    btn_idx = day_body.find("class='complete-btn'")
                if btn_idx == -1:
                    btn_idx = day_body.find('class=complete-btn')
                if btn_idx != -1:
                    button_start = day_body.rfind('<button', 0, btn_idx)
                    if button_start != -1:
                        day_body = day_body[:button_start] + bridge_html + day_body[button_start:]
                    else:
                        day_body = day_body[:btn_idx] + bridge_html + day_body[btn_idx:]
                else:
                    day_body += bridge_html

            content = parts[0] + day_marker + day_body + remainder

        # Write back to file
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Finished modifying week{w}.html!")

if __name__ == '__main__':
    process_files()
    print("\nInjection of visual maps, debugging challenges, and week bridges completed!")
