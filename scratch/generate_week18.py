import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
week17_path = os.path.join(base_dir, "week17.html")
week18_path = os.path.join(base_dir, "week18.html")

if not os.path.exists(week17_path):
    print("Error: week17.html not found to copy styles from!")
    exit(1)

content_w17 = open(week17_path, 'r', encoding='utf-8').read()

# 1. Extract head/sidebar and script footers from week17.html
split_idx = content_w17.find('<main class="main">')
if split_idx == -1:
    print("Error: Could not find <main class='main'> in week17.html")
    exit(1)

header = content_w17[:split_idx]

# Clean up header references to week 17
header = header.replace("<title>Week 17 — Deploy + Flask + Docker | 135-Day AI/ML Roadmap</title>", "<title>Week 18 — Capstone & Portfolio Polish | 135-Day AI/ML Roadmap</title>")
header = header.replace("<title>Week 17 — Deploy + Flask + Docker</title>", "<title>Week 18 — Capstone & Portfolio Polish</title>")
header = header.replace("Week 17 Coursework", "Week 18 Coursework")
header = header.replace("Week 17 — Deploy + Flask + Docker", "Week 18 — Capstone & Portfolio Polish")
header = header.replace("Deploy + Flask + Docker", "Capstone & Portfolio Polish")
header = header.replace("Week 17", "Week 18")

# Let's adjust the day pills in topnav:
pills_old_pattern = r'<div class="day-pills" role="tablist" aria-label="Day selector">.*?</div>'
pills_new_html = """<div class="day-pills" role="tablist" aria-label="Day selector">
      <div class="day-pill active" onclick="goDay(125)" id="pill-125" role="tab" aria-selected="true" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(125)">125</div>
      <div class="day-pill" onclick="goDay(126)" id="pill-126" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(126)">126</div>
      <div class="day-pill" onclick="goDay(127)" id="pill-127" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(127)">127</div>
      <div class="day-pill" onclick="goDay(128)" id="pill-128" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(128)">128</div>
      <div class="day-pill" onclick="goDay(129)" id="pill-129" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(129)">129</div>
      <div class="day-pill" onclick="goDay(130)" id="pill-130" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(130)">130</div>
      <div class="day-pill" onclick="goDay(131)" id="pill-131" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(131)">131</div>
      <div class="day-pill" onclick="goDay(132)" id="pill-132" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(132)">132</div>
      <div class="day-pill" onclick="goDay(133)" id="pill-133" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(133)">133</div>
      <div class="day-pill" onclick="goDay(134)" id="pill-134" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(134)">134</div>
      <div class="day-pill" onclick="goDay(135)" id="pill-135" role="tab" aria-selected="false" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')goDay(135)">135</div>
    </div>"""
header = re.sub(pills_old_pattern, pills_new_html, header, flags=re.DOTALL)

# Adjust the sidebar items:
sb_items_pattern = r'<div class="sb-items" role="tablist" aria-label="Day list">.*?</div>'
sb_items_new_html = """<div class="sb-items" role="tablist" aria-label="Day list">
      <div class="sb-item active" onclick="goDay(125);closeSidebar()" id="sb-125" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(125)">Day 125: Kubernetes</div>
      <div class="sb-item" onclick="goDay(126);closeSidebar()" id="sb-126" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(126)">Day 126: Cloud Deploy</div>
      <div class="sb-item" onclick="goDay(127);closeSidebar()" id="sb-127" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(127)">Day 127: MLOps Basics</div>
      <div class="sb-item" onclick="goDay(128);closeSidebar()" id="sb-128" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(128)">Day 128: Capstone Specification</div>
      <div class="sb-item" onclick="goDay(129);closeSidebar()" id="sb-129" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(129)">Day 129: Core Pipeline</div>
      <div class="sb-item" onclick="goDay(130);closeSidebar()" id="sb-130" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(130)">Day 130: API Wrapping</div>
      <div class="sb-item" onclick="goDay(131);closeSidebar()" id="sb-131" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(131)">Day 131: Deployment Polish</div>
      <div class="sb-item" onclick="goDay(132);closeSidebar()" id="sb-132" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(132)">Day 132: GitHub Polish</div>
      <div class="sb-item" onclick="goDay(133);closeSidebar()" id="sb-133" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(133)">Day 133: Resume & LinkedIn</div>
      <div class="sb-item" onclick="goDay(134);closeSidebar()" id="sb-134" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(134)">Day 134: Mock Drills I</div>
      <div class="sb-item" onclick="goDay(135);closeSidebar()" id="sb-135" role="button" tabindex="0" onkeydown="if(event.key==='Enter')goDay(135)">Day 135: Mock Drills II</div>
    </div>"""
header = re.sub(sb_items_pattern, sb_items_new_html, header, flags=re.DOTALL)

# Extract footer starting after the closing </main> tag in week17.html
footer_idx = content_w17.find('</main>')
if footer_idx == -1:
    print("Error: Could not find </main> in week17.html")
    exit(1)

footer = content_w17[footer_idx + len('</main>'):]
footer = footer.replace("const WEEK = 17;", "const WEEK = 18;")
footer = footer.replace("const DAYS = [118,119,120,121,122,123,124];", "const DAYS = [125,126,127,128,129,130,131,132,133,134,135];")

# 2. Build Day Sections Content
main_content = '<main class="main">\n'

# Days data with tasks, resources, and quiz specifications
days_data = {
    125: {
        "title": "Kubernetes Basics for ML Deployments",
        "desc": "Learn the fundamental concepts of container orchestration with Kubernetes (K8s) and deploy a serialized ML model local cluster.",
        "hours": "5 hrs",
        "badge": "Kubernetes Basics",
        "theory": """<h3 class="sh3">1. Why Kubernetes for Production ML?</h3>
    <p>While Docker containerizes our application, Kubernetes orchestrates multiple containers across a cluster of servers, providing auto-scaling, load balancing, zero-downtime rolling updates, and self-healing. This is crucial for serving large ML workloads in production.</p>
    
    <div class="callout callout-info">
      <strong>K8s Key Concepts:</strong><br>
      • <strong>Pod:</strong> The smallest deployable unit, hosting one or more container instances.<br>
      • <strong>Deployment:</strong> Defines the desired state of pods (number of replicas, image versions).<br>
      • <strong>Service:</strong> Exposes pods to the network, load balancing traffic among them.<br>
      • <strong>kubectl:</strong> Command-line interface to interact with the K8s API.
    </div>

    <div class="mermaid">
    graph TD
      Client["Client Request"] --> Service["K8s Service (LoadBalancer)"]
      Service --> Pod1["Pod 1 (ML API Container)"]
      Service --> Pod2["Pod 2 (ML API Container)"]
      Service --> Pod3["Pod 3 (ML API Container)"]
    </div>

    <h3 class="sh3">2. Declarative K8s Manifest YAML Example</h3>
    <p>Let's define a <code>deployment.yaml</code> to serve our Flask ML API container across 3 replicas:</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">yaml — deployment.yaml</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre>apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-model-deployment
  labels:
    app: ml-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ml-api
  template:
    metadata:
      labels:
        app: ml-api
    spec:
      containers:
      - name: flask-ml-api
        image: username/flask-ml-model:v1
        ports:
        - containerPort: 5000
        resources:
          limits:
            cpu: "500m"
            memory: "512Mi"
          requests:
            cpu: "250m"
            memory: "256Mi"</pre>
    </div>

    <h3 class="sh3">3. Exposing the Deployment with a Service</h3>
    <p>Now, let's expose these pods via a LoadBalancer service using <code>service.yaml</code>:</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">yaml — service.yaml</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre>apiVersion: v1
kind: Service
metadata:
  name: ml-model-service
spec:
  type: LoadBalancer
  selector:
    app: ml-api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000</pre>
    </div>""",
        "tasks": [
            ("Deploy Local K3s Cluster", "Install k3d or minikube on your local machine and verify that you can contact the cluster using kubectl commands.", "⏱ 25 min", "tb-easy", "kubectl cluster-info runs successfully and displays cluster details."),
            ("Write K8s Deployment Manifest", "Write a complete deployment.yaml manifest for your FastAPI model serving image, setting CPU limit to 500m and memory request to 256Mi.", "⏱ 45 min", "tb-med", "yaml linting passes and dry-run validation with kubectl diff runs without exceptions.")
        ],
        "resources": [
            ("Kubernetes Tutorial for Beginners", "https://www.youtube.com/watch?v=X48VuDVv0do", "yt", "Comprehensive video covering pods, deployments, services, and cluster setups."),
            ("Kubernetes Official Deployments Doc", "https://kubernetes.io/docs/concepts/workloads/controllers/deployment/", "doc", "Reference guide for configuring replicas, rolling updates, and resource constraints.")
        ],
        "quiz": {
            "q": "What is the primary role of a Kubernetes Service?",
            "opts": [
                ("A", "To compile neural networks for faster training.", "wrong"),
                ("B", "To expose a set of pod replicas to the network and load balance traffic among them.", "correct"),
                ("C", "To store persistent training checkpoints.", "wrong")
            ],
            "fb_c": "✅ Correct! K8s Service abstracts network access, providing a single IP address and DNS name to access underlying replica pods dynamically.",
            "fb_w": "❌ Think about what happens when pods crash and restart with new IP addresses. Which element maps a stable endpoint?"
        }
    },
    126: {
        "title": "Cloud Deployment on Render & Railway",
        "desc": "Configure continuous deployment to free cloud platforms from GitHub repositories and manage environment variables securely.",
        "hours": "5 hrs",
        "badge": "Render & CD Pipelines",
        "theory": """<h3 class="sh3">1. Continuous CD Integration with GitHub</h3>
    <p>Deploying manually gets repetitive. By setting up build hooks from a GitHub repository, cloud providers automatically rebuild and redeploy your container image whenever you push new changes to the master branch.</p>

    <div class="callout callout-proj">
      <strong>Step-by-Step Render.com Deployment:</strong><br>
      1. Create a free account on Render.com.<br>
      2. Click "New" -> "Web Service".<br>
      3. Connect your GitHub repository containing the Dockerfile.<br>
      4. Render detects the Dockerfile, builds the image, and provisions a public HTTP endpoint free!
    </div>

    <h3 class="sh3">2. Simple GitHub Actions CI/CD Blueprint</h3>
    <p>This GitHub Actions workflow file <code>.github/workflows/deploy.yml</code> automatically tests code before allowing merge:</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">yaml — deploy.yml</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre>name: CI Pipeline
on: [push]
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run Pytest
      run: |
        pytest</pre>
    </div>""",
        "tasks": [
            ("Deploy to Render.com", "Create a Web Service on Render, connect your Git repository, configure environment variables, and verify that the endpoint builds successfully.", "⏱ 25 min", "tb-easy", "The Render deployment dashboard shows a green 'Live' status and outputs a public URL."),
            ("Configure GitHub Actions Pipeline", "Add a basic .github/workflows/main.yml file to your repo to automatically run black format checks and pytest suites on every push.", "⏱ 45 min", "tb-med", "GitHub repository displays a green checkmark next to your latest commit, indicating a successful run.")
        ],
        "resources": [
            ("Deploying Python to Render", "https://render.com/docs/deploy-python", "doc", "Official documentation explaining python settings, custom start commands, and wsgi setup."),
            ("GitHub Actions Quickstart", "https://docs.github.com/en/actions/quickstart", "web", "Step-by-step tutorial on writing workflow files, managing jobs, and using community actions.")
        ],
        "quiz": {
            "q": "What does a CI/CD pipeline ensure?",
            "opts": [
                ("A", "That changes are automatically tested and deployed reliably.", "correct"),
                ("B", "That models consume less VRAM on local devices.", "wrong"),
                ("C", "That Jupyter notebooks run in parallel threads.", "wrong")
            ],
            "fb_c": "✅ Correct! Automated pipelines handle the repetitive build/test/release steps, eliminating human errors and speeding up deployment.",
            "fb_w": "❌ Think about what the name stands for: Continuous Integration and Continuous Deployment. What is being continuous?"
        }
    },
    127: {
        "title": "MLOps Basics & Experiment Tracking",
        "desc": "Understand the MLOps lifecycle, use MLflow to track parameters, and record training metrics on a model registry.",
        "hours": "4 hrs",
        "badge": "MLflow Logging",
        "theory": """<h3 class="sh3">1. The Need for Experiment Tracking</h3>
    <p>During training, we adjust learning rates, model architectures, and data features. Without a centralized tracking tool, it's impossible to compare hundreds of training runs to select the best model. MLOps frameworks solve this.</p>

    <h3 class="sh3">2. Tracking Experiments with MLflow</h3>
    <p>Here is how to log parameters, metrics, and save our scikit-learn model artifact to MLflow registry:</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — train_mlflow.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre>import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

mlflow.set_experiment("Customer_Churn_RF")

with mlflow.start_run():
    n_estimators = 100
    max_depth = 5
    
    # Log hyperparameters
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    
    # Train
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X_train, y_train)
    
    # Log metric
    acc = accuracy_score(y_val, model.predict(X_val))
    mlflow.log_metric("val_accuracy", acc)
    
    # Log model artifact
    mlflow.sklearn.log_model(model, "random_forest_model")
    print(f"Logged run with accuracy: {acc}")</pre>
    </div>""",
        "tasks": [
            ("Track Hyperparameters with MLflow", "Write a training script that integrates MLflow to log parameters (learning rate, epochs) and metrics (val_loss, accuracy) during a training loop.", "⏱ 25 min", "tb-easy", "The local mlruns/ folder is created and populates metadata for the executed run."),
            ("Compare Runs in MLflow UI", "Launch the MLflow tracking user interface locally, compare at least three training runs with different hyperparameters, and export the performance table.", "⏱ 45 min", "tb-med", "Running 'mlflow ui' opens the dashboard at localhost:5000, displaying the run metrics side-by-side.")
        ],
        "resources": [
            ("MLflow Tracking Quickstart", "https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html", "doc", "Guide showing how to log metrics, compare parameters, and navigate the tracking UI."),
            ("MLOps Community Wiki", "https://mlops.community/", "web", "Curated articles and community wiki discussing deployment checklists and production observability.")
        ],
        "quiz": {
            "q": "What is logged in MLflow as an 'Artifact'?",
            "opts": [
                ("A", "The loss gradients calculated during backward pass.", "wrong"),
                ("B", "Serialized model files, plots, images, and other binary outputs of a run.", "correct"),
                ("C", "The git history of the training script.", "wrong")
            ],
            "fb_c": "✅ Correct! Artifacts are persistent files (like .pkl files or loss curve PNGs) logged and saved in store backends during a run.",
            "fb_w": "❌ Metrics are scalar numbers. Artifacts are static files. Which one stores the serialized weights?"
        }
    },
    128: {
        "title": "Capstone Part 1: Project Architecture Specification",
        "desc": "Design the complete system architecture diagram for your Capstone project, selecting datasets, model backbones, and deployment options.",
        "hours": "6 hrs",
        "badge": "Capstone Spec",
        "theory": """<h3 class="sh3">1. Choosing Your Capstone Track</h3>
    <p>Choose ONE of the three tracks to build over the next 4 days. This project must demonstrate end-to-end engineering, including model selection, pipeline orchestration, API development, containerization, and cloud deployment.</p>

    <div class="callout callout-info">
      <strong>Three Professional Tracks:</strong><br>
      • <strong>Track A: Production RAG Chatbot:</strong> Next.js frontend + FastAPI streaming backend + ChromaDB vector database + LangGraph orchestration.<br>
      • <strong>Track B: Edge Computer Vision App:</strong> MobileNetV2 feature extractor + PyTorch custom classifier + Gradio frontend + Docker containers deployed to Render.<br>
      • <strong>Track C: Fine-tuned LLM Classifier:</strong> QLoRA fine-tuned Mistral-7B/Llama-3 model + FastAPI async wrapper + LangSmith tracing.
    </div>

    <h3 class="sh3">2. System Architecture Outline</h3>
    <p>Draw a diagram of your pipeline showing data flow: User query -> Frontend client -> FastAPI Gateway -> Vector database search / Model inference -> Result streaming back to user.</p>""",
        "tasks": [
            ("Select Capstone Track", "Finalize your capstone project scope, select a specific dataset (e.g. Flickr8k, Custom PDFs), and write down the list of technologies to be integrated.", "⏱ 25 min", "tb-easy", "A project proposal file (proposal.md) is written, detailing the track scope and dataset."),
            ("Draw System Flowchart", "Draw a complete architectural flowchart tracing data queries from the browser frontend, through the API controllers and vector DBs, to the inference engine.", "⏱ 45 min", "tb-med", "An architecture SVG/PNG is created and committed to the project root assets directory.")
        ],
        "resources": [
            ("Machine Learning Systems Design Primer", "https://github.com/chiphuyen/machine-learning-systems-design", "web", "Explanations of data pipelines, prediction serving, and training infrastructure scaling."),
            ("System Design Interview Guide", "https://www.youtube.com/watch?v=xpDnVSmNFX0", "yt", "Comprehensive video detailing standard strategies for architecting complex web services.")
        ],
        "quiz": {
            "q": "Why is system architecture planning critical before coding an ML app?",
            "opts": [
                ("A", "It guarantees that the neural model weights will converge to zero loss.", "wrong"),
                ("B", "It defines network endpoints, dependency borders, and data flow paths, preventing structural mismatches later.", "correct"),
                ("C", "It automatically generates the docker-compose deployment configuration.", "wrong")
            ],
            "fb_c": "✅ Correct! Proper planning prevents circular imports, ensures clear separation of concerns, and maps structural interface requirements beforehand.",
            "fb_w": "❌ Think about integration errors. What helps align frontend inputs with backend API schemas?"
        }
    },
    129: {
        "title": "Capstone Part 2: Model Training & Core Pipeline",
        "desc": "Implement the core model training scripts, load pre-trained vectors, configure embeddings pipelines, and verify metrics convergence.",
        "hours": "6 hrs",
        "badge": "Model Training",
        "theory": """<h3 class="sh3">1. Implementing Core Pipelines</h3>
    <p>Write clean python modules for loading data, tokenizing, preprocessing text or images, and instantiating the neural architectures. Integrate MLflow tracking from Day 127 to capture training metrics.</p>

    <h3 class="sh3">2. Dense Vector Indexing Setup (For RAG)</h3>
    <p>If building the RAG chatbot (Track A), implement the parsing and semantic chunking scripts to load documents into your vector DB:</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — chunk_indexing.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre>import chromadb
from chromadb.utils import embedding_functions

# Initialize ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")
ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_or_create_collection(name="capstone_docs", embedding_function=ef)

# Chunk and insert
docs = ["Kubernetes orchestrates multiple containers.", "MLflow tracks hyperparameters and models."]
ids = ["doc1", "doc2"]
collection.add(documents=docs, ids=ids)

# Query semantic search
res = collection.query(query_texts=["How to track runs?"], n_results=1)
print(res["documents"])</pre>
    </div>""",
        "tasks": [
            ("Implement Data Preprocessing Pipeline", "Write a modular preprocessing class that scales/normalizes inputs, tokenizes texts, or resizes image inputs with clean test assertions.", "⏱ 25 min", "tb-easy", "Unit tests verify that inputs are correctly transformed into expected tensor shapes."),
            ("Build Model Training Loop", "Assemble the core training pipeline in PyTorch/Keras, setting up checkpoints and logging learning curves to your local MLflow instance.", "⏱ 45 min", "tb-med", "The model trains without errors, and accuracy/loss curves converge as logged in the tracking dashboard.")
        ],
        "resources": [
            ("PyTorch Training Loops Guide", "https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html", "doc", "Official tutorial tracing dataset loaders, network forwards, and backpropagation optimization loops."),
            ("ChromaDB Developer Reference", "https://docs.trychroma.com/getting-started", "web", "Developer manual showing how to initialize persistent clients, add metadata, and query documents.")
        ],
        "quiz": {
            "q": "What is the benefit of saving model checkpoints during training?",
            "opts": [
                ("A", "It decreases the VRAM consumption of the training batch.", "wrong"),
                ("B", "It allows restoring the model weights from the best epoch if validation performance degrades or crashes.", "correct"),
                ("C", "It automatically compiles the model for fast inference.", "wrong")
            ],
            "fb_c": "✅ Correct! Checkpointing acts as a safety net, letting you resume training or select the best generalized state safely.",
            "fb_w": "❌ Think about training failures. What happens if the server shuts down or the loss diverges after epoch 50?"
        }
    },
    130: {
        "title": "Capstone Part 3: API Wrapper & Containerization",
        "desc": "Wrap your core ML model pipeline inside a high-concurrency FastAPI async application and containerize it using multi-stage Dockerfiles.",
        "hours": "6 hrs",
        "badge": "FastAPI & Docker",
        "theory": """<h3 class="sh3">1. High-Performance FastAPI Wrapper</h3>
    <p>Serve predictions asynchronously using Pydantic validation schemas to guarantee input data formats:</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">python — main.py</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre>from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Capstone ML Model API")

class InputData(BaseModel):
    text: str

@app.post("/predict")
async def get_prediction(data: InputData):
    # Mock inference logic
    result = {"label": "Tech", "score": 0.96}
    return {"prediction": result}</pre>
    </div>

    <h3 class="sh3">2. Optimized Multi-Stage Dockerfile</h3>
    <p>Write a Dockerfile that separates compiler tools from runtime packages to output tiny images:</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">docker — Dockerfile</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre># Stage 1: Build dependencies
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]</pre>
    </div>""",
        "tasks": [
            ("Build FastAPI Predictions Route", "Create a FastAPI web server with a POST endpoint that parses input payloads using a Pydantic schema and returns model predictions.", "⏱ 25 min", "tb-easy", "Accessing localhost:8000/docs displays the interactive Swagger interface with POST schema details."),
            ("Construct Multi-stage Dockerfile", "Write an optimized Dockerfile using separate builder and runtime stages to produce a minimal container image (under 300MB if using CPU-only packages).", "⏱ 45 min", "tb-med", "Running 'docker build -t ml-api .' creates the image, and 'docker run' exposes the server successfully.")
        ],
        "resources": [
            ("FastAPI Documentation First Steps", "https://fastapi.tiangolo.com/tutorial/first-steps/", "doc", "Official FastAPI guide covering parameters, query variables, and request validation schemas."),
            ("Dockerizing Python Applications Guide", "https://docs.docker.com/language/python/containerize/", "doc", "Reference guide explaining best practices for building python images, caching layers, and setting users.")
        ],
        "quiz": {
            "q": "What is the primary advantage of multi-stage Docker builds?",
            "opts": [
                ("A", "They allow running multiple containers on the same port.", "wrong"),
                ("B", "They keep the final production image clean and tiny by excluding compilers and build cache layers.", "correct"),
                ("C", "They speed up the training of convolutional networks.", "wrong")
            ],
            "fb_c": "✅ Correct! By leaving intermediate compilers and download caches behind, production images are highly optimized and secure.",
            "fb_w": "❌ Think about disk size and container footprint. What happens if we copy intermediate compiler headers to production?"
        }
    },
    131: {
        "title": "Capstone Part 4: Cloud Deployment & Frontend",
        "desc": "Deploy your containerized backend service to Render or Railway, link it to a frontend UI, and perform end-to-end integration tests.",
        "hours": "6 hrs",
        "badge": "CD Integrations",
        "theory": """<h3 class="sh3">1. Testing the Live Endpoint</h3>
    <p>Verify that your cloud deployment works by sending predictions payload via curl requests:</p>
    <div class="cb">
      <div class="cb-head"><span class="cb-lang">bash — test_endpoint.sh</span><div class="cb-btns"><button class="copy-btn" onclick="copyCode(this)">copy</button></div></div>
      <pre>curl -X POST https://your-app.onrender.com/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "Is this model scaling automatically?"}'</pre>
    </div>

    <h3 class="sh3">2. Simple Frontend Integration</h3>
    <p>Wire up a clean Streamlit or Gradio interface that connects to your deployed API backend, giving non-technical users a way to interact with your model.</p>""",
        "tasks": [
            ("Deploy Container to Cloud", "Configure continuous deployment on Render or Railway to automatically pull your Docker image and expose it to a public endpoint.", "⏱ 25 min", "tb-easy", "The cloud provider logs show successful container startup, and curl query to the public URL returns prediction results."),
            ("Build Streamlit User Interface", "Write a simple streamlit.py app that exposes input boxes/sliders and fetches results dynamically from the deployed backend service.", "⏱ 45 min", "tb-med", "Running 'streamlit run streamlit.py' launches a beautiful local web client that displays model scores.")
        ],
        "resources": [
            ("Streamlit Connections Tutorial", "https://docs.streamlit.io/develop/tutorials/databases/private-api", "doc", "Reference guide showing how to query private external API endpoints and display JSON responses."),
            ("Railway CD Deploy Guide", "https://docs.railway.app/deploy/overview", "web", "Step-by-step guide explaining continuous deployment pipelines, volume mounts, and proxy routing.")
        ],
        "quiz": {
            "q": "Why should the client frontend query the model via an API rather than loading weights directly?",
            "opts": [
                ("A", "Loading model weights in the client frontend is faster but requires more bandwidth.", "wrong"),
                ("B", "It decouples client UI changes from model architecture updates, keeping the client code extremely lightweight.", "correct"),
                ("C", "APIs automatically compress weights before transmitting predictions.", "wrong")
            ],
            "fb_c": "✅ Correct! Decoupled architectures allow updating the backend model weights without modifying or redeploying the client frontend.",
            "fb_w": "❌ Think about model size (e.g. 500MB). Can we expect a user's web browser to download and run the model locally?"
        }
    },
    132: {
        "title": "GitHub Portfolio Polish",
        "desc": "Refactor your repositories, write clean documentation with system design flowcharts, and optimize your GitHub landing page.",
        "hours": "5 hrs",
        "badge": "Repository Layouts",
        "theory": """<h3 class="sh3">1. Formatting a Professional README</h3>
    <p>A recruiter evaluates a project in 10 seconds. Your README must show: Project Title, Architecture diagram, Tech Stack badges, Quickstart commands, and Evaluation Metrics results.</p>

    <div class="callout callout-tip">
      <strong>README Blueprint:</strong><br>
      • Use markdown headers clearly.<br>
      • Add visual flowcharts or screenshots of the user interface.<br>
      • Display accuracy, precision, F1 score tables or latency charts.<br>
      • Show setup commands: <code>docker-compose up --build</code>.
    </div>""",
        "tasks": [
            ("Organize Repository Files", "Refactor your capstone repository to separate code (/src), configurations (/config), unit tests (/tests), and assets (/assets).", "⏱ 25 min", "tb-easy", "The repository structure matches the standard clean production blueprint."),
            ("Write Professional README.md", "Draft a comprehensive README documenting the project overview, system design flow, quickstart instructions, and evaluation metrics results.", "⏱ 45 min", "tb-med", "README displays clear markdown tables, code syntax highlights, and linked architecture diagrams.")
        ],
        "resources": [
            ("Awesome README List", "https://github.com/matiassingers/awesome-readme", "web", "Collection of highly polished README files for different technology stacks and projects."),
            ("Markdown Reference Guide", "https://www.markdownguide.org/", "web", "Comprehensive reference guide for writing tables, code blocks, checklists, and images in markdown.")
        ],
        "quiz": {
            "q": "What is the most critical information a project README should convey immediately?",
            "opts": [
                ("A", "The complete git commit history.", "wrong"),
                ("B", "What the project does, the architecture flow, and how to run it locally in under 3 commands.", "correct"),
                ("C", "The detailed derivation of the loss functions.", "wrong")
            ],
            "fb_c": "✅ Correct! Recruits and developers want to understand the project value and run the setup instantly without reading long manuals.",
            "fb_w": "❌ Think about user convenience. When you look at an open-source project, what do you want to see first?"
        }
    },
    133: {
        "title": "Resume & LinkedIn Optimization",
        "desc": "Incorporate your AI/ML projects and MLOps keywords into your technical resume and optimize your LinkedIn profile for recruiter search.",
        "hours": "5 hrs",
        "badge": "Resume Formatting",
        "theory": """<h3 class="sh3">1. Formatting the ML Resume</h3>
    <p>List your projects using the STAR method (Situation, Task, Action, Result). Highlight specific engineering impact: "Built RAG pipeline, reducing latency by 40% and increasing retrieval recall to 92%."</p>

    <div class="callout callout-info">
      <strong>Key Keywords to Include:</strong><br>
      Python, PyTorch, scikit-learn, LangChain, Transformers, Docker, FastAPI, ChromaDB, Kubernetes, MLflow, CI/CD, MLOps, System Design.
    </div>""",
        "tasks": [
            ("Add MLOps Keywords to Skills", "Update your resume skills grid to explicitly include production keywords (Docker, Kubernetes, MLflow, CI/CD, FastAPI) alongside ML frameworks.", "⏱ 25 min", "tb-easy", "Resume skills section lists complete technologies matching modern job descriptions."),
            ("Write STAR Project Descriptions", "Rewrite your capstone project descriptions using the STAR method, highlighting quantified results and engineering metrics.", "⏱ 45 min", "tb-med", "Resume bullet points display specific numbers showing performance increases or cost reductions.")
        ],
        "resources": [
            ("ML Engineer Resume Guidelines", "https://www.workera.ai/", "web", "Standard resume formats and engineering skill grids compiled from top industry hiring practices."),
            ("LinkedIn Optimization Tips", "https://www.linkedin.com/", "web", "Checking search algorithms, headline formulas, and profile summaries optimization strategies.")
        ],
        "quiz": {
            "q": "How does the STAR method improve resume descriptions?",
            "opts": [
                ("A", "It automatically translates your resume into multiple languages.", "wrong"),
                ("B", "It structures bullet points to highlight your actions and quantified business/engineering impact, rather than just listing tasks.", "correct"),
                ("C", "It guarantees that the resume will bypass ATS scanners.", "wrong")
            ],
            "fb_c": "✅ Correct! STAR points show hiring managers exactly what actions you took and the real impact of your work.",
            "fb_w": "❌ Think about impact. What sounds better: 'Worked on RAG' or 'Designed a RAG pipeline that increased retrieval recall by 15%'?"
        }
    },
    134: {
        "title": "Final Interview Prep: ML Theory & Coding",
        "desc": "Revise core machine learning theory topics, algorithms derivation, evaluation metrics, and solve popular coding drill questions.",
        "hours": "6 hrs",
        "badge": "ML Theory Drills",
        "theory": """<h3 class="sh3">1. Core ML Interview Drill Scenarios</h3>
    <p>Practice answering classic technical interview questions in structured layouts:</p>

    <div class="callout callout-proj">
      <strong>Example Scenarios:</strong><br>
      • <strong>Q:</strong> How do you handle high class-imbalance during training?<br>
      • <strong>A:</strong> Downsample majority class, upsample minority class (SMOTE), apply class-weighted loss functions, and evaluate using Precision-Recall AUC instead of Accuracy.<br>
      <br>
      • <strong>Q:</strong> Why does gradient descent diverge and how do we fix it?<br>
      • <strong>A:</strong> The learning rate is set too high, causing weight values to overshoot the minimum. Fix: Reduce learning rate, apply decay schedules, or use Adaptive optimizers (Adam).
    </div>""",
        "tasks": [
            ("Revise Core ML Theory Topics", "Review mathematical derivations for key algorithms (linear regression gradients, SVM margins, cross-entropy derivatives).", "⏱ 25 min", "tb-easy", "You can verbally explain how cost functions guide model parameter adjustments."),
            ("Solve Classical ML Coding Drills", "Practice coding simple ML helper functions from scratch (e.g. k-means step, computing precision/recall scores, standardizing arrays).", "⏱ 45 min", "tb-med", "You can write the NumPy equations for basic metrics in under 10 minutes without references.")
        ],
        "resources": [
            ("Machine Learning Interview Book", "https://huyenchip.com/ml-interviews-book/", "web", "Free online chapters detailing engineering, systems design, and theory interview loops."),
            ("ML Coding Interview Prep Tips", "https://www.youtube.com/watch?v=N5P5z2bTqQ4", "yt", "Video walking through common python coding drills, array operations, and algorithm implementations.")
        ],
        "quiz": {
            "q": "Why is Precision-Recall AUC preferred over ROC AUC for highly imbalanced datasets?",
            "opts": [
                ("A", "PR AUC is faster to compute in python.", "wrong"),
                ("B", "PR AUC focuses on the minority positive class and is not affected by a large count of true negatives, giving a realistic evaluation.", "correct"),
                ("C", "PR AUC ignores false positives entirely.", "wrong")
            ],
            "fb_c": "✅ Correct! ROC AUC contains False Positive Rate, which uses True Negatives in the denominator, masking poor minority predictions when TN is huge.",
            "fb_w": "❌ Think about the formulas. FPR = FP / (FP + TN). If TN is 1 million and FP is 100, what happens to FPR?"
        }
    },
    135: {
        "title": "Final Interview Prep: System Design & Graduation",
        "desc": "Review end-to-end ML system design blueprints (scaling pipelines, model monitoring, load balancing) and celebrate your graduation!",
        "hours": "6 hrs",
        "badge": "ML System Design",
        "theory": """<h3 class="sh3">1. ML System Design Layout</h3>
    <p>When asked to design an ML system (e.g. recommendation system or search ranking), structure your response into: Data Ingestion & Preprocessing -> Model Training & Registry -> Online Inference API -> Model Monitoring & Feedback loops.</p>

    <div class="milestone">
      <div class="milestone-icon">🎉</div>
      <div class="milestone-content">
        <h4>135 Days Complete — You Are Now an AI Engineer!</h4>
        <p>Congratulations! You have completed the entire 135-day curriculum. You have coded Python basics, calculated multivariate derivatives, implemented deep classifiers, containerized services, and deployed capstones. You have all the skills needed to build production-grade AI applications. Keep learning, keep building, and go change the industry! 🚀</p>
      </div>
    </div>""",
        "tasks": [
            ("Design ML System Architecture", "Draft a complete system design document for a real-time product recommendation engine, covering data pipes, retrieval, ranking, and monitoring.", "⏱ 25 min", "tb-easy", "The layout clearly details database choices, API endpoints, caching layers, and latency budgets."),
            ("Review Model Drift Metrics", "Study how data drift is detected using Population Stability Index (PSI) and formulate a monitoring plan for production serving.", "⏱ 45 min", "tb-med", "You can describe how drift alerts trigger automated pipelines to pull new inputs and retrain.")
        ],
        "resources": [
            ("ML System Design Interview Guide", "https://github.com/khangich/machine-learning-system-design", "web", "Exhaustive review resource covering recommendation, search, feeds, and monitoring architectures."),
            ("MLOps Guide & Milestones", "https://mlops-guide.org/", "web", "Overview roadmap covering continuous training, model registries, registries checks, and monitoring systems.")
        ],
        "quiz": {
            "q": "What is the primary indicator that an ML model in production needs to be retrained?",
            "opts": [
                ("A", "The server hosting the API runs out of memory.", "wrong"),
                ("B", "Input data distributions shift significantly (data drift), leading to drop in real-world performance metrics.", "correct"),
                ("C", "The API receives more than 10,000 requests per second.", "wrong")
            ],
            "fb_c": "✅ Correct! When real-world user data shifts away from the training distribution, the model's accuracy degrades, requiring retraining on fresh inputs.",
            "fb_w": "❌ Think about changing user behaviors over time. What happens if the training data was collected in winter, but it is now summer?"
        }
    }
}

takeaways_data = {
    125: ["Kubernetes provides auto-scaling, self-healing, and load balancing for production containers.",
          "Pods are the smallest deployable units in K8s, and Services expose them to external traffic."],
    126: ["Continuous deployment (CD) automates builds and releases directly from git pushes.",
          "GitHub Actions workflows can run unit tests on every commit to ensure pull request stability."],
    127: ["MLflow logs hyperparameter settings, execution metrics, and serialized model files (artifacts).",
          "Centralized tracking interfaces let you compare multiple runs side-by-side to select the optimal candidate."],
    128: ["Designing clear system boundaries and endpoints is critical before writing ML application code.",
          "Choose the appropriate track (RAG, CV, or LLM) matching your target domain for the portfolio project."],
    129: ["Modularizing training and preprocessing code ensures model reproducibility and testability.",
          "Sentence Transformers and vector indices (e.g., ChromaDB) allow performing semantic search for RAG."],
    130: ["FastAPI provides async handlers and data validation via Pydantic models for fast web serving.",
          "Multi-stage Docker builds reduce the production image size by leaving compilers and caches behind."],
    131: ["Integration testing verifies that client requests flow seamlessly to backend cloud endpoints.",
          "Streamlit or Gradio can be used to construct a quick interactive web interface for the API."],
    132: ["A clean and organized repository structure (src, tests, configs) improves code maintainability.",
          "A professional README.md with clear metrics, architecture diagrams, and quickstart commands is a portfolio key."],
    133: ["Use the STAR format to showcase engineering results and quantified business impact in your resume.",
          "Include high-impact MLOps keywords (Docker, K8s, MLflow, CI/CD) matching modern job descriptions."],
    134: ["Review core machine learning mathematical foundations (gradients, SVM margins, cross-entropy) regularly.",
          "NumPy-based array operations and basic algorithm implementations (e.g. k-means) are popular interview drills."],
    135: ["ML System Design responses should structure data pipes, modeling, online serving, and active monitoring.",
          "Graduating the 135-day curriculum marks the start of building production-grade AI applications!"]
}

objectives_data = {
    125: [
        "Understand Kubernetes architecture (Pods, Deployments, Services) and how they scale ML APIs.",
        "Write declarative YAML manifests to serve a containerized Flask/FastAPI app with multiple replicas.",
        "Install a local cluster (k3d/minikube) and test cluster scaling and service exposure via LoadBalancer."
    ],
    126: [
        "Set up continuous deployment (CD) pipelines triggered automatically from GitHub pushes.",
        "Configure environment variables and secrets securely inside cloud-hosted runners.",
        "Write GitHub Actions workflow files to automate unit testing suites on code updates."
    ],
    127: [
        "Differentiate model metrics tracking from traditional code versioning workflows.",
        "Integrate MLflow SDK into model training scripts to log hyperparameters, training loss, and val accuracy.",
        "Compare model performance runs side-by-side inside the local MLflow dashboard."
    ],
    128: [
        "Structure a complete machine learning system design covering data flow and integration points.",
        "Select an appropriate capstone project track (RAG Chatbot, CV classifier, or LLM Classifier).",
        "Draft an architectural flowchart tracing raw inputs to downstream inference components."
    ],
    129: [
        "Build modular Python scripts for loading, cleaning, and preprocessing domain data.",
        "Set up a robust training loop or vector indexing pipeline using ChromaDB.",
        "Track validation metrics and save serialized model check-points."
    ],
    130: [
        "Expose model predictions using FastAPI async endpoints with Pydantic request validation.",
        "Write multi-stage Dockerfiles to minimize production container footprint.",
        "Build and verify local Docker images, testing container responsiveness on exposing ports."
    ],
    131: [
        "Deploy the containerized backend ML API to a public cloud environment (Render or Railway).",
        "Develop a lightweight Streamlit or Gradio user interface that connects to the remote API.",
        "Perform end-to-end integration tests confirming predictions are served under 500ms."
    ],
    132: [
        "Structure repository directories following standard engineering layouts (src, tests, configs).",
        "Write a comprehensive README.md including architecture diagrams, metrics tables, and quickstarts.",
        "Document setup steps using docker-compose to enable single-command local reproduction."
    ],
    133: [
        "Format project bullets using the STAR framework to emphasize quantified engineering results.",
        "Incorporate industry-demand MLOps keywords (Docker, K8s, CI/CD, MLflow) into technical skills grids.",
        "Optimize your professional LinkedIn profile to align with modern developer search patterns."
    ],
    134: [
        "Review fundamental machine learning mathematical equations (loss derivatives, SVM margin optimization).",
        "Practice implementing common algorithms (e.g. k-means, precision/recall metrics) using raw NumPy.",
        "Solve classical coding interview drills under standard time constraints."
    ],
    135: [
        "Structure responses to ML system design interview questions into logical components.",
        "Formulate monitoring plans to identify feature drift and model performance degradation.",
        "Graduate the 135-day roadmap and transition to active industry role applications!"
    ]
}

for d, data in days_data.items():
    active_class = " active" if d == 125 else ""
    
    # Format Tasks HTML
    tasks_html = f"""<div id="tasks-section-{d}">
        <h2 class="sh2">⚡ Tasks</h2>"""
        
    for title, desc, time, badge_class, done in data["tasks"]:
        tasks_html += f"""
        <div class="task-block">
          <div class="task-header" onclick="toggleTask(this)" style="background:rgba(79,209,165,.05)" role="button" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')this.click()" aria-expanded="false">
            <span class="task-badge {badge_class}">{badge_class.replace('tb-','').upper()}</span>
            <span class="task-title">{title}</span>
            <span class="task-time">{time}</span>
          </div>
          <div class="task-body">
            <p>{desc}</p>
            <div class="done-when">{done}</div>
          </div>
        </div>"""
    tasks_html += "</div>"
    
    # Format Resources HTML
    res_html = f"""<h2 class="sh2">📚 Recommended Resources</h2>
    <div class="res-grid">"""
    
    for r_title, url, r_type, r_desc in data["resources"]:
        icon = "📺" if r_type == "yt" else "📄" if r_type == "doc" else "🌐"
        res_html += f"""
      <a href="{url}" class="res-card type-{r_type}-card" target="_blank">
        <div class="res-icon type-{r_type}">{icon}</div>
        <div class="res-body">
          <div class="res-type">{r_type.upper()}</div>
          <span class="res-title">{r_title}</span>
          <div class="res-desc">{r_desc}</div>
        </div>
      </a>"""
    res_html += "</div>"
    
    # Format Quiz HTML
    quiz_html = f"""<h2 class="sh2">🧪 Quiz</h2>
    <div class="quiz-block" id="quiz-section-{d}">
      <div class="quiz-num">Q1 OF 1</div>
      <div class="quiz-q">{data["quiz"]["q"]}</div>"""
      
    for idx, (letter, text, status) in enumerate(data["quiz"]["opts"]):
        quiz_html += f"""
      <div class="quiz-opt" onclick="quiz(this,'{status}','q{d}a')" role="button" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')this.click()"><span class="quiz-letter">{letter}</span>{text}</div>"""
      
    quiz_html += f"""
      <div class="quiz-feedback correct-fb" id="q{d}a-correct">{data["quiz"]["fb_c"]}</div>
      <div class="quiz-feedback wrong-fb" id="q{d}a-wrong">{data["quiz"]["fb_w"]}</div>
    </div>"""

    # Format Takeaways HTML
    takeaways_list = takeaways_data.get(d, [
        "Mastered the essential architecture, workflows, and configurations of this lesson.",
        "Implemented coding exercises and verified implementation correct behaviour."
    ])
    takeaways_items = "".join(f"      <li><strong>Key Point:</strong> {item}</li>\n" for item in takeaways_list)
    takeaways_html = f"""
  <div class="takeaways">
    <h3>📝 Key Takeaways</h3>
    <ol>
{takeaways_items}    </ol>
  </div>"""

    # Format Objectives HTML
    objectives_list = objectives_data.get(d, [])
    objectives_items = "".join(f"      <li>{item}</li>\n" for item in objectives_list)
    objectives_html = f"""
    <div class="objectives">
      <h3>🎯 By the end of Day {d} you will be able to:</h3>
      <ul>
{objectives_items}      </ul>
    </div>"""

    # Combine everything
    main_content += f"""
  <!-- DAY {d} -->
  <div class="day-section{active_class}" id="day-{d}">
    <div class="day-header">
      <div class="day-tag">WEEK 18 · DAY {d}</div>
      <h1>{data["title"]}</h1>
      <p>{data["desc"]}</p>
      <div class="meta-row">
        <span class="meta-badge g">⏱ {data["hours"]}</span>
        <span class="meta-badge o">⚡ {data["badge"]}</span>
      </div>
    </div>

    {objectives_html}

    {data["theory"]}

    {tasks_html}

    {quiz_html}

    {takeaways_html}

    {res_html}

    <button class="complete-btn" id="btn-day-{d}" onclick="completeDay({d}, 150)">✓ Complete Day {d} — Earn 150 XP!</button>
  </div>
"""

main_content += '</main>\n'

# Write final file
week18_html = header + main_content + footer
with open(week18_path, 'w', encoding='utf-8') as f:
    f.write(week18_html)

print("week18.html generated successfully!")
