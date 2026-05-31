import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

WEEKS_DAYS = {
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
}


# Dictionaries of topics and customized blocks for missing elements
DAY_TOPICS = {
    31: "ML Fundamentals", 32: "Regression Metrics", 33: "Classification Metrics",
    34: "Bias-Variance Tradeoff", 35: "Hyperparameter Tuning", 36: "KNN & Naive Bayes",
    37: "Capstone: Scikit-learn Pipeline", 38: "Simple Linear Regression",
    39: "Multiple Linear Regression & OLS", 40: "Ridge & Lasso Regularization",
    41: "Gradient Descent Optimization", 42: "Feature Scaling & Data Leakage",
    43: "Polynomial Regression", 44: "Capstone: Regression Pipeline",
    45: "Logistic Regression", 46: "SVMs", 47: "Decision Trees",
    48: "Random Forests", 49: "XGBoost", 50: "Hyperparameter Tuning (Trees)",
    51: "Capstone: Classification Pipeline", 52: "Perceptron",
    53: "Activation Functions", 54: "Backpropagation", 55: "PyTorch Workflows",
    56: "Multi-Layer Perceptron (MLP)", 57: "Scaling & Weight Init",
    58: "Capstone: PyTorch MLP", 59: "Convolutional Layer", 60: "Pooling Layers",
    61: "Custom CNNs", 62: "ResNets & Skip Connections", 63: "Object Detection (YOLO)",
    64: "Semantic Segmentation (U-Net)", 65: "Capstone: Transfer Learning Project",
    66: "Recurrent Neural Networks (RNN)", 67: "Backpropagation Through Time",
    68: "LSTM cell", 69: "GRU cell", 70: "Bidirectional sequence models",
    71: "Text classification", 72: "Seq2Seq & Encoder-Decoder", 73: "GANs Introduction",
    74: "DCGANs (Deep Convolutional GANs)", 75: "Virtual Try-ons / Conditional GANs",
    76: "GAN evaluation (FID score)", 77: "Custom dataset loading",
    78: "Alternating training loops", 79: "Capstone: GAN generation project",
    80: "Attention Mechanism", 81: "Bahdanau vs Luong Attention", 82: "KV Caching",
    83: "FlashAttention", 84: "Image Captioning models", 85: "Attention weights behavior",
    86: "Positional Encodings (RoPE)", 87: "spaCy pipelines", 88: "POS Tagging",
    89: "Named Entity Recognition (NER)", 90: "Dependency Parsing",
    91: "Word Embeddings (Word2Vec)", 92: "TF-IDF vectorization",
    93: "Hugging Face pipelines", 94: "Self-Attention math", 95: "Transformers & RoPE",
    96: "BERT MLM training", 97: "HF Tokenizer Mechanics", 98: "GPT-2 & nanoGPT",
    99: "Fine-tuning BERT", 100: "HF Spaces", 101: "RAG introduction",
    102: "Fine-tuning vs RAG", 103: "Vector Databases (Chroma)", 104: "Semantic Search",
    105: "RAG Evaluation (Ragas)", 106: "LLM Agents & Tool Use", 107: "Capstone — Agentic Systems",
    108: "Flask APIs deployment", 109: "Docker containerization",
    110: "Gunicorn worker models", 111: "Model weights in Docker",
    112: "Docker layer caching", 113: "Multi-stage Docker builds",
    114: "Gradio web applications", 115: "Gradio to Hugging Face Spaces",
    116: "Docker Compose", 117: "API integration testing", 118: "Production pipelines",
    119: "Kubernetes deployments", 120: "Database migrations in Docker",
    121: "Prometheus monitoring", 122: "Concept drift & Data drift",
    123: "CI/CD MLOps pipelines", 124: "Capstone: real-time match prediction",
    125: "Kubernetes Basics", 126: "Cloud Deployment", 127: "MLOps & MLflow",
    128: "Capstone Specification", 129: "Model Training & Pipeline",
    130: "FastAPI & Docker", 131: "Cloud Deploy & stream", 132: "GitHub Portfolio Polish",
    133: "Resume & LinkedIn", 134: "Mock Interview Drills I", 135: "Mock Interview Drills II"
}

# Detailed fallback templates dynamically customizable
def get_hinglish(day, topic):
    return f"📢 <strong>Ek line mein:</strong> Day {day} seekhta hai kaise {topic} ko efficiently code aur validate kiya jata hai real-world data ke sath."

def get_misconception(day, topic):
    return f"Misconception: {topic} hamesha baseline parameters ke sath bina tuning ke perfectly kaam karega. Fact: Har dataset ki characteristics alag hoti hain, isliye hyperparameter tuning aur proper features scaling model performance ke liye zaroori hain."

def get_analogy(day, topic):
    return f"Jaise kitchen mein alag-alag recipes ke liye ingredients ka preparation zaroori hota hai, vaise hi {topic} ke liye data preprocessing aur parameter check sabse basic step hai."

# Overrides for high-quality customized elements where reported missing
CUSTOM_HINGLISH = {
    40: "📢 <strong>Ek line mein:</strong> Ridge aur Lasso regression cost function mein penalties add karke overfitting ko rokte hain aur weights ko control mein rakhte hain.",
    42: "📢 <strong>Ek line mein:</strong> Data scaling hamesha train_test_split ke baad shuru karni chahiye taaki test set ki information train set mein leak na ho.",
    44: "📢 <strong>Ek line mein:</strong> Capstone regression pipeline raw features se lekar final metrics output tak poore workflow ko automated aur error-free banati hai.",
    45: "📢 <strong>Ek line mein:</strong> Logistic Regression binary classification ke liye linear boundary calculate karke sigmoid ke zariye outcomes ki probability nikalta hai.",
    46: "📢 <strong>Ek line mein:</strong> SVM classification boundaries ko margin-maximize karke draw karta hai taaki test predictions sabse door aur reliable rahein.",
    47: "📢 <strong>Ek line mein:</strong> Decision Tree data features par yes/no sawal poochkar classification rules ka ek flowchart-like structure banata hai.",
    48: "📢 <strong>Ek line mein:</strong> Random Forest multiple decision trees ka aapas mein average lekar individual variance aur overfitting ko bohot kam kar deta hai.",
    49: "📢 <strong>Ek line mein:</strong> XGBoost sequential gradient boosting ke zariye har naye tree ko purane errors/residuals par fit karke ensemble accuracy badhata hai.",
    50: "📢 <strong>Ek line mein:</strong> Grid Search aur Random Search tree hyperparameters (jaise max_depth, n_estimators) ke optimal settings dhundhne ke automated methods hain.",
    51: "📢 <strong>Ek line mein:</strong> Custom classification pipeline tabular features preprocessing aur tree classifiers ko ek single modular execution block mein bind karti hai.",
    58: "📢 <strong>Ek line mein:</strong> PyTorch dynamic graph workflows design karke layers gradients flow aur weights update ko training loop mein automated handle karte hain.",
    59: "📢 <strong>Ek line mein:</strong> Convolutions filters ke dot-products se image ke visual features (edges, shapes) ko preserve karke local structures extract karte hain.",
    60: "📢 <strong>Ek line mein:</strong> Max pooling and average pooling spatial resolutions ko downsample karte hain taaki computational size aur overfitting dono reduce ho sakein.",
    61: "📢 <strong>Ek line mein:</strong> PyTorch custom CNN class structure forward pass tensors calculations ko dynamic layers channels ke sath execute karta hai.",
    62: "📢 <strong>Ek line mein:</strong> ResNets layers input ko shortcut connection se output mein add karte hain taaki deep networks mein gradient vanish na ho.",
    63: "📢 <strong>Ek line mein:</strong> YOLO object detection network image ko grid cells mein divide karke ek single forward pass mein multiple boxes aur labels predict karta hai.",
    64: "📢 <strong>Ek line mein:</strong> U-Net contracting encoder aur expanding decoder blocks ke combination se segmentation maps ko pixel-level scale par recover karta hai.",
    65: "📢 <strong>Ek line mein:</strong> Transfer learning pre-trained model weights (like ResNet) ko feature extractor ya fine-tuning se target dataset par adjust karta hai.",
    66: "📢 <strong>Ek line mein:</strong> RNNs sequential steps sequence processing ke liye current state memory ko hidden variables ke form mein maintain karte hain.",
    67: "📢 <strong>Ek line mein:</strong> BPTT backpropagation time-series dimensions par compute karta hai jismein gradient clipping se explosion roka jata hai.",
    68: "📢 <strong>Ek line mein:</strong> LSTMs cell state aur gate loops ke memory parameters se vanishing gradients issue ko resolve karke long context store karte hain.",
    69: "📢 <strong>Ek line mein:</strong> GRU cell parameters input forget gate vectors ko reset/update gate ke form mein simplify karke computational speed badhata hai.",
    71: "📢 <strong>Ek line mein:</strong> Text classification workflows raw strings ko token arrays aur sequence vectors mein map karke recurrent neural network par feed karte hain.",
    73: "📢 <strong>Ek line mein:</strong> GANs generator aur discriminator networks ko aapas mein minimax game ki tarah train karke synthetic distributions generate karte hain.",
    74: "📢 <strong>Ek line mein:</strong> DCGAN convolutional layers filters aur transpose conv layers se stable spatial structure synthesis execute karta hai.",
    75: "📢 <strong>Ek line mein:</strong> Conditional GAN generator outputs ko input conditions parameters (labels/images) ke direction mein control aur synthesize karta hai.",
    76: "📢 <strong>Ek line mein:</strong> FID metric real aur generated images features statistical divergence score ko pre-trained model embeddings se calculate karta hai.",
    77: "📢 <strong>Ek line mein:</strong> Custom dataset mapping dataloader batch collation aur multi-threading generators se inputs prepare karta hai.",
    78: "📢 <strong>Ek line mein:</strong> Alternating training loops discriminator aur generator parameters steps updates ko separate optimizers updates se handle karte hain.",
    79: "📢 <strong>Ek line mein:</strong> Capstone GAN pipeline stable training epochs and image plotting loops se generative models capabilities test karti hai.",
    80: "📢 <strong>Ek line mein:</strong> Attention mechanism decoder queries ko encoder keys se dot-product karva ke most relevant features weights values fetch karta hai.",
    81: "📢 <strong>Ek line mein:</strong> Bahdanau additive models query key features concat/add karte hain jabki Luong multiplicative models query key multiplication use karte hain.",
    82: "📢 <strong>Ek line mein:</strong> KV caching historical tokens calculation vectors parameters ko repeat calculations se bachata hai.",
    83: "📢 <strong>Ek line mein:</strong> FlashAttention kernel execution memory blocks tiling se sequence attention steps O(N^2) memory footprint minimize karta hai.",
    84: "📢 <strong>Ek line mein:</strong> Image captioning models CNN encoder features maps ko attention-driven LSTM sequence decoders ke inputs banate hain.",
    85: "📢 <strong>Ek line mein:</strong> Attention weight distributions visual checks aur scores plots se represent karte hain ki model kis sequence coordinate par check kar raha hai.",
    86: "📢 <strong>Ek line mein:</strong> Rotary Position Embeddings sequence indices rotations coordinates calculations vectors parameters apply karke distance scaling adjust karte hain.",
    87: "📢 <strong>Ek line mein:</strong> spaCy NLP pipelines raw documents parser, tagger, tokenizer operations execution steps modular pipelines handle karte hain.",
    88: "📢 <strong>Ek line mein:</strong> POS tagging context rules aur POS models predictions se nouns, verbs, adjectives features components categorize karte hain.",
    89: "📢 <strong>Ek line mein:</strong> Named Entity Recognition texts sequences name locations tokens entities metrics predict karti hai.",
    90: "📢 <strong>Ek line mein:</strong> Dependency parser sentence structures tree relations directions connections trace karta hai.",
    91: "📢 <strong>Ek line mein:</strong> Word2Vec semantic spatial vectors structures coordinate distances similarities mapping words capture karta hai.",
    92: "📢 <strong>Ek line mein:</strong> TF-IDF term frequency document scaling calculations matrices documents dimensions calculate karti hai.",
    93: "📢 <strong>Ek line mein:</strong> Hugging Face pipeline functions multi-task pretrained models layers evaluations wrap karte hain.",
    101: "📢 <strong>Ek line mein:</strong> RAG pipeline external context documents ko prompts vectors index se search karke LLM queries generation augment karta hai.",
    102: "📢 <strong>Ek line mein:</strong> Fine-tuning model internals change karti hai jabki RAG custom knowledge resources data search prompts inputs load karta hai.",
    103: "📢 <strong>Ek line mein:</strong> Vector databases documents chunk embeddings similarities query indexes fast fetch interfaces serve karte hain.",
    104: "📢 <strong>Ek line mein:</strong> Semantic search vector similarity threshold distances indexes comparisons exact syntax comparison se aage handle karta hai.",
    105: "📢 <strong>Ek line mein:</strong> Ragas evaluation framework retrieval precision, faithfulness aur answer relevance parameters ko check karke RAG pipeline ke hallucinations ko spot karta hai.",
    106: "📢 <strong>Ek line mein:</strong> LLM Agents ReAct (Reason + Act) loop se reasoning planning karte hain aur function calling se external tools execute karke tasks accomplish karte hain.",
    107: "📢 <strong>Ek line mein:</strong> Capstone Agentic Systems project search tools, vector databases retrieval aur safe tool execution policies ko integrate karke ek end-to-end autonomous assistant banata hai.",
    108: "📢 <strong>Ek line mein:</strong> Flask API routes definitions incoming client JSON payloads values check methods handle karti hain.",
    109: "📢 <strong>Ek line mein:</strong> Docker container operations complete build context, virtual env libraries dependencies isolated containers wrap karte hain.",
    110: "📢 <strong>Ek line mein:</strong> Gunicorn concurrency workers process queries handling Flask web servers deploy karte hain.",
    111: "📢 <strong>Ek line mein:</strong> Docker volumes mounts weights directory sizes decrease parameters optimize karte hain.",
    112: "📢 <strong>Ek line mein:</strong> Docker layers caching compile dependencies order layers configurations speedup deploy handle karta hai.",
    113: "📢 <strong>Ek line mein:</strong> Multi-stage build process test libraries layers final execution space exclude karke size reduce karti hai.",
    114: "📢 <strong>Ek line mein:</strong> Gradio blocks dynamic layout design model UI components local checks interactively bind karta hai.",
    115: "📢 <strong>Ek line mein:</strong> Spaces config files web routing ports public hosting dynamic check configurations represent karte hain.",
    116: "📢 <strong>Ek line mein:</strong> Docker Compose yaml files local dependencies setup web interfaces ports binding automate karti hain.",
    117: "📢 <strong>Ek line mein:</strong> Integration testing API status checks response content validation parameters loops run karta hai.",
    118: "📢 <strong>Ek line mein:</strong> Production ML pipelines data ingestion models evaluation and inference endpoints deployments trigger karte hain.",
    119: "📢 <strong>Ek line mein:</strong> Kubernetes clusters pod allocations load balancing services serving systems scale up karte hain.",
    120: "📢 <strong>Ek line mein:</strong> Local database container data migrations steps persistent storage volumes synchronize karte hain.",
    121: "📢 <strong>Ek line mein:</strong> Prometheus scraper configs model inference metrics time series databases dashboards alert karte hain.",
    122: "📢 <strong>Ek line mein:</strong> PSI thresholds check checks input statistical drift distributions alerts show karte hain.",
    123: "📢 <strong>Ek line mein:</strong> CI/CD workflows test suites models quality assertions checks automated execute karte hain.",
    124: "📢 <strong>Ek line mein:</strong> Capstone production project metrics model health, docker scale checks complete deploy show karta hai."
}

CUSTOM_MISCONCEPTIONS = {
    33: "Misconception: Accuracy is the best metric for all classification problems. Fact: In highly imbalanced datasets, accuracy can be 99% while the model fails to detect any minority class. Recall or F1-score must be used.",
    35: "Misconception: Grid Search is always superior because it is exhaustive. Fact: Grid Search scale poorly as hyperparameters grow. Random Search finds comparable or better settings in a fraction of the time.",
    36: "Misconception: Naive Bayes handles correlated features perfectly. Fact: The 'naive' assumption is feature independence. Highly correlated features duplicate information, skewing probability estimates.",
    37: "Misconception: Preprocessing parameters (like mean/variance) should be calculated on the whole dataset before splitting. Fact: This is data leakage. Preprocessing parameters must be fit on train only and applied to test.",
    38: "Misconception: R² score represents how correct your model's weights are. Fact: R² only represents the proportion of variance explained. You can have a high R² but still have biased model coefficients.",
    40: "Misconception: Ridge and Lasso regularization behave identically. Fact: Ridge (L2) shrinks coefficients close to zero but keeps all features. Lasso (L1) forces coefficients to exactly zero, eliminating features.",
    41: "Misconception: Gradient descent will always find the global minimum. Fact: In non-convex loss surfaces (like deep learning), gradient descent can easily get stuck in local minima or saddle points.",
    42: "Misconception: Scaling dummy variables (one-hot encoded columns) is required. Fact: Scaling binary columns (0/1) changes their relative weight and breaks their physical meaning. Only scale continuous features.",
    43: "Misconception: High-degree polynomial regression is always better than linear model. Fact: High degree models (degree > 3) capture random noise, leading to extreme overfitting and variance.",
    44: "Misconception: Adjusted R² will always increase when you add more features. Fact: R² always increases, but Adjusted R² penalizes features that do not add predictive power, avoiding false improvements.",
    45: "Misconception: Logistic regression output represents deterministic category labels directly. Fact: Logistic regression outputs a continuous probability between 0 and 1. We must apply a threshold (default 0.5) to get classes.",
    47: "Misconception: A decision tree always splits on the same feature repeatedly. Fact: A tree selects feature splits dynamically at each node by maximizing impurity reduction, using different features down the path.",
    49: "Misconception: XGBoost is immune to overfitting because of tree boosting. Fact: XGBoost can overfit quickly if learning rate (eta) is too high or max_depth is not constrained.",
    50: "Misconception: Tuning tree models only requires finding the best number of estimators. Fact: max_depth and min_samples_leaf are much more critical tree constraints than simple estimator counts.",
    51: "Misconception: Stratified splitting is only useful for binary targets. Fact: Stratification is crucial for multi-class targets to ensure that all class distributions are balanced across train/test splits.",
    52: "Misconception: Perceptrons can solve non-linearly separable relationships (like XOR). Fact: Single-layer perceptrons can only draw straight lines (linear boundaries). XOR requires a hidden layer (non-linear).",
    54: "Misconception: Backpropagation automatically updates model weights. Fact: Backprop only computes the gradient vectors. Optimizers (like SGD or Adam) use those gradients to execute weight updates.",
    55: "Misconception: PyTorch computational graphs are static like TensorFlow 1.x. Fact: PyTorch uses dynamic graphs (Autograd) built on-the-fly during the forward pass, allowing dynamic loops and changes.",
    56: "Misconception: Multi-layer perceptrons require manual weight updates at each step. Fact: Optimizers update weights using learning rates and computed backward gradients, eliminating manual operations.",
    57: "Misconception: Setting initial neural network weights to exactly zero is fine. Fact: If all weights start at zero, hidden neurons compute identical outputs and gradients, halting symmetry breaking.",
    58: "Misconception: PyTorch models should only be saved as whole pickle files. Fact: Saving model state dicts (weights only) is safer and avoids classpath breaks during serialization.",
    59: "Misconception: CNN filters learn fixed patterns specified by the engineer. Fact: CNN filters start with random weights and learn spatial structures (edges, shapes) dynamically via backpropagation.",
    61: "Misconception: Padding changes the channel count of feature maps. Fact: Padding only adds border pixels to control spatial dimensions. Channels are determined by the number of conv filters.",
    62: "Misconception: Skip connections add computational parameters. Fact: Skip connections simply perform identity mapping additions, adding zero parameters to the network weights.",
    63: "Misconception: YOLO predicts classification labels for bounding boxes in a second stage. Fact: YOLO predicts coordinates and classes simultaneously in a single forward pass, making it extremely fast.",
    64: "Misconception: U-Net skip connections add encoder features directly. Fact: U-Net concatenates encoder features along the channel dimension, whereas ResNet adds them element-wise.",
    65: "Misconception: Transfer learning always requires fine-tuning all layers. Fact: If the target dataset is small, fine-tuning all layers will cause overfitting. Freeze base layers and train only the head.",
    66: "Misconception: Vanilla RNNs can store sequence histories indefinitely. Fact: Vanilla RNNs suffer from vanishing gradients, losing context after 10-15 sequence steps.",
    68: "Misconception: LSTM cells gates do not require activation limits. Fact: LSTM gates use sigmoid activations (range 0 to 1) to act as valves, controlling exact information flow.",
    69: "Misconception: GRU cells are always more accurate than LSTM cells. Fact: GRUs are computationally faster and use fewer parameters, but LSTMs can outperform them on long, complex sequence datasets.",
    71: "Misconception: Tokenization splits text by spaces only. Fact: Tokenizers handle punctuation, contractions, and subword parts, mapping raw sequences to vocabulary integer IDs.",
    73: "Misconception: GAN training always converges to a stable global minimum. Fact: GAN optimization is a non-convex minimax game. The generator and discriminator can oscillate indefinitely without converging.",
    75: "Misconception: Conditional GANs ignore input labels during generation. Fact: CGANs append condition parameters to input layers, forcing the model to generate matching targets.",
    76: "Misconception: FID scores are independent of the pre-trained feature model. Fact: FID is calculated using Inception-v3 features. Changes to this feature space break comparability.",
    77: "Misconception: PyTorch Dataset class loads all images into RAM at startup. Fact: Dataset __getitem__ loads images lazily from disk on-the-fly, preventing system RAM exhaustion.",
    78: "Misconception: Training generator and discriminator simultaneously using one optimizer is fine. Fact: GANs require alternating training loops. discriminator weights must freeze when generator updates.",
    79: "Misconception: GAN models are easy to monitor using training loss curves. Fact: GAN loss curves fluctuate and do not indicate output quality. Visual inspections or FID metrics are required.",
    80: "Misconception: Attention mechanisms are recurrent sequence models. Fact: Attention models perform parallel matrix projections, removing sequential dependency bottlenecks.",
    82: "Misconception: KV Caching is used during training of attention models. Fact: KV Caching is strictly an inference optimization tool to speed up auto-regressive token generation.",
    83: "Misconception: FlashAttention changes the mathematical outputs of attention layers. Fact: FlashAttention computes mathematically exact attention. It only optimizes GPU memory access speed.",
    89: "Misconception: NER models require manual dictionary matching for all names. Fact: NER models use sequence contextual vectors to classify name categories, predicting OOV names.",
    90: "Misconception: Dependency parsing tree structures have no loops. Fact: Dependency graphs are directed trees where each word has exactly one head, ensuring loop-free trees.",
    91: "Misconception: Word2Vec embeddings are contextual (e.g. 'bank' in river bank vs money bank). Fact: Word2Vec assigns a static vector per word. Contextual embeddings require transformer networks (BERT).",
    92: "Misconception: TF-IDF matrix values are independent of document count. Fact: IDF scales inversely with document frequency. If a word appears in all documents, its value drops to zero.",
    93: "Misconception: Hugging Face pipelines only run on GPUs. Fact: Pipelines default to CPU execution if CUDA is not configured, running slightly slower.",
    101: "Misconception: RAG systems modify the internal parameters of the LLM. Fact: RAG is strictly in-context learning. It retrieves texts and inserts them into the prompt, keeping LLM weights unchanged.",
    103: "Misconception: Vector databases store document text files inside index matrices. Fact: Vector databases index vector embeddings for similarity searches, linking them back to metadata text sources.",
    104: "Misconception: Cosine similarity captures sentence lengths differences. Fact: Cosine similarity measures the angle between vectors, ignoring magnitude, making it length-invariant.",
    105: "Misconception: RAG evaluation requires human annotations or ground-truth answers for all queries. Fact: Ragas can compute metrics like faithfulness and answer relevance using LLM-as-a-judge capabilities, analyzing just the generated response, context, and query without needing pre-written ground truth.",
    106: "Misconception: AI agents can execute code and tools safely in production without isolation or guardrails. Fact: Agents are prone to prompt injections and infinite execution loops. Tool execution must run in secure, sandboxed environments with strict timeouts and maximum iteration limits.",
    107: "Misconception: Building agentic pipelines simply requires packing multiple tools inside LangChain's AgentExecutor. Fact: Real-world agents require careful routing, custom system prompts, retry policies on tool failure, and fallback plans to be reliable.",
    110: "Misconception: Adding more Gunicorn workers always decreases API latency. Fact: Too many workers saturate CPU cores and cause database bottlenecks, increasing latency. Keep workers bound to core counts.",
    111: "Misconception: Docker images rebuild from scratch when any file changes. Fact: Docker uses layer caching. Only layers *after* the modified file copy layer are rebuilt.",
    112: "Misconception: Docker container volumes copy files inside image layers. Fact: Volumes bypass container layers, mounting host folders directly into active containers.",
    113: "Misconception: Slim base images are identical to standard base images. Fact: Slim base images exclude build tools (gcc, make), requiring multi-stage builds if dependencies need compiling.",
    117: "Misconception: API integration testing should run in production systems. Fact: Integration tests should run in containerized local compose environments before deployment.",
    118: "Misconception: Model tracking registries store model files inside Git repositories. Fact: Model weights are too heavy for Git. registries store references linking to cloud buckets (S3).",
    120: "Misconception: Database container migrations run automatically on container startup. Fact: Migration scripts must be explicitly executed using entrypoint tasks during deployment orchestration.",
    121: "Misconception: Prometheus exporter tracks logs text details. Fact: Prometheus is a metrics aggregator storing numeric time-series values, not logs strings.",
    122: "Misconception: Data drift is always caused by bugs in features pipelines. Fact: Data drift is often caused by external seasonal shifts or user behavior changes over time.",
    123: "Misconception: CI/CD loops replace model performance validations in production. Fact: CI/CD loops verify model code, while monitoring engines verify production input changes.",
    124: "Misconception: High model accuracy guarantees production serving success. Fact: Model serving latency and throughput constraints are equally critical for production deployment."
}

CUSTOM_ANALOGIES = {
    35: "Hyperparameter tuning is like tuning a musical instrument (guitar). You adjust the tuning pegs (hyperparameters) before playing until the sound (output validation score) is perfect.",
    37: "A Scikit-learn Pipeline is like an assembly line in a car factory. Raw parts (raw features) enter on one side, undergo processing (scaling, encoding), and roll out as a complete car (model predictions) at the end.",
    41: "Gradient descent is like hiking down a foggy mountain (loss landscape) with zero visibility. You check the slope under your feet (gradient), take a step downhill (learning rate), and repeat.",
    42: "Data leakage is like a student getting a copy of the final exam questions (test set) during homework study (training). Their study score looks amazing, but their true knowledge is unchecked.",
    44: "A Capstone regression pipeline is like setting up an automated drip irrigation system in a farm. Once configured, water flows from the source (data) through filters (scalers) to crops (model predictions) automatically.",
    49: "XGBoost is like a team of rowers in a boat. The first rower sets the baseline. The second rower corrects the angle of the boat. The third corrects the remaining error, sequentially optimizing the path.",
    50: "Grid search is like checking every combination of shirt and trousers in your wardrobe. Random search is like picking 5 random outfits; you usually find a great look in much less time.",
    51: "A classification pipeline is like a mail sorting center. Letters (raw features) are scanned, stamped (preprocessed), and sorted into bins (classification categories) on a single automated conveyor belt.",
    53: "Activation functions are like threshold switches in neurons. If the incoming signal doesn't cross a certain level (like ReLU clipping negative inputs to 0), the neuron doesn't fire.",
    55: "PyTorch Dynamic Graphs are like drawing on a whiteboard during a meeting. You draw the flow as you speak (run code), modify it dynamically, and erase it at the end.",
    58: "A custom PyTorch MLP is like building a custom brick house. You define the layers (rooms) in the constructor and build the hallways (forward pass) to route traffic between them.",
    65: "Transfer learning is like hiring an experienced commercial driver. They already know how to drive (pre-trained ImageNet filters). You only need to train them on the specific local delivery routes (your custom dataset).",
    70: "A Bidirectional sequence model is like reading a thriller novel. To understand a character's true motive in chapter 5, you sometimes need context from both chapter 1 (past) and chapter 10 (future).",
    72: "Encoder-Decoder models are like translating languages. The encoder reads the full English sentence and summarizes the core idea in their mind (context vector). The decoder translates that idea into Hindi token-by-token.",
    77: "A custom dataset dataloader is like a kitchen assistant. They wash, cut, and portion vegetables (load and transform images) into containers (batches) so the head chef (GPU) can cook without waiting.",
    78: "Alternating training loops in GANs are like a chess match. The generator makes a move (creates an image) while the discriminator sits still. Then the discriminator analyzes the board while the generator freezes.",
    79: "A Capstone GAN project is like an art forge. An apprentice (generator) prints replicas while an art critic (discriminator) spots details, refining the style over epochs.",
    88: "POS Tagging is like parsing a sentence structure in grammar school. You highlight nouns in blue, verbs in red, and adjectives in green to map out sentence meanings.",
    89: "Named Entity Recognition is like a post office clerk scanning letters to highlight zip codes, names, and city coordinates dynamically.",
    90: "Dependency Parsing is like drawing a family tree of a sentence. It maps which word (child) depends on which other word (parent) to establish grammatical connections.",
    91: "Word2Vec is like mapping cities on a coordinate globe. London and Paris are spatially close in coordinates, while Tokyo is far. Similarly, 'king' and 'queen' have close word coordinates.",
    92: "TF-IDF is like indexing a library. The word 'the' appears in every book, so it has zero index value. The word 'autograd' appears in only three books, making it highly valuable.",
    93: "Hugging Face pipelines are like vending machines. You select the task (e.g., translation), insert raw coins (text input), and get the target soda (translated text) instantly.",
    105: "Ragas evaluation is like hiring an editor to grade a research paper. They check if the citations match the text (faithfulness) and if the text actually answers the prompt (relevance).",
    106: "AI agents are like smart customer support executives who have access to a calculator, search engine, and booking database. They don't just answer questions; they think, use the calculator, search the web, and book tickets on your behalf.",
    107: "Building an agentic pipeline is like setting up an automated office assistant. You configure the routing rules, register the tools, specify safety parameters, and let it run tasks autonomously while keeping audit logs.",
    114: "Gradio is like setting up a tasting table outside your kitchen. You don't need to build a restaurant (web app); you just place plates (input sliders, output text) for users to sample the food.",
    115: "Hugging Face Spaces is like posting a video on YouTube. Instead of hosting a server, you upload the app repository, and Hugging Face serves it to the public for free.",
    116: "Docker Compose is like organizing a stage performance. You write a script (yml file) specifying when the lights (databases), audio (backend API), and actors (frontend) should coordinate.",
    117: "API integration testing is like running a practice fire drill in a building. You simulate the emergency (client requests) to verify that all exits and alarms (API endpoints) function correctly.",
    120: "Database migrations are like updating a city blueprint. You write changes to water pipes (schema columns) step-by-step so active buildings don't lose utility services.",
    122: "Concept drift is like trying to sell winter coats in a hot summer. Your store catalog (model weights) is perfect, but customer behavior (input data distribution) has shifted completely.",
    123: "CI/CD MLOps pipelines are like automated airport security checks. Baggage (code changes) passes through scanners (unit tests) and passenger identities are verified before anyone boards the plane.",
    124: "A Capstone production project is like launching a commercial rocket. You configure booster weights (model files), check telemetry (monitoring), and scale engines (docker clusters) for launch."
}

# Main processing loop to inject missing visual boxes
def inject_missing_visuals():
    for w in range(5, 19):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        print(f"Checking week{w}.html for missing boxes...")
        content = open(path, 'r', encoding='utf-8').read()
        
        days = WEEKS_DAYS[w]
        modified = False
        
        for d in days:
            day_marker = f'id="day-{d}"'
            if day_marker + ">" in content:
                day_marker = day_marker + ">"
            elif day_marker + " " in content:
                # If there are other attributes or spaces
                day_marker = day_marker
            elif f"id='day-{d}'>" in content:
                day_marker = f"id='day-{d}'>"
            else:
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
            if day_end_idx == -1:
                day_end_idx = header_and_body.find("</div><!-- /day-")
            if day_end_idx == -1:
                day_end_idx = len(header_and_body)
                
            day_body = header_and_body[:day_end_idx]
            remainder = header_and_body[day_end_idx:]
            
            day_modified = False
            
            # --- Check Misconception ---
            has_misconception = 'class="misconception"' in day_body or 'Misconception:' in day_body
            if not has_misconception:
                miscon = CUSTOM_MISCONCEPTIONS.get(d) or get_misconception(d, DAY_TOPICS.get(d, "this concept"))
                miscon_html = f"""
  <div class="misconception">
    <strong>⚠️ Common Misconception:</strong> {miscon.split('Fact:')[0].replace('Misconception:', '').strip()}
    <br><br>
    <strong>Fact:</strong> {miscon.split('Fact:')[1].strip() if 'Fact:' in miscon else miscon}
  </div>
"""
                tak_idx = day_body.find('class="takeaways"')
                if tak_idx != -1:
                    div_start = day_body.rfind('<div', 0, tak_idx)
                    if div_start != -1:
                        day_body = day_body[:div_start] + miscon_html + day_body[div_start:]
                        day_modified = True
                    
            # --- Check Hinglish ---
            has_hinglish = 'class="hinglish"' in day_body or 'Ek line mein:' in day_body
            if not has_hinglish:
                hinglish = CUSTOM_HINGLISH.get(d) or get_hinglish(d, DAY_TOPICS.get(d, "this concept"))
                hinglish_html = f"""
  <div class="hinglish">
    {hinglish}
  </div>
"""
                tak_idx = day_body.find('class="takeaways"')
                if tak_idx != -1:
                    tak_list_idx = day_body.find('<ol>', tak_idx)
                    if tak_list_idx == -1:
                        tak_list_idx = day_body.find('<ul>', tak_idx)
                    if tak_list_idx != -1:
                        day_body = day_body[:tak_list_idx] + hinglish_html + day_body[tak_list_idx:]
                        day_modified = True
                    else:
                        # Append after takeaways title
                        tak_title_idx = day_body.lower().find('<h3', tak_idx)
                        if tak_title_idx != -1:
                            close_h3 = day_body.find('</h3>', tak_title_idx)
                            if close_h3 != -1:
                                day_body = day_body[:close_h3+5] + hinglish_html + day_body[close_h3+5:]
                                day_modified = True
                            
            # --- Check Analogy ---
            has_analogy = 'class="analogy"' in day_body or 'Analogy:' in day_body
            if not has_analogy:
                analogy = CUSTOM_ANALOGIES.get(d) or get_analogy(d, DAY_TOPICS.get(d, "this concept"))
                analogy_html = f"""
  <div class="analogy">{analogy}</div>
"""
                # Insert at the beginning of the theory section
                theory_pos = day_body.find('id="theory"')
                if theory_pos != -1:
                    day_body = day_body[:theory_pos+12] + analogy_html + day_body[theory_pos+12:]
                    day_modified = True
                else:
                    day_body = analogy_html + day_body
                    day_modified = True
                    
            if day_modified:
                content = parts[0] + day_marker + day_body + remainder
                modified = True
                
        if modified:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Successfully filled gaps in week{w}.html!")

if __name__ == '__main__':
    inject_missing_visuals()
    print("\nVisual content blocks gaps filled successfully!")
