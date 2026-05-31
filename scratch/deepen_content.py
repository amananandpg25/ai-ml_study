import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# ══════════════════════════════════════════════════════════════════════════════
# DATA DEFINITIONS
# ══════════════════════════════════════════════════════════════════════════════

# 1. Indian Company Connections (Weeks 5-17)
INDIAN_CONNECTIONS = {
    # Week 5
    31: "Swiggy utilizes supervised learning to predict estimated delivery times (regression) and unsupervised clustering to group delivery partners by area density.",
    32: "Zomato tracks Mean Absolute Error (MAE) for food preparation time estimates to make sure users aren't left waiting with false expectations.",
    33: "Razorpay uses precision-recall thresholds for classification: a false positive (flagging normal payment as fraud) causes user dropoff, while a false negative costs money.",
    34: "Flipkart models face overfitting during Big Billion Days if their recommendation engines over-specialize on historical seasonal trends.",
    35: "MakeMyTrip uses automated hyperparameter optimization to find the best flight pricing elasticity models for major holidays.",
    36: "Lenskart uses a KNN-like similarity search in feature spaces to recommend glasses frames that match your uploaded face scan shape.",
    37: "JioCinema uses Scikit-learn pipelines to transform incoming demographic data and serve initial content recommendation rankings.",
    # Week 6
    38: "Housing.com uses Linear Regression to compute base property valuations across Delhi NCR based on square footage and distance to metro stations.",
    39: "NoBroker calculates the relative weight of flat amenities (pool, gym, parking) on rent using Multiple Linear Regression models.",
    40: "MagicBricks applies Ridge and Lasso regularization to housing price predictions to drop noise from highly correlated features (like number of bedrooms vs bathrooms).",
    41: "Ola uses gradient descent optimization to dynamically adjust cab ride fares based on demand-supply ratios in real-time.",
    42: "Delhivery scales distance and package weight coordinates using StandardScaler to prevent large numbers from overwhelming routing models.",
    43: "Swiggy Instamart calculates polynomial regression features to model the non-linear surge of item demand during rainstorms.",
    44: "Tata 1mg builds automated pipeline models using OLS regressions to forecast monthly inventory needs for chronic medicine categories.",
    # Week 7
    45: "Paytm uses Logistic Regression to model the probability of a user defaulting on their Paytm Postpaid loans based on transactional history.",
    46: "Razorpay employs Support Vector Machines (SVMs) with non-linear kernels to draw complex boundaries separating normal payments from high-risk fraud signatures.",
    47: "Flipkart uses Decision Trees to guide customer support chatbots, routing users through diagnostic nodes (e.g. 'Is item damaged?' -> Yes/No).",
    48: "PhonePe trains Random Forests on customer device metrics to predict app crashes and latency bottlenecks across different Android versions.",
    49: "Groww utilizes XGBoost as their primary tabular classifier to predict user propensity to invest in mutual funds vs direct equity.",
    50: "Urban Company fine-tunes hyperparameters of their service allocation classifiers using grid search to match local service providers efficiently.",
    51: "MakeMyTrip's capstone classifier uses tree-based ensembles to predict user booking cancellations during monsoon seasons.",
    # Week 8
    52: "Paytm's early fraud alert systems were based on single-layer perceptrons mapping transactional features to binary risk scores.",
    53: "Dream11 uses neural network activation functions to model complex, non-linear relationships between fantasy player statistics and final points.",
    54: "InMobi trains multi-layer neural networks via backpropagation to optimize real-time ad click-through rate (CTR) prediction algorithms.",
    55: "Myntra uses PyTorch dynamic computation graphs to rapidly test experimental recommendation network architectures for fashion items.",
    56: "Ola Maps uses multi-layer neural networks to predict estimated time of arrival (ETA) through complex urban traffic grids.",
    57: "Razorpay scales payment risk variables to mean 0 and variance 1 to avoid activation saturation during neural network inference.",
    58: "Zomato's prediction servers deploy PyTorch models to production using specialized serialization engines to handle high concurrency.",
    # Week 9
    59: "Ola detects and reads vehicle license plates at automated toll booths using deep Convolutional Neural Networks.",
    60: "Flipkart searches visual catalogs by using max pooling layers in CNNs to extract translation-invariant patterns of shoes or shirts.",
    61: "Ajio builds custom PyTorch CNNs to extract edge, texture, and style feature representations from uploaded fashion images.",
    62: "Nikaa uses deep residual networks (ResNets) to classify skin types and textures from user selfies for personalized makeup matches.",
    63: "Ola Cabs uses YOLO object detection models to capture street sign coordinates and speed limits from dashcam video feeds.",
    64: "Netmeds uses U-Net models for semantic segmentation, isolating lung areas in chest X-ray scans to help spot infection sites.",
    65: "Myntra uses Transfer Learning from ImageNet pre-trained ResNets to build custom catalog classification models for new clothing seasons.",
    # Week 10
    66: "MakeMyTrip utilizes Recurrent Neural Networks (RNNs) to parse sequential flight search queries and recommend dynamic package deals.",
    67: "Flipkart sentiment analyzer parses raw product reviews character-by-character using recurrent networks to identify negative reviews early.",
    68: "Swiggy uses LSTMs to model weekly sequence dynamics of kitchen inventory demands, avoiding food wastage.",
    69: "BookMyShow uses GRUs to analyze real-time sequence patterns of seat selections, flagging automated ticket-booking bots.",
    70: "Paytm uses Bidirectional LSTMs to process transaction histories forward and backward, spotting suspicious cash-out sequences.",
    71: "Zomato analyzes customer chat transcripts using sequence models to automate instant refund approvals for missing orders.",
    72: "Tata 1mg uses sequence-to-sequence models to translate medical jargon in doctor prescriptions into simple patient advice summaries.",
    # Week 11
    73: "Myntra uses Generative Adversarial Networks (GANs) to generate synthetic fashion model shoots, cutting photography costs.",
    74: "Flipkart experiments with Deep Convolutional GANs (DCGANs) to synthesize new pattern designs for custom apparel lines.",
    75: "Nykaa utilizes GANs to overlay lipstick shades and cosmetic colors realistically onto user video feeds for virtual try-ons.",
    76: "Dream11 simulates fantasy league outcomes by generating synthetic match trajectories using GAN-like adversarial training paradigms.",
    77: "Meesho uses synthetic image generation to create diverse background settings for vendor product photos automatically.",
    78: "InMobi utilizes adversarial networks to simulate user ad clicks, testing stability of downstream analytical engines.",
    79: "Urban Company generates synthetic customer query datasets using GANs to stress-test their customer service routing pipelines.",
    # Week 12
    80: "Flipkart uses attention mechanisms to align words in search queries (e.g., 'blue water-resistant running shoes') to product catalog attributes.",
    81: "Ola Maps uses Bahdanau attention to match street sign visual text inputs with destination database tokens during sequence decoding.",
    82: "Tata 1mg uses Luong attention models to decode handwritten doctor prescriptions, translating them into medicine stock codes.",
    83: "Zomato uses visual attention networks to scan restaurant menu photos, extracting names and prices dynamically.",
    84: "Swiggy uses image captioning attention models to describe dishes from user photos, automatically tagging them as vegetarian or gluten-free.",
    85: "Paytm uses attention weights over user transaction history sequences to identify changing financial behavior patterns.",
    86: "MakeMyTrip uses cross-attention models to translate complex holiday itinerary queries into scheduled flight and hotel bookings.",
    # Week 13
    87: "Inshorts uses spaCy pipelines for tokenization, breaking down raw news articles into sentence chunks for their 60-word summaries.",
    88: "Flipkart parses reviews using POS tagging to isolate adjectives (e.g. 'comfortable', 'slow') and link them to nouns (e.g. 'seat', 'battery').",
    89: "Razorpay uses Named Entity Recognition (NER) to scan KYC PDF documents, automatically extracting PAN numbers and director names.",
    90: "Myntra uses dependency parsing to interpret complex search queries like 'kurta with red print but no sleeves'.",
    91: "Swiggy clusters customer support emails using Word2Vec semantic embeddings to route complaints to specialized human agents.",
    92: "Paytm uses TF-IDF vectorization to match customer search terms with their internal banking FAQ documentation database.",
    93: "Tata 1mg uses Hugging Face pipeline models to run classification on drug interaction queries, flagging dangerous combinations.",
    # Week 14
    94: "Flipkart uses Self-Attention layers to capture contextual relationships between search queries and purchased items in high dimensions.",
    95: "Razorpay runs pre-LN Transformer blocks on transaction sequence streams to detect multi-card fraud trails across different merchant outlets.",
    96: "JioCinema uses BERT model variations to perform sentiment extraction on live sports comment feeds at massive scale.",
    97: "Tata 1mg uses custom tokenizers trained on medical corpora to preserve chemical names (like Acetaminophen) without splitting them into fragments.",
    98: "Swiggy uses light GPT-2 models (nanoGPT style) to generate automated responses for delivery partners during active runs.",
    99: "MakeMyTrip fine-tunes BERT models to categorize flight cancellation reasons from email text into structured reimbursement codes.",
    100: "Ola deploys localized conversational bots onto Hugging Face Spaces to test Hinglish chat support layouts for auto drivers.",
    # Week 15
    101: "Zomato uses RAG systems with LLMs to allow customer service agents to instantly search restaurant policy documents.",
    102: "Paytm embeds transactional rulebooks into LangChain structures, allowing support bots to verify refunds against compliance rules.",
    103: "Flipkart uses vector databases (like Chroma) to index product catalogs, enabling visual search (upload a shirt, find similar shirts).",
    104: "Groww uses vector databases to store financial market disclosures, facilitating semantic search across thousands of PDFs.",
    105: "Tata 1mg uses RAG pipelines to answer customer questions about medicine side effects by querying a verified medical drug database.",
    106: "PhonePe uses LangChain evaluation tools to monitor support LLMs for hallucinations regarding transaction fee details.",
    107: "Lenskart uses a complete RAG application to recommend glasses frames based on style profiles and face measurements stored in vector databases.",
    # Week 16
    108: "Razorpay deploys ML models as Flask APIs inside secure private subnets to handle real-time fraud scoring for merchant checkouts.",
    109: "Swiggy containerizes their route optimization engines inside Docker to ensure they scale reliably during high-demand lunch rushes.",
    110: "Urban Company deploys Gunicorn servers with Flask to handle concurrent bookings from millions of active users.",
    111: "Zomato serves real-time delivery coordinate predictions using Flask APIs deployed on auto-scaling cloud clusters.",
    112: "Paytm packages their credit risk models inside Docker containers to run identical pipelines on local development machines and production servers.",
    113: "MakeMyTrip uses multi-stage Docker builds to reduce the size of their flight recommendation microservices from 2GB to 300MB.",
    114: "Tata 1mg builds Gradio web applications to allow medical experts to visually audit prescription classification models.",
    115: "Meesho deploys Gradio interfaces to allow small vendors to verify synthetic background replacement models before uploading product photos.",
    116: "Groww uses Docker Compose to set up local dev environments consisting of a Flask API, a Redis cache, and a PostgreSQL database.",
    117: "PhonePe runs automated API endpoint integration testing inside Docker Compose to verify that changes don't disrupt payment flows.",
    # Week 17
    118: "Delhivery deploys shipping routing models in production, exposing predictions via fast APIs to regional hub sorting networks.",
    119: "Paytm containerizes their transaction monitoring pipeline using multi-stage Dockerfiles to run in microservice architectures.",
    120: "Myntra runs local testing of recommendation web dashboards using Docker Compose, linking databases and frontend frameworks.",
    121: "Razorpay sets up Prometheus metrics on their model serving endpoints to trigger alerts if fraud check latency exceeds 50ms.",
    122: "Groww deploys their final portfolios with automated Docker health checks, monitoring model degradation in real production markets.",
    123: "Zomato integrates model deployments with active CI/CD pipelines, automatically running safety tests before exposing endpoints to customers.",
    124: "Ola builds a comprehensive portfolio project showing real-time driver-rider match prediction deployed inside container clusters.",
    125: "Tata Communications uses Kubernetes to orchestrate their containerized edge routing models across regional clusters.",
    126: "Haptik deploys and updates their customer service conversational models on Render/Railway using continuous integration hooks.",
    127: "Pine Labs monitors their fraud detection models using MLflow to track real-time accuracy and prediction thresholds.",
    128: "Infosys defines complete ML system specs, detailing pipelines, databases, and container nodes for corporate clients.",
    129: "Wipro indexes large legal documents into vector databases to build smart internal compliance search assistants.",
    130: "Cognizant containerizes high-concurrency client APIs using optimized Docker multi-stage build pipelines.",
    131: "Swiggy integrates user interfaces with model serving REST API endpoints to calculate delivery partner allocation paths.",
    132: "L&T technology services publishes fully documented repos with architecture diagrams on GitHub for portfolio display.",
    133: "Tech Mahindra engineers optimize their profiles with high-impact MLOps keywords to stand out in recruiter searches.",
    134: "TCS recruits face mock technical drills covering binary cross entropy, decision boundary margin maximization, and optimizer parameters.",
    135: "HCL hosts final graduation projects showcasing scaled deployment of machine learning workflows."
}

# 2. "Why does this work?" Math Intuition (Weeks 5-9)
MATH_INTUITIONS = {
    # Week 5
    36: "KNN works because of the <strong>homophily principle</strong> (similarity implies proximity). Mathematically, we measure distance in an N-dimensional vector space using Euclidean distance $d(p, q) = \\sqrt{\\sum (p_i - q_i)^2}$. If features are normalized, points closer in distance are highly likely to share the same label because decision boundaries in nature are usually smooth rather than chaotic. Naive Bayes works by applying <strong>Bayes' Theorem</strong> with the 'naive' assumption that all features are conditionally independent given the class label. Mathematically: $P(y|X) = \\frac{P(X|y)P(y)}{P(X)} \\propto P(y) \\prod P(x_i|y)$. This converts a massive joint probability estimation (which would require infinite data) into a product of simple, independent 1D conditional probabilities, making it extremely fast and highly effective for text.",
    # Week 6
    38: "Linear Regression works by finding the line that minimizes the sum of squared differences between observed values and predictions. Mathematically, it minimizes Mean Squared Error (MSE): $J(m, c) = \\frac{1}{n}\\sum(y_i - (mx_i + c))^2$. Squaring the errors ensures they are positive and penalizes larger errors more heavily. The derivatives $\\frac{\\partial J}{\\partial m}$ and $\\frac{\\partial J}{\\partial c}$ guide us to the exact minimum.",
    39: "Ordinary Least Squares (OLS) works because it has a closed-form analytical solution. Mathematically, we solve $\\hat{\\beta} = (X^T X)^{-1} X^T y$ by setting the gradient of the sum of squared residuals to zero. The term $(X^T X)^{-1}$ projects the target vector $y$ onto the column space of the feature matrix $X$, finding the closest possible linear combination.",
    40: "Regularization works by adding a penalty to the loss function to constrain coefficient sizes. Ridge (L2) adds $\\lambda \\sum \\beta_j^2$, drawing coefficients close to zero but not exactly zero (due to the circular/spherical constraint). Lasso (L1) adds $\\lambda \\sum |\\beta_j|$, which creates a diamond-shaped constraint space whose sharp corners intersect the axis, forcing some coefficients to exactly zero, thereby performing automatic feature selection.",
    # Week 7
    45: "Logistic Regression works because it models probabilities using the Sigmoid function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$, which maps any real-valued number to $[0, 1]$. To train it, we minimize the binary cross-entropy loss (negative log-likelihood): $J(w) = -\\frac{1}{n}\\sum [y_i \\log(\\hat{y}_i) + (1-y_i) \\log(1-\\hat{y}_i)]$. This loss is convex, meaning gradient descent is guaranteed to find the global minimum without getting stuck.",
    46: "Support Vector Machines work by maximizing the geometric margin between classes. Mathematically, it solves $\\min \\frac{1}{2}||w||^2$ subject to $y_i(w^T x_i + b) \\ge 1$. The margin is $\\frac{2}{||w||}$. By maximizing this margin, we find the decision boundary that is furthest from the closest training points (support vectors), maximizing generalizability. Kernels project data to a higher-dimensional space where it becomes linearly separable.",
    47: "Decision Trees work by recursively partitioning the feature space to maximize purity in child nodes. Mathematically, at each node, it selects the split that maximizes Information Gain (reduction in Entropy: $H(S) = -\\sum p_i \\log_2 p_i$) or Gini Impurity ($G = 1 - \\sum p_i^2$). By making nodes as pure as possible, the tree quickly converges on a set of logical rules that classify the data.",
    48: "Random Forests work because of <strong>ensemble variance reduction</strong>. According to probability theory, the variance of the average of $B$ independent, identically distributed random variables is $\\frac{\\sigma^2}{B}$. By bootstrapping training data (bagging) and selecting a random subset of features at each split, we create highly de-correlated trees. Averaging their predictions dramatically reduces variance (overfitting) without increasing bias.",
    49: "Gradient Boosting works by training trees sequentially to predict the <strong>residuals</strong> (errors) of the preceding trees. Mathematically, it performs gradient descent in the function space. Each new tree fits the negative gradient of the loss function with respect to the current predictions: $r_{im} = -\\left[\\frac{\\partial L(y_i, f(x_i))}{\\partial f(x_i)}\\right]_{f=f_{m-1}}$. Summing these weak learners creates an extremely robust model.",
    # Week 8
    52: "The Perceptron works because its learning rule is guaranteed to converge if the data is linearly separable (Perceptron Convergence Theorem). Mathematically, it updates weights only when it makes a mistake: $w \\leftarrow w + \\eta(y_i - \\hat{y}_i)x_i$. If the target is $1$ and prediction is $0$, it adds $x_i$ to $w$, bringing the weight vector closer to the misclassified point.",
    53: "Activation functions work because they introduce non-linear mapping capabilities. Without them, a multi-layer neural network is mathematically equivalent to a single-layer linear model: $W_2(W_1 x + b_1) + b_2 = (W_2 W_1)x + (W_2 b_1 + b_2) = W'x + b'$. Non-linear activations like ReLU, Sigmoid, or Tanh allow the network to approximate any continuous function (Universal Approximation Theorem).",
    54: "Backpropagation works by applying the <strong>chain rule of calculus</strong> to efficiently calculate the gradient of a loss function with respect to all weights in the network. Instead of computing gradients from scratch for each weight (which is computationally prohibitive), backprop propagates error signals backward from output to input, storing intermediate derivatives. This dynamic programming approach reduces the time complexity from $O(N^2)$ to $O(N)$.",
    # Week 9
    59: "CNNs work because they exploit spatial structures in images using <strong>weight sharing</strong> and <strong>local receptive fields</strong>. Mathematically, a convolution operation slides a small filter over the image, computing dot products at each position: $S(i,j) = (I * K)(i,j) = \\sum \\sum I(i-m, j-n) K(m,n)$. This detects local patterns (edges, textures) regardless of their position in the image, dramatically reducing parameter count compared to fully-connected layers.",
    60: "Pooling works by introducing <strong>translation invariance</strong> and reducing spatial dimensionality. Max pooling extracts the maximum value within a window: $P(i,j) = \\max(x_{m,n})$. This keeps the most dominant features (e.g. active edges) while discarding exact spatial coordinates, making the network robust to small translations and rotations of the input, while lowering computational memory requirements."
}

# 3. Failure Cases (Weeks 5-17)
FAILURE_CASES = {
    # Week 5
    31: ("ValueError: Found input variables with inconsistent numbers of samples", "Training data X and labels y have a different number of rows (e.g., shape mismatch).", "Check the length of both inputs before calling train_test_split. Ensure len(X) == len(y)."),
    32: ("ValueError: Mean Squared Error yields NaN / infinity", "Target values contain missing values (NaN) or inputs have extreme outliers causing overflow.", "Use df.isna().sum() to verify no nulls, and clean or scale features using StandardScaler before calculating loss."),
    33: ("ValueError: Target is multiclass but average='binary'", "Trying to calculate binary classification metrics (like precision/recall) on a dataset with more than 2 classes.", "Specify the average parameter in the metric call: precision_score(y_true, y_pred, average='macro') or 'micro'."),
    34: ("Overfitting / validation loss going up while train loss goes down", "Model capacity is too high for the amount of data, or training has run for too many iterations.", "Apply L1/L2 regularization, reduce features, or use early stopping to halt training when validation performance peaks."),
    35: ("ValueError: Parameter grid is empty or invalid key", "Dictionary keys in param_grid do not match the exact parameter names of the scikit-learn estimator.", "Print estimator.get_params().keys() to verify the correct parameter names and check for spelling/formatting typos."),
    36: ("ValueError: Expected 2D array, got 1D array instead", "Passing a single sample (1D array) to model.predict() or model.fit() in Scikit-learn.", "Reshape the single sample using input_data.reshape(1, -1) before calling model.predict()."),
    37: ("ValueError: Pipeline steps must be list of tuples", "Passing estimators directly to the Pipeline constructor without wrapping them in named tuples.", "Define steps as a list of tuples: [('scaler', StandardScaler()), ('clf', LogisticRegression())]."),
    # Week 6
    38: ("LinAlgError: Singular matrix", "Features are perfectly collinear (one feature is a linear combination of others), making matrix inversion impossible.", "Remove highly correlated features using df.drop() or add L2 regularization (Ridge) to stabilize the matrix inversion."),
    39: ("ValueError: Expected 2D array, got 1D array instead", "Passing a 1D array for X (features) to LinearRegression().fit() instead of a 2D column vector.", "Reshape X using X.values.reshape(-1, 1) or specify it as double brackets df[['feature_name']]."),
    40: ("Model coefficients shrink to exactly zero when alpha is too high in Lasso", "The regularization strength hyperparameter alpha is set too large, penalizing the weights too heavily.", "Tune alpha using grid search (LassoCV) over a logarithmic scale like np.logspace(-4, 2, 100)."),
    41: ("Loss goes to infinity (NaN) during gradient descent updates", "The learning rate is set too high, causing weight updates to overshoot the minimum and diverge.", "Reduce the learning rate (e.g. from 0.1 to 0.001) or implement gradient clipping/scaling."),
    42: ("ValueError: X has 10 features, but LinearRegression is expecting 8 features", "Features passed to predict() do not match the shape or column names of features used in fit().", "Ensure that the preprocessing pipeline applied to the test set is identical to the one applied to the training set."),
    43: ("ValueError: Polynomial features contain extremely large numbers leading to overflow", "Using high degree polynomials (degree > 5) on unscaled data, causing numerical instability.", "Scale features with StandardScaler or MinMaxScaler *before* applying PolynomialFeatures."),
    44: ("KeyError: 'column_name' not found in DataFrame", "Pipeline step tries to transform a column name that was dropped or renamed in a previous pipeline step.", "Double check the order of steps in ColumnTransformer and verify output feature names at each stage."),
    # Week 7
    45: ("ConvergenceWarning: lbfgs failed to converge (status=1): STOP: TOTAL NO. of ITERATIONS REACHED", "The optimizer did not find the global minimum within the default number of iterations.", "Increase max_iter in LogisticRegression(max_iter=1000) or apply feature scaling to help the solver converge faster."),
    46: ("ValueError: The number of features in the input samples does not match...", "The input dimensions to SVM predict do not match the dimensions on which the SVM was trained.", "Check shape of test input. Ensure it has been transformed by the exact same scaler used during training."),
    47: ("Overfitting / Decision Tree grows extremely deep with 100% train accuracy but very low test accuracy", "No depth constraints are set, allowing the tree to split until every leaf is perfectly pure.", "Constrain model capacity by setting max_depth (e.g. max_depth=5) or min_samples_leaf in the constructor."),
    48: ("Performance bottleneck: Random Forest training takes extremely long time", "Training a high number of deep estimators sequentially on a single CPU core.", "Set n_jobs=-1 in the Random Forest constructor to enable multi-core parallel training."),
    49: ("XGBoostError: Clean your column names! Graphic characters like [ or ] are not allowed.", "Feature names contain special characters (like JSON bracket notation) which breaks XGBoost's parser.", "Rename columns using df.columns = [c.replace('[','').replace(']','') for c in df.columns] before training."),
    50: ("IndexError: list index out of range in GridSearchCV.best_params_", "Trying to access parameters from grid search when the fitting process failed due to errors in all folds.", "Check grid fitting logs to resolve primary exceptions. Set error_score='raise' to debug issues immediately."),
    51: ("ValueError: Input contains NaN, infinity or a value too large for dtype('float64')", "Missing values or infinities are present in the final dataset passed to the classifier.", "Impute missing values using SimpleImputer() or drop rows containing nulls using df.dropna()."),
    # Week 8
    52: ("RuntimeError: Perceptron does not converge", "Attempting to train a single-layer perceptron on non-linearly separable data (like the XOR gate problem).", "Use a Multi-Layer Perceptron (MLP) with a hidden layer and non-linear activation functions (like ReLU)."),
    53: ("RuntimeError: Gradients are zero (Vanishing Gradients)", "Training a deep network using Sigmoid/Tanh activations, causing gradients to shrink to zero in early layers.", "Replace Sigmoid/Tanh activations in hidden layers with ReLU or Leaky ReLU activations."),
    54: ("RuntimeError: w1.grad is None after loss.backward()", "Forgetting to set requires_grad=True on inputs/weights, or performing operations in-place preventing gradient tracking.", "Initialize parameter tensors with requires_grad=True and avoid in-place operations like w1 += grad."),
    55: ("RuntimeError: CUDA out of memory", "Attempting to load too many samples or a model that is too large into GPU RAM.", "Reduce the batch_size (e.g. from 128 to 32) or run torch.cuda.empty_cache() to clear garbage tensors."),
    56: ("RuntimeError: Expected object of device type cuda but got device type cpu for argument", "Tensors in a single operation are located on different devices (one on CPU, one on GPU).", "Move all parameters and input tensors to the same device using .to(device) or .cuda()/.cpu()."),
    57: ("RuntimeError: loss.backward() called a second time", "Attempting to run backprop multiple times without retaining the computation graph.", "Set retain_graph=True in loss.backward(retain_graph=True) if you explicitly need to backprop twice."),
    58: ("RuntimeError: Attempting to serialize a model containing lambda functions", "Python pickle module cannot serialize anonymous lambda functions during state saving.", "Replace lambdas with standard named functions or save only the state dict using torch.save(model.state_dict(), path)."),
    # Week 9
    59: ("RuntimeError: Given groups=1, weight of size [16, 3, 3, 3] expected input [32, 1, 28, 28] to have 3 channels...", "CNN input shape has a different number of channels than what the first Conv2D layer expects.", "Reshape or unsqueeze the input tensor to include the channel dimension (e.g. shape [batch, channels, height, width])."),
    60: ("RuntimeError: Negative spatial dimensions after MaxPool2d", "Applying pooling operations repeatedly on small images, reducing spatial dimensions to zero.", "Check image input sizes and adjust MaxPool stride/kernel sizes, or reduce the number of pooling layers."),
    61: ("RuntimeError: Expected 4D tensor as input, got 3D tensor instead", "Passing a single image tensor of shape [channels, height, width] to a PyTorch CNN.", "Add a batch dimension at index 0 using image_tensor.unsqueeze(0) to make it [1, channels, height, width]."),
    62: ("RuntimeError: Output size mismatch in skip connection addition (ResNet)", "Attempting to add residual input x to conv output F(x) when height, width, or channel counts differ.", "Apply a 1x1 projection convolution with matching stride to x to match shapes before addition."),
    63: ("RuntimeError: NMS outputs empty bounding boxes", "Confidence thresholds are set too high, filtering out all proposed boxes.", "Lower the confidence score threshold (e.g. to 0.15) to inspect raw predictions before running NMS."),
    64: ("RuntimeError: U-Net concatenation shape mismatch", "Encoder crop shape does not match decoder upsampled shape during skip connection concatenation.", "Ensure padding='same' is used in convolutions, or crop the encoder tensor to match the decoder tensor size."),
    65: ("RuntimeError: Target size (torch.Size([32])) must be the same as input size (torch.Size([32, 10]))", "Loss function (like BCELoss) expects single-channel outputs, but classifier output has multiple classes.", "Use CrossEntropyLoss for multiclass outputs, or ensure the final output layer has a single node for binary targets."),
    # Week 10
    66: ("RuntimeError: RNN input shape mismatch: expected [seq_len, batch, input_size] but got...", "PyTorch RNNs expect sequence dimensions in a specific order depending on the batch_first parameter.", "Set batch_first=True in the RNN constructor or permute input dimensions using tensor.transpose(0, 1)."),
    67: ("RuntimeError: Exploding Gradients (Loss yields NaN or weights overflow)", "Unbounded recurrent state multiplications over long sequences causing exponential gradient growth.", "Implement gradient clipping using torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)."),
    68: ("LSTM performance bottleneck: training is extremely slow", "Processing long sequence loops sequentially in Python instead of vectorized batch operations.", "Set batch_first=True, pack sequences using pack_padded_sequence, and ensure you use GPU acceleration."),
    69: ("Model fails to learn long-term dependencies in long text passages", "Vanilla RNNs suffer from vanishing gradients, losing context after 10-15 tokens.", "Replace vanilla RNN layers with LSTM or GRU layers which use gates to preserve memory over longer sequences."),
    70: ("RuntimeError: Trying to backward through the graph a second time...", "Forgetting to detach hidden states between batch sequences in truncated BPTT.", "Call hidden.detach() or h.detach_() on hidden state variables before passing them to the next sequence step."),
    71: ("IndexError: index out of range in embedding layer", "Passing integer token IDs that are greater than or equal to the specified vocabulary size in nn.Embedding.", "Ensure token IDs are clipped to [0, vocab_size - 1] or increase the vocab_size parameter in the embedding layer constructor."),
    72: ("RuntimeError: Encoder-Decoder sequence lengths mismatch in Cross-Attention", "Decoder query dimensions and encoder key/value dimensions do not align.", "Verify that query projection weight matrices and key projection weight matrices project tensors to matching dimensions."),
    # Week 11
    73: ("RuntimeError: GAN Generator collapses to outputting identical images (Mode Collapse)", "The generator finds a single output pattern that fools the discriminator, stopping diversity learning.", "Apply historical averaging, use Wasserstein GAN (WGAN) loss, or add dropouts and noise to discriminator inputs."),
    74: ("Discriminator loss goes to exactly 0.0, halting Generator learning", "The discriminator becomes too powerful too quickly, causing generator gradients to vanish.", "Reduce discriminator learning rate, use soft/noisy labels (e.g. 0.9 instead of 1.0), or train generator multiple times per discriminator update."),
    75: ("RuntimeError: Transpose Convolution outputs checkerboard artifacts in synthetic images", "Kernel size is not divisible by the stride, leading to uneven pixel overlaps.", "Ensure kernel size is a multiple of stride (e.g., kernel=4 for stride=2) or switch to bilinear upsampling followed by Conv2D."),
    76: ("GAN training diverges / loss curves oscillate wildly without reaching equilibrium", "Unstable minimax game optimization settings (e.g., learning rates too high).", "Use Adam optimizer with beta1=0.5, apply spectral normalization on discriminator layers, or use gradient penalties (WGAN-GP)."),
    77: ("RuntimeError: custom dataloader yields inconsistent batch shapes", "Images in custom dataset have different heights/widths, making batch collation fail.", "Apply a standard transforms.Resize((H, W)) in the Dataset.__getitem__ method to ensure uniform tensor shapes."),
    78: ("RuntimeError: generator outputs contain heavy noise and pixelation", "Discriminator is too weak or generator capacity is insufficient to capture fine details.", "Increase discriminator capacity, add BatchNormalization to generator blocks, or increase training epochs."),
    79: ("RuntimeError: GAN evaluation metrics (FID) yield extremely high scores", "Generated image distribution is far from the real image distribution, indicating low quality.", "Verify input preprocessing scales match (e.g. [-1, 1] scaling in both real and generated images before FID calculation)."),
    # Week 12
    80: ("RuntimeError: Attention weights contain NaN", "Dot products Q @ K.T yield extremely large values, causing softmax to overflow.", "Scale dot products by dividing by math.sqrt(d_k) before applying the softmax function."),
    81: ("RuntimeError: Mask shape mismatch in causal self-attention", "The lower triangular mask tensor shape does not align with the sequence length dimensions of the attention matrix.", "Verify batch broadcast dimensions of the mask. Shape should be [1, seq_len, seq_len] or [seq_len, seq_len]."),
    82: ("Decoder output repeats the same token sequence infinitely during inference", "The model gets stuck in a local loop due to greedy decoding decisions on saturated logits.", "Implement temperature scaling (T > 1.0) and top-k or top-p (nucleus) sampling instead of greedy argmax decoding."),
    83: ("RuntimeError: Attention matrix exceeds GPU memory limits", "Standard attention has O(N^2) memory complexity, crashing on long sequence lengths (N > 2048).", "Use block-tiling (FlashAttention), windowed local attention, or gradient checkpointing to reduce memory footprint."),
    84: ("RuntimeError: Caption generator outputs <UNK> for all words", "Tokenizer vocabulary does not include common words from the captions dataset.", "Check tokenizer vocabulary threshold parameters (e.g. min_frequency) and verify preprocessing mapping codes."),
    85: ("Attention weights focus entirely on a single token, ignoring context", "Softmax saturation due to unscaled scores, or lack of entropy regularization during training.", "Scale attention scores by 1/sqrt(d_k) or apply dropout to attention weights (e.g., nn.Dropout(0.1))."),
    86: ("RuntimeError: Cross-attention fails during decoder step", "Encoder key/value tensor shapes do not match decoder query tensor shapes along the channel dimension.", "Ensure the hidden dimension size (d_model) is identical in both the encoder and decoder architectures."),
    # Week 13
    87: ("TypeError: Argument 'text' must be string, got list", "Passing a tokenized list of strings directly to a spaCy nlp() pipeline constructor.", "Join list elements using ' '.join(tokens) or pass raw string documents directly to the nlp object."),
    88: ("AttributeError: 'Token' object has no attribute 'pos' in spaCy", "Attempting to read POS tags from spaCy tokens when the tagger component is disabled.", "Ensure that tagger is enabled. Check using nlp.pipe_names to confirm 'tagger' is in the pipeline list."),
    89: ("RuntimeError: NER model fails to extract entities from multi-line text blocks", "Tokenizer splits sentences across newlines, breaking sequential entity span boundaries.", "Clean text by replacing newlines with spaces: text.replace('\\n', ' ') before passing to NER parser."),
    90: ("AttributeError: 'Token' object has no attribute 'dep_'", "Attempting to inspect dependency parsing details when the parser component is disabled.", "Check nlp.pipe_names and ensure 'parser' component is loaded (e.g. nlp = spacy.load('en_core_web_sm'))."),
    91: ("KeyError: 'word' not in vocabulary (Word2Vec)", "Attempting to retrieve embeddings for out-of-vocabulary (OOV) words.", "Wrap lookups in a try-except block or check word in model.wv before accessing vector representation."),
    92: ("ValueError: empty vocabulary; perhaps the documents only contain stop words", "TF-IDF Vectorizer fails because all words in the input document match the stop_words filter list.", "Check document input content. Verify that documents contain meaningful content and adjust stop_words parameter settings."),
    93: ("ImportError: cannot import name 'pipeline' from 'transformers'", "Hugging Face transformers package is missing or outdated on the local system.", "Run pip install --upgrade transformers huggingface_hub to fetch the latest module builds."),
    # Week 14
    94: ("RuntimeError: Attention scores diverge to infinity", "Scaled dot product calculation omits division by sqrt(d_k), leading to extreme softmax logits.", "Ensure attention scores are divided by math.sqrt(d_k) before applying the softmax layer."),
    95: ("Pre-LN vs Post-LN training instability (Loss stays flat)", "Post-LN layers without learning rate warmup cause gradients to vanish in early epochs.", "Switch to Pre-LN architecture (apply LayerNorm to layer inputs *before* residual additions) or add a learning rate warmup scheduler."),
    96: ("RuntimeError: BERT input contains token indices out of bounds", "Input token IDs exceed the maximum vocabulary size specified in the model configuration.", "Verify tokenizer vocabulary size matches configuration setting: model.config.vocab_size."),
    97: ("Hugging Face Tokenizer outputs too many [UNK] tokens", "Tokenizer was trained on a small vocabulary or with a high min_frequency threshold.", "Retrain tokenizer with a larger vocabulary size or use a pre-trained tokenizer like 'bert-base-uncased'."),
    98: ("RuntimeError: nanoGPT training halts with NaN loss", "Gradients overflowed because learning rate was too high or activation functions exploded.", "Implement gradient clipping, reduce learning rate, or use mixed precision (torch.amp) with scaling."),
    99: ("RuntimeError: fine-tuning BERT takes extremely long on CPU", "Attempting to run backpropagation through all 110M+ parameters of BERT without GPU acceleration.", "Move model and inputs to GPU: model.to('cuda') or freeze base BERT layers to train only classifier heads."),
    100: ("HF Spaces upload fails: 'Repository not found' or authorization error", "Git credentials are not configured or Hugging Face token is missing.", "Run huggingface-cli login and input your write token before pushing your Space."),
    # Week 15
    101: ("RuntimeError: RAG returns irrelevant/hallucinated answers", "Document chunks are too large or vector similarity threshold is set too low, returning noise.", "Reduce chunk size (e.g. chunk_size=500), increase chunk overlap, or use a cross-encoder re-ranker to filter top retrieved chunks."),
    102: ("LangChain ValidationError: Missing required environment variable OPENAI_API_KEY", "OPENAI_API_KEY is not set in the environment shell variables.", "Set key using export OPENAI_API_KEY='sk-...' or load it inside python using dotenv.load_dotenv()."),
    103: ("ChromaDB ValueError: Dimension mismatch (expecting 1536, got 768)", "Vector database was created using one embedding model (e.g., OpenAI), but new queries use a different model (e.g., Cohere).", "Ensure the embedding model class passed to Chroma query matches the model class used during database instantiation."),
    104: ("Vector database queries are extremely slow", "Database is doing full linear scans instead of utilizing Approximate Nearest Neighbor (ANN) index scaling.", "Ensure HNSW index configurations are enabled and build vector databases on structured collections rather than raw lists."),
    105: ("RAG LLM reaches maximum context length limits", "Too many retrieved document chunks are injected into the prompt template.", "Limit the number of retrieved documents (e.g. k=3) or use map-reduce chain types in LangChain."),
    106: ("LangChain OutputParserException: Failed to parse output into JSON structure", "The LLM response did not follow the required schema instructions.", "Use PydanticOutputParser with few-shot examples, or switch to structured outputs API calling features (JSON Mode)."),
    107: ("ChromaDB LockError: Database is locked by another process", "Attempting to write to Chroma SQLite database from multiple concurrent python script instances.", "Ensure only one process has write access to the SQLite file, or migrate Chroma to run as a client-server container."),
    # Week 16
    108: ("Flask RuntimeError: Address already in use (Port 5000 locked)", "Another Flask API instance or system service (like macOS AirPlay Receiver) is already running on port 5000.", "Change the port parameter in app.run(port=5001) or turn off conflicting background services."),
    109: ("Docker build error: 'No such file or directory' during COPY", "File paths specified in the COPY instruction do not exist relative to the Docker build context.", "Ensure you run the docker build command from the root directory containing the target files, and verify paths in the Dockerfile."),
    110: ("Gunicorn H12 timeout error: Worker timeout (Gunicorn kills workers serving long inference requests)", "ML model inference takes longer than Gunicorn's default timeout threshold of 30 seconds.", "Increase timeout threshold using gunicorn --timeout 120 app:app, or move long-running model inferences to async background tasks."),
    111: ("Flask API returns 500 Internal Server Error when processing image uploads", "Flask fails to read binary files correctly because of incorrect payload formats.", "Access files using request.files['image'] and verify image content headers before converting them to numpy arrays."),
    112: ("Docker container exits instantly with code 0 or 1", "The Dockerfile CMD instruction exits because there is no foreground process keeping the container alive.", "Ensure CMD runs a blocking foreground server process (like gunicorn or python app.py) instead of a background daemon."),
    113: ("Docker build takes extremely long and image size is multi-gigabyte", "Docker is copying unnecessary files (like datasets, backups, virtualenvs) and caching heavy layers repeatedly.", "Create a .dockerignore file containing .git, venv, datasets, and use slim base images (e.g., python:3.9-slim)."),
    114: ("Gradio ValueError: Interface layout column width is zero", "Gradio theme configuration or blocks component arrangement syntax is incorrect.", "Inspect block element nest levels. Ensure all rows/columns are declared inside a with gr.Blocks(): context wrapper."),
    115: ("Gradio inputs.Image() yields None inside prediction function", "Image upload component format does not match input shape or type conversions fail.", "Verify that the Gradio image input type matches your function argument (e.g. type='numpy' vs type='filepath')."),
    116: ("Docker Compose error: 'service must specify image or build'", "Docker compose service block has syntax errors or path declarations are missing.", "Verify that compose service contains either build: . or image: name, and check YAML indent spacing."),
    117: ("Docker Compose container cannot connect to database container (ConnectionRefusedError)", "Attempting to connect to localhost inside a container, which resolves to the container's own loopback rather than the compose network.", "Connect using the database service name (e.g., host='db-service-name') instead of 'localhost' or '127.0.0.1'."),
    # Week 17
    118: ("Flask API returns 503 Service Unavailable under load testing", "Concurrency thresholds exceeded. Server queue is saturated with blocked inference threads.", "Scale workers using Gunicorn process managers, or configure reverse-proxy load balancers to distribute traffic."),
    119: ("Docker build error: 'pip install' fails to install torch due to network timeouts", "Heavy PyTorch download triggers pip socket timeouts during image building.", "Use pre-built PyTorch docker base images (like pytorch/pytorch) or increase pip timeout values using --default-timeout=100."),
    120: ("Docker Compose volume mounts don't synchronize local file updates", "Volume paths are declared as relative paths but build directories use absolute context setups.", "Use absolute volume mount paths or verify local permissions of folder mounts in docker-compose.yml."),
    121: ("Prometheus monitoring endpoint returns 404 error", "Prometheus scrapers are hitting incorrect route mappings on the Flask model server.", "Ensure you register prometheus metrics middleware on the root application object using prometheus_client.make_wsgi_app()."),
    122: ("ML model performance degrades silently in production (Concept Drift)", "Data inputs from users shift over time, rendering original training distributions obsolete.", "Implement logging of inputs and configure alerts to detect divergence in prediction histograms (PSI metrics)."),
    123: ("CI/CD deployment pipeline fails on git push with authentication errors", "Security tokens expired or SSH keys are missing in the runners environment variables.", "Update target deployment keys inside project secrets settings dashboard."),
    124: ("Kubernetes pod exits with OOMKilled status", "The container memory limits are configured too low for deep learning model weight loads.", "Increase resource memory limits in deployment.yaml configuration scripts.")
}

# 4. Hyperparameter Tips (Weeks 5-17)
HYPERPARAMETER_TIPS = {
    # Week 5
    31: "learning_rate=0.001 is standard because it provides stable convergence for Adam optimizer. batch_size=32 is ideal as it fits comfortably in GPU RAM while keeping gradient variance low.",
    32: "loss='mse' squares errors, making it highly sensitive to outliers. If your dataset contains heavy outliers, choose loss='mae' (L1 loss) to prevent model weights from shifting excessively.",
    33: "class_weight='balanced' automatically adjusts weights inversely proportional to class frequencies. This is crucial for imbalanced classification tasks (like fraud detection).",
    34: "Regularization strength alpha=1.0 is a default starting point. Higher alpha values restrict coefficients more heavily (increasing bias), while lower values allow complex models (increasing variance).",
    35: "GridSearchCV checks every parameter combination. Use RandomizedSearchCV first to scan a broad parameter space efficiently, then run a fine grid search around the best values.",
    36: "In KNN, k=5 is a standard default. Smaller k values (e.g. k=1) lead to high variance (noisy boundaries), while larger k values (e.g. k=50) increase bias (over-smooth boundaries).",
    37: "StandardScaler shifts data to mean=0 and variance=1. This is a critical prerequisite for distance-based estimators (like KNN or SVM) to prevent large scale features from dominating.",
    # Week 6
    38: "fit_intercept=True is default. Only set fit_intercept=False if you are sure your target variable is exactly zero when all input features are zero.",
    39: "When fitting multiple regression models, avoid using highly correlated features (collinearity) as they inflate the variance of coefficient estimates.",
    40: "Lasso alpha controls sparsity. Setting alpha=0 is equivalent to ordinary linear regression. Start with alpha=0.1 and use cross-validation (LassoCV) to find the optimal L1 penalty.",
    41: "Gradient descent learning_rate=0.01 is a safe baseline. If loss oscillates or goes to NaN, reduce learning rate to 0.001. If convergence is too slow, increase it to 0.1.",
    42: "Normalizing target variables is rarely necessary but scaling feature coordinates is critical. Always run feature scaling *after* splitting data to avoid validation leakage.",
    43: "PolynomialFeatures(degree=2) is a standard non-linear extension. Higher degrees (degree >= 3) cause exponential feature growth and severe overfitting.",
    44: "ColumnTransformer allows processing different features with different scalers (e.g. One-Hot encoding for text, StandardScaler for numbers) in a single workflow.",
    # Week 7
    45: "C=1.0 (inverse regularization strength) in LogisticRegression. Smaller C values specify stronger regularization, drawing weights closer to zero, which helps prevent overfitting.",
    46: "SVM C parameter balances margin width vs classification violations. A large C focuses on classifying all training points correctly (overfitting risk); small C allows a wider margin (generalization).",
    47: "DecisionTree max_depth=None grows trees until pure. In production, always set max_depth (e.g., between 3 and 8) to constraint complexity and avoid overfitting.",
    48: "RandomForest n_estimators=100 is standard. Increasing trees does not cause overfitting (unlike boosting), it only increases accuracy up to a point of diminishing returns.",
    49: "XGBoost learning_rate (eta)=0.3 is default. In practice, setting a lower learning rate (e.g. 0.05) combined with more estimators (n_estimators=1000) yields higher performance.",
    50: "When tuning tree models, max_depth and min_samples_split are the most impactful hyperparameters to adjust first to control leaf sizes.",
    51: "Always balance your training folds. If target distributions are imbalanced, use StratifiedKFold cross-validation to ensure each fold has matching class ratios.",
    # Week 8
    52: "Perceptron epochs=10 is a quick baseline. Since it only converges on linearly separable data, check your dataset linearity before running long epochs.",
    53: "ReLU is default for hidden layers because it doesn't saturate on positive values. Sigmoid is strictly reserved for the final output layer of binary classifiers.",
    54: "Adam optimizer default beta values are (0.9, 0.999). These control exponential decay rates of gradient moment estimates and rarely need adjustment.",
    55: "Batch size 32 or 64 is optimal for GPU training. It aligns well with GPU thread warps, maximizing memory bandwidth utilization.",
    56: "Weight decay (L2 regularization) of 1e-5 to 1e-4 is standard in PyTorch optimizers. It penalizes large weights, preventing overfitting.",
    57: "Learning rate schedulers (like ReduceLROnPlateau) decrease the learning rate when validation loss stalls, helping the model settle into global minima.",
    58: "In production serving, disable gradient tracking using torch.no_grad() to halve memory requirements and speed up inference times.",
    # Week 9
    59: "Standard convolution kernel_size=3 with padding=1 keeps spatial resolution unchanged. Stride=2 downsamples resolution by half, acting as an alternative to pooling.",
    60: "Max pooling kernel=2 with stride=2 reduces height and width of feature maps by exactly 50%, retaining the most active feature signals.",
    61: "When adding convolutional layers, double the number of filters (channels) after each downsampling step (e.g. 32 -> 64 -> 128) to extract richer semantic representations.",
    62: "In deep CNNs, apply Batch Normalization immediately after Conv2D layers and before activations to stabilize internal covariate shift.",
    63: "YOLO confidence threshold=0.25 is standard to filter out low-quality bounding boxes before running Non-Maximum Suppression (NMS).",
    64: "In U-Net, the final classification layer uses activation='sigmoid' for binary semantic segmentation (predicting tumor vs background per pixel).",
    65: "When running transfer learning, freeze the base pre-trained layers first and train only the custom classification head. Unfreeze late layers for fine-tuning only at very low learning rates (e.g., 1e-5).",
    # Week 10
    66: "In RNNs, hidden_size=128 or 256 is a standard default. Too large values lead to overfitting, while too small values fail to store sequence context.",
    67: "When training RNNs on long text documents, implement gradient clipping (max_norm=1.0) to prevent gradient explosions through backpropagation.",
    68: "LSTMs contain input, forget, output, and cell gates. Set forget_gate bias initialization to 1.0 (default in PyTorch) to prevent early forgetting.",
    69: "GRU is computationally lighter than LSTM because it combines forget and input gates into a single update gate, running ~20% faster.",
    70: "Bidirectional=True doubles the sequence context information by processing text forward and backward, but doubles the parameter size.",
    71: "Embedding dimensions are typically calculated using vocabulary_size ** 0.25, up to a maximum of 512, balancing representation vs memory.",
    72: "Teacher forcing ratio=0.5 is standard during decoder training. It feeds the true target token as the next input instead of the model's prediction.",
    # Week 11
    73: "GAN learning_rate=0.0002 for Adam is standard. Use different learning rates for Generator and Discriminator (TTUR) to stabilize minimax dynamics.",
    74: "WGAN gradient penalty coefficient lambda=10 is standard to enforce the Lipschitz constraint, preventing discriminator gradients from vanishing.",
    75: "Generator architectures use Conv2DTranspose for upsampling. Set kernel_size to a multiple of stride (e.g. 4x4 kernel with stride 2) to avoid artifacts.",
    76: "Discriminator dropout=0.3 prevents it from becoming too dominant over the generator early in training.",
    77: "Batch size 64 or 128 is optimal for GANs. Smaller batch sizes introduce noisy gradients that disrupt generator-discriminator equilibrium.",
    78: "Spectral normalization on discriminator layers restricts the weight matrices, stabilizing GAN convergence.",
    79: "FID (Fréchet Inception Distance) requires at least 10,000 generated images to compute reliable quality evaluations compared to real distributions.",
    # Week 12
    80: "Scaled dot product scales scores by 1/sqrt(d_k). For standard d_k=64, this scaling factor is 1/8 = 0.125, preventing gradient saturation.",
    81: "Causal masking replaces future token attention logits with -inf, ensuring the model cannot look ahead during training.",
    82: "Greedy decoding (argmax) leads to repetitive text. Use temperature=0.7 and top-p (nucleus)=0.9 to generate diverse, high-quality responses.",
    83: "Self-attention has O(N^2) memory complexity. In long documents, use gradient checkpointing to trade computational time for GPU memory.",
    84: "Visual attention models use feature extraction maps from late layers of pre-trained CNNs (like ResNet50) as Key/Value representations.",
    85: "Multi-head attention typically uses h=8 or h=12 heads. This splits the model dimension d_model into smaller subspaces (d_k = d_model / h).",
    86: "In cross-attention, decoder queries attend to encoder keys and values. Keep query, key, and value dimension sizes identical.",
    # Week 13
    87: "spaCy en_core_web_sm is a lightweight CPU model. Switch to en_core_web_trf (transformer-based) for higher accuracy if GPU is available.",
    88: "Disable unused components in spaCy: nlp.select_pipes(disable=['ner', 'parser']) to speed up simple tokenization pipelines.",
    89: "Named Entity Recognition relies on transition-based parsers. When training custom NER, ensure dataset labels are balanced across categories.",
    90: "Dependency parsing creates directional trees. Restrict sequence lengths to avoid computational memory bottlenecks.",
    91: "Word2Vec vector_size=100 or 300 is standard. Lower dimensions compress semantics too much; higher dimensions require massive datasets.",
    92: "TF-IDF max_features=10000 filters out rare noise words, reducing feature matrix size and improving classifier performance.",
    93: "Hugging Face pipelines default to float32. Use float16 or bfloat16 precision to halve GPU memory requirements.",
    # Week 14
    94: "Transformers dimension d_model=512 or 768 is standard. Higher dimensions (e.g. 4096 in Llama) extract deeper semantics but require massive datasets.",
    95: "LayerNorm epsilon=1e-5 prevents division by zero during normalization and should not be modified.",
    96: "BERT vocabulary size is exactly 30,522. When training on custom domains, append custom tokens to the vocabulary and resize model embeddings.",
    97: "Hugging Face tokenizers use BPE (Byte Pair Encoding) or WordPiece. Set character_coverage=0.999 for non-English languages.",
    98: "In nanoGPT, configure block_size (context length) based on task needs. Default context size is 256 or 512 for local training.",
    99: "BERT fine-tuning learning_rate should be extremely small (e.g. 2e-5 to 5e-5) to avoid destroying pre-trained weights.",
    100: "When deploying spaces, choose appropriate CPU instances. Heavy transformer models require basic GPU hardware for interactive performance.",
    # Week 15
    101: "RAG chunk_size=500 with chunk_overlap=50 is a standard default. Too large chunks introduce irrelevant text; too small chunks lose context.",
    102: "OpenAI temperature=0.0 is crucial for factual Q&A tasks to prevent model hallucinations. Use temperature=0.7 only for creative generation.",
    103: "Vector databases use cosine similarity or L2 distance. Cosine similarity is preferred for text embeddings as it normalizes document lengths.",
    104: "In ChromaDB, configure HNSW index parameters (M, efConstruction) to balance indexing speed vs search accuracy.",
    105: "LLM max_tokens controls response length. Set it to 256 or 512 for concise answers, avoiding excessive token usage costs.",
    106: "Few-shot templates improve output formatting. Provide 3-5 examples of correct input-output formats to guide LLM responses.",
    107: "In hybrid search, set vector weight=0.7 and keyword weight=0.3 to optimize search matches across technical catalogs.",
    # Week 16
    108: "Flask debug=True should never be used in production as it exposes an interactive debugger allowing arbitrary code execution.",
    109: "Docker memory limits should be configured to prevent container processes from crashing due to host system memory saturation.",
    110: "Gunicorn workers count should be set to (2 * CPU_cores) + 1 to maximize request throughput without overloading CPU.",
    111: "Flask client max_content_length defaults to 16MB. Increase it if you expect heavy payload uploads.",
    112: "Docker Compose ports mapping host_port:container_port should avoid port conflicts with host system daemons.",
    113: "Always use multi-stage Docker builds to separate dependencies compile phase from deployment image phase.",
    114: "Gradio queue() is required for high concurrency. Set default concurrency limits to protect API endpoints.",
    115: "In Gradio, configure output format of image components to avoid unnecessary format conversion overhead.",
    116: "Docker Compose restart policy restart: always ensures model services restart automatically after crashes.",
    117: "When testing APIs, configure short socket timeouts (e.g., 5 seconds) to prevent infinite connection hangs.",
    # Week 17
    118: "Model serving thread concurrency should be configured based on hardware core counts.",
    119: "Multi-stage Docker builds can reduce final image sizes by up to 90%, speeding up deployment download times.",
    120: "Docker Compose volume synchronization intervals should be optimized to reduce file system CPU overhead on macOS.",
    121: "Configure Prometheus metrics scrapers to pull data at 15-second intervals, minimizing metrics collection overhead.",
    122: "Model drift alerts should trigger when Population Stability Index (PSI) values exceed 0.25, indicating distribution shift.",
    123: "CI/CD pipeline test runner timeout limits should be capped to prevent hanging jobs from consuming build hours.",
    124: "Kubernetes pod CPU and Memory limits should be configured with a 20% buffer above average inference usage values."
}

# 5. Common Interview Questions (Weeks 5-17)
INTERVIEW_QUESTIONS = {
    # Week 5
    31: ("Flipkart", "How do you split a dataset while preserving minority class distributions? Explain StratifiedKFold."),
    32: ("Razorpay", "Why is Mean Absolute Error (MAE) robust to outliers while Mean Squared Error (MSE) is not? Explain mathematically."),
    33: ("Paytm", "In fraud detection, would you optimize for Precision or Recall? Explain the trade-off."),
    34: ("Groww", "What is the Bias-Variance tradeoff? How does model complexity affect these parameters?"),
    35: ("MakeMyTrip", "What is the difference between Grid Search and Random Search? Why does Random Search run faster?"),
    36: ("Lenskart", "Does KNN perform well on high-dimensional datasets? What is the Curse of Dimensionality?"),
    37: ("JioCinema", "Why is data scaling a prerequisite for distance-based algorithms? Explain StandardScaler vs MinMaxScaler."),
    # Week 6
    38: ("Housing.com", "Explain the closed-form analytical solution of Ordinary Least Squares (OLS) regression."),
    39: ("NoBroker", "What are the assumptions of Linear Regression? What happens if features are highly collinear?"),
    40: ("MagicBricks", "What is the difference between Ridge (L2) and Lasso (L1) regularization? Why does Lasso produce sparse weights?"),
    41: ("Ola Cabs", "Why do we subtract the gradient in Gradient Descent? What happens if the learning rate is too large?"),
    42: ("Delhivery", "Explain validation data leakage. How do you prevent it when scaling features?"),
    43: ("Swiggy Instamart", "What is Polynomial Regression? How do you control its complexity?"),
    44: ("Tata 1mg", "How do you evaluate linear regression performance? Explain the difference between R² and Adjusted R²."),
    # Week 7
    45: ("Paytm", "Why does Logistic Regression use the Sigmoid function? Why is it trained using Cross-Entropy instead of MSE?"),
    46: ("Razorpay", "How do SVM kernels work? Explain the Kernel Trick and the role of Support Vectors."),
    47: ("Flipkart", "How does a Decision Tree select feature splits? Explain Entropy, Gini Impurity, and Information Gain."),
    48: ("PhonePe", "Why doesn't a Random Forest overfit as you add more trees? Explain Bagging."),
    49: ("Groww", "What is Gradient Boosting? How does XGBoost differ from vanilla Gradient Boosting?"),
    50: ("Urban Company", "How do you handle severe class imbalance in tree-based models?"),
    51: ("MakeMyTrip", "Compare bagging vs boosting ensemble paradigms. What are their bias-variance characteristics?"),
    # Week 8
    52: ("Paytm", "What are the mathematical limitations of a single-layer perceptron? Prove why it cannot solve XOR."),
    53: ("Dream11", "Why do neural networks require non-linear activations? What is the vanishing gradient problem?"),
    54: ("InMobi", "Derive the backpropagation weight updates for a simple 3-layer neural network using the chain rule."),
    55: ("Myntra", "How does PyTorch build its dynamic computational graph? Explain Autograd."),
    56: ("Ola Maps", "What is the difference between Batch, Mini-batch, and Stochastic Gradient Descent?"),
    57: ("Razorpay", "Why is weight initialization critical in deep networks? Explain Xavier and He initialization."),
    58: ("Zomato", "What is PyTorch TorchScript and why is it used for production model deployments?"),
    # Week 9
    59: ("Ola", "Why are CNNs preferred over Fully Connected networks for image tasks? Explain weight sharing and local receptive fields."),
    60: ("Flipkart", "What is the role of Pooling in CNNs? Does it reduce spatial dimensions or channel counts?"),
    61: ("Ajio", "How do you calculate the output shape of a convolutional layer given input size, stride, padding, and kernel size?"),
    62: ("Nykaa", "Why do deep ResNets solve the vanishing gradient problem? Explain skip connections."),
    63: ("Ola Cabs", "How does YOLO object detection work? Explain the difference between one-stage and two-stage detectors."),
    64: ("Netmeds", "Explain the U-Net architecture. Why are skip connections concatenated instead of added?"),
    65: ("Myntra", "What is Transfer Learning? Under what conditions do you freeze the base model vs fine-tune it?"),
    # Week 10
    66: ("MakeMyTrip", "Why do standard RNNs struggle with long-term dependencies? Explain vanishing gradients over time."),
    67: ("Flipkart", "How does Backpropagation Through Time (BPTT) work? What is the role of gradient clipping?"),
    68: ("Swiggy", "How do the gates in an LSTM cell manage memory? Explain forget, input, and output gates."),
    69: ("BookMyShow", "Compare GRU vs LSTM architectures. Which one is computationally lighter and why?"),
    70: ("Paytm", "Explain Bidirectional sequence models. When are they useful, and when can they NOT be used?"),
    71: ("Zomato", "How do Word Embeddings work? Explain the difference between static embeddings (Word2Vec) and contextual embeddings (BERT)."),
    72: ("Tata 1mg", "What is Seq2Seq? Explain the Encoder-Decoder information bottleneck problem."),
    # Week 11
    73: ("Myntra", "Explain the minimax objective function of GANs. What is Mode Collapse?"),
    74: ("Flipkart", "How does Wasserstein GAN (WGAN) stabilize GAN training? What is the role of Gradient Penalty?"),
    75: ("Nykaa", "How does Transpose Convolution upsample image grids? Why does it cause checkerboard artifacts?"),
    76: ("Dream11", "How do you evaluate GAN output quality quantitatively? Explain FID score."),
    77: ("Meesho", "Explain the difference between conditional GANs and standard GANs."),
    78: ("InMobi", "How do adversarial training methods improve model robustness against adversarial attacks?"),
    79: ("Urban Company", "How do you deploy GAN generators to production environments for real-time synthesis?"),
    # Week 12
    80: ("Flipkart", "Derive Scaled Dot-Product Attention. Why is the scaling factor 1/sqrt(d_k) necessary?"),
    81: ("Ola Maps", "What is the difference between self-attention, cross-attention, and causal masked attention?"),
    82: ("Tata 1mg", "What is KV Caching and why is it essential for fast inference in auto-regressive decoders?"),
    83: ("Zomato", "What is FlashAttention? How does it avoid O(N^2) memory bottlenecks during attention computation?"),
    84: ("Swiggy", "How do image captioning attention models align visual features with text generation sequences?"),
    85: ("Paytm", "Compare Bahdanau attention (additive) vs Luong attention (multiplicative)."),
    86: ("MakeMyTrip", "Explain the difference between absolute positional encodings and relative positional encodings (like RoPE)."),
    # Week 13
    87: ("Inshorts", "Explain spaCy's design philosophy. How does its pipeline system differ from NLTK?"),
    88: ("Flipkart", "What is Part-of-Speech (POS) Tagging? How is it used in search query interpretation?"),
    89: ("Razorpay", "How do named entity recognition models identify span boundaries? Explain BIO tagging schemes."),
    90: ("Myntra", "What is Dependency Parsing? How does it help extract grammatical structures from search inputs?"),
    91: ("Swiggy", "How does CBOW (Continuous Bag of Words) differ from Skip-Gram in Word2Vec?"),
    92: ("Paytm", "How does TF-IDF score words? Explain mathematically why it down-weights common words."),
    93: ("Tata 1mg", "How do Hugging Face transformers handle tokenization mismatches for out-of-vocabulary words?"),
    # Week 14
    94: ("Flipkart", "Why did the Transformer architecture replace recurrent sequence models (LSTMs) for NLP tasks?"),
    95: ("Razorpay", "Explain Pre-LN vs Post-LN architectures. Why is Pre-LN more stable to train?"),
    96: ("JioCinema", "What is BERT's training objective? Explain Masked Language Modeling (MLM) and Next Sentence Prediction (NSP)."),
    97: ("Tata 1mg", "How does Byte Pair Encoding (BPE) tokenizer work? How does it build its vocabulary?"),
    98: ("Swiggy", "Explain the autoregressive training process of decoder-only models (like GPT-2)."),
    99: ("MakeMyTrip", "How do you adapt a pre-trained BERT model for text classification? Explain the role of the [CLS] token."),
    100: ("Ola", "How do you optimize Transformer models for production deployment? Explain quantization and pruning."),
    # Week 15
    101: ("Zomato", "What is Retrieval-Augmented Generation (RAG)? How does it reduce LLM hallucinations?"),
    102: ("Paytm", "What is the difference between RAG and fine-tuning an LLM? When should you use which?"),
    103: ("Flipkart", "How do Vector Databases index high-dimensional vectors? Explain HNSW indexing."),
    104: ("Groww", "What is semantic search? Compare cosine similarity vs L2 distance for vector retrieval."),
    105: ("Tata 1mg", "Explain chunking strategies in RAG. How do chunk size and overlap affect retrieval accuracy?"),
    106: ("PhonePe", "How do you evaluate a RAG pipeline? Explain the Ragas framework metrics."),
    107: ("Lenskart", "What is hybrid search in vector databases? How do you combine keyword search and semantic vector search?"),
    # Week 16
    108: ("Razorpay", "How do you secure ML model APIs in production? What is CORS and why is it important?"),
    109: ("Swiggy", "Why is Docker containerization essential for ML models? Explain reproducibility and environmental isolation."),
    110: ("Urban Company", "Explain Gunicorn's worker model. How does it handle multiple concurrent HTTP requests?"),
    111: ("Zomato", "How do you handle heavy model weights (e.g. 5GB PyTorch files) inside Docker images?"),
    112: ("Paytm", "What is the difference between Docker image layers and Docker containers? How do you optimize build times?"),
    113: ("MakeMyTrip", "Explain multi-stage Docker builds. How do they reduce production container sizes?"),
    114: ("Tata 1mg", "Why is Gradio preferred over custom web frameworks for rapid ML prototyping and expert audits?"),
    115: ("Meesho", "How do you deploy a Gradio app to Hugging Face Spaces? Explain git lfs."),
    116: ("Groww", "What is Docker Compose? How do you manage multi-container services (API + Database + Cache)?"),
    117: ("PhonePe", "How do you run automated integration testing for containerized microservices?"),
    # Week 17
    118: ("Delhivery", "How do you structure a production-grade ML pipeline? Explain data validation and model registries."),
    119: ("Paytm", "How do you deploy containerized ML models to Kubernetes? Explain pods and load balancers."),
    120: ("Myntra", "How do you manage database migrations inside containerized microservices?"),
    121: ("Razorpay", "Explain model monitoring in production. What metrics do you track to spot performance degradation?"),
    122: ("Groww", "What is Concept Drift vs Data Drift? How do you detect them statistically?"),
    123: ("Zomato", "Explain CI/CD pipelines for ML models. How do you implement blue-green deployments?"),
    124: ("Ola", "How do you design a real-time low-latency inference system for millions of requests?")
}

# 6. "What to Google" Search Terms (Weeks 5-17)
SEARCH_TERMS = {
    # Week 5
    31: "sklearn train_test_split ValueError, classification report precision recall explained",
    32: "numpy broadcasting tutorial, ordinary least squares linear regression math derivation",
    33: "precision recall curve sklearn multiclass, confusion matrix visual guide",
    34: "bias variance tradeoff mathematically, validation loss curves overfitting overfitting",
    35: "randomizedsearchcv vs gridsearchcv sklearn, param_grid syntax sklearn pipeline",
    36: "sklearn kneighborsclassifier distance metrics, naive bayes conditional independence formula",
    37: "sklearn columntransformer custom pipeline, standardscaler fit_transform leakage",
    # Week 6
    38: "linear regression derivatives cost function, simple linear regression formula derivation",
    39: "ordinary least squares closed form solution math, collinearity statsmodels VIF calculation",
    40: "lasso vs ridge regression constraint geometry, elasticnet scikit-learn alpha vs l1_ratio",
    41: "gradient descent step by step numerical example, learning rate decay schedules pytorch",
    42: "scikit-learn fit transform pipeline data leakage, test set leakage train_test_split",
    43: "polynomial regression overfitting scikit-learn, np.polyfit vs PolynomialFeatures",
    44: "r2 score vs adjusted r2 score explained, linear regression diagnostic plots residuals",
    # Week 7
    45: "binary cross entropy loss derivative derivation, logistic regression sigmoid activation math",
    46: "support vector machine lagrangian multiplier dual problem, soft margin classifier SVM math",
    47: "decision tree gini impurity vs entropy information gain, tree pruning algorithms CART",
    48: "bagging ensemble variance reduction proof, random forest out of bag error estimation",
    49: "gradient boosting residuals derivation, xgboost parameter tuning guide max_depth",
    50: "gridsearchcv best_params_ raise error_score, hyperparameter tuning tree based models",
    51: "stratified kfold cross validation sklearn, ensemble voting classifier soft vs hard voting",
    # Week 8
    52: "perceptron learning rule convergence proof, perceptron xor problem linear separation",
    53: "activation functions derivatives relu sigmoid tanh, universal approximation theorem proof",
    54: "backpropagation chain rule step by step numerical example, dL/dw calculation neural network",
    55: "pytorch autograd custom backward function, dynamic computation graph pytorch visual",
    56: "stochastic gradient descent momentum optimization, adam optimizer update equations math",
    57: "xavier initialization vs he initialization formula, vanishing gradient activation saturation",
    58: "pytorch save state dict vs full model, torchscript trace vs script compilation",
    # Week 9
    59: "convolution filter calculation padding stride math, local receptive fields weight sharing CNN",
    60: "maxpool2d vs avgpool2d dimensions calculation, translation invariance convolutional networks",
    61: "pytorch conv2d input channel mismatch ValueError, padding calculation conv shape formulas",
    62: "resnet degradation problem skip connection math, identity shortcut vs projection shortcut 1x1 conv",
    63: "yolo loss function coordinate scale factors, non maximum suppression numpy from scratch",
    64: "unet skip connections concatenation PyTorch, transpose convolution spatial upsampling math",
    65: "transfer learning fine tuning guidelines learning rates, torchvision models resnet50 pre trained",
    # Week 10
    66: "rnn backpropagation through time vanishing gradients, sequence modeling input shape mismatch",
    67: "pytorch clip_grad_norm_ max_norm, exploding gradients lstm cell states",
    68: "lstm cell equations gate math structures, pack_padded_sequence pytorch dataloader",
    69: "gru vs lstm cell math complexity differences, gated recurrent unit gate update reset",
    70: "bidirectional lstm sequence concatenation shapes, nn.LSTM batch_first shape guide",
    71: "word2vec skip gram negative sampling math, nn.Embedding vocab index out of bounds",
    72: "encoder decoder attention bottleneck seq2seq, teacher forcing ratio decay pytorch",
    # Week 11
    73: "gan minimax loss mode collapse explain, generator discriminator game theory nash equilibrium",
    74: "wgan gp gradient penalty paper math, discriminator loss goes to zero gan training",
    75: "conv2dtranspose checkerboard artifacts pixels overlap, bilinear upsampling followed by conv2d",
    76: "frechet inception distance fid calculation evaluation, gan metrics inception score",
    77: "conditional gan generator label projection, transforms.Resize custom pytorch dataset dataloader",
    78: "spectral normalization discriminator weights PyTorch, adversarial training loss optimization",
    79: "deploying generative models serving flask latency, pytorch model evaluation inference mode",
    # Week 12
    80: "attention mechanism bahdanau vs luong math, scaled dot product attention softmax saturation",
    81: "causal masked attention matrix lower triangular, self attention vs cross attention pytorch",
    82: "kv caching decoder generation inference time, greedy search vs top p sampling temperature",
    83: "flashattention tiling sram algorithms paper, o(n^2) memory complexity self attention",
    84: "image captioning attention maps visual alignments, seq2seq model with attention PyTorch",
    85: "multi head attention projection dimensions split, scaled dot product attention transpose shapes",
    86: "relative positional encoding rotary embeddings rope math, absolute positional encoding sine waves",
    # Week 13
    87: "spacy custom pipeline components tokenization, nlp.select_pipes disable components speed",
    88: "spacy pos tagging adjectives extraction nltk, part of speech syntax tags parser",
    89: "named entity recognition bio tagging scheme custom, spacy custom ner entity annotation",
    90: "dependency parsing tree visualization spacy, sentence dependency tree extraction python",
    91: "word2vec cbow vs skip gram hierarchical softmax, gensim word2vec training vocabulary",
    92: "tf-idf vectorizer max_features vocabulary scikit-learn, log term frequency inverse document frequency",
    93: "huggingface pipelines sentiment classification cpu gpu, tokenizer output padding truncation tensors",
    # Week 14
    94: "multihead self attention layer pytorch from scratch, transformer positional encoding intuition",
    95: "pre-ln vs post-ln stability learning rate warmup, layernorm vs batchnorm differences",
    96: "bert masked language modeling next sentence prediction, bert base uncased vocab index",
    97: "byte pair encoding tokenizer python from scratch, subword tokenization wordpiece vocabulary",
    98: "nanogpt training loop pytorch karpathy, autoregressive decoder transformer blocks",
    99: "bert classification head fine tuning pytorch, cls token representation classification",
    100: "quantization pytorch transformer models inference, huggingface Spaces deploy git push",
    # Week 15
    101: "langchain retrieval QA chain template RAG, llm hallucination retrieval overlap settings",
    102: "fine tuning vs rag context inject trade off, llm context window length prompt compression",
    103: "hnsw index parameters vector search speed, chromadb persistent client path settings",
    104: "vector cosine similarity vs l2 distance embeddings, semantic search python chromadb collections",
    105: "recursive character text splitter chunk size rag, chunk overlap sliding window retrieval",
    106: "ragas evaluation framework retrieval precision faithfulness, langchain evaluation qa chains",
    107: "hybrid search dense sparse vectors langchain, reciprocal rank fusion vector databases",
    # Week 16
    108: "flask api cors access control allow origin, secure api endpoint token validation",
    109: "docker build context no such file COPY, docker container environment variable python",
    110: "gunicorn worker class gevent thread limits, gunicorn timeout model inference latency",
    111: "docker multi stage builds size optimize slim, pip cache clean dockerfile layer size",
    112: "docker cmd vs entrypoint foreground process, container exits instantly exit code 0",
    113: "dockerfile best practices caching pip install, dockerignore file python patterns",
    114: "gradio custom layout blocks gr.Row gr.Column, gradio concurrent request queue limit",
    115: "gradio image input type numpy pillow filepath, gradio interface share public url link",
    116: "docker compose multi container environment yaml, docker compose volume mounts relative paths",
    117: "docker compose network service name resolve container, integration testing docker compose environment",
    # Week 17
    118: "deploying ml models best practices server architecture, flask api concurrency thread scaling",
    119: "deploy ml model to kubernetes deployment service yaml, docker file sizes multi stage build",
    120: "docker compose volume data persistence sqlite, docker compose environment variables yaml",
    121: "prometheus flask exporter metrics configuration, prometheus scrape targets setup guide",
    122: "population stability index calculations python math, data drift metrics monitoring dashboard",
    123: "mlops ci cd pipelines github actions deployment, blue green deployment strategy containers",
    124: "low latency machine learning serving docker clusters, model serving performance benchmarks container"
}

# ══════════════════════════════════════════════════════════════════════════════
# MAIN PROCESSING LOOP
# ══════════════════════════════════════════════════════════════════════════════

# Weeks mapped to days
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

# Objectives for Week 4 Day 30, Week 6 Day 44, and Week 14 Days 95-100
MISSING_OBJECTIVES = {
    30: [
        "Perform a comprehensive Exploratory Data Analysis (EDA) on a custom dataset",
        "Formulate and execute hypothesis tests to find statistically significant features",
        "Assemble a complete preprocessing pipeline with ColumnTransformers",
        "Apply Principal Component Analysis (PCA) to visualize high-dimensional data clusters"
    ],
    44: [
        "Consolidate linear and regularized regression mechanics under a unified capstone project",
        "Write custom python scripts implementing OLS equations and gradient descent weight updates",
        "Analyze residuals variance to diagnose linear model failures under non-linear data distributions",
        "Construct a production-ready model pipeline from raw features scaling to test validations"
    ],
    95: [
        "Assemble a complete multi-head attention block from query, key, and value projections",
        "Describe the architectural difference between Pre-LayerNorm and Post-LayerNorm settings",
        "Mathematically define the relative positional rotation mechanisms of RoPE",
        "Implement a KV caching routine to accelerate auto-regressive token generation during decoding"
    ],
    96: [
        "Analyze the bidirectional masked training objectives of BERT models (MLM & NSP)",
        "Explain why BERT is optimal for feature extraction but cannot generate text auto-regressively",
        "Implement sentence semantic similarity matching queries using pretrained BERT sentence encoders",
        "Verify shape changes and intermediate representations at each hidden layer of the transformer stack"
    ],
    97: [
        "Mathematically explain subword tokenization routines including BPE and WordPiece",
        "Construct a custom subword tokenizer using Hugging Face tokenizers library on custom domain corpora",
        "Manage index mappings, special tokens, padding offsets, and truncation limits in PyTorch",
        "Inspect token alignments and handle OOV representations without losing semantic values"
    ],
    98: [
        "Construct a complete causal decoder-only transformer model (nanoGPT architecture) from scratch",
        "Formulate causal sequence masks to prevent key-query interactions from looking into future tokens",
        "Write custom training loops optimizing CrossEntropy Loss with standard weight decay regularizations",
        "Perform text generation queries, manipulating temperature and top-k distributions dynamically"
    ],
    99: [
        "Fine-tune a pre-trained BERT model for custom sentiment classification tasks",
        "Write a custom dataset loader mapping raw text passages to token tensors",
        "Freeze base encoder layers to speed up gradient computations on limited hardware resources",
        "Monitor evaluation losses and evaluate model classification reports across train epochs"
    ],
    100: [
        "Configure custom inference loops for Transformer architectures in production environments",
        "Build interactive web dashboards using Gradio interfaces, exposing text generation parameters",
        "Package applications and deploy them to Hugging Face Spaces using git push pipelines",
        "Optimize inference speeds applying static quantization techniques to model parameters"
    ]
}

# Analogy & Misconception blocks for Week 14 (Days 94-100)
WEEK14_ANALOGIES = {
    94: "Imagine you are in a library searching for 'Indian spices'. The query (Q) is your search term. The database cards (K) are the index descriptions of all the books in the library. The value (V) is the actual content pages of the books. Self-attention does a dot-product search of Q against all Ks, finds the best matches, and pulls a weighted combination of their Vs.",
    95: "Imagine writing a recipe step-by-step. Sinusoidal encoding is like writing the step number at the top of the card. RoPE (Rotary Position Embeddings) is like drawing a clock hand on the card that rotates a specific angle for each step. When you compare two cards, you just check the relative angle difference between the clock hands to know how far apart the steps are, regardless of their card numbers.",
    96: "BERT is like a student filling in the blanks in a textbook paragraph where some words are blacked out (Masked Language Model). By looking at both the left and right context of the sentence simultaneously, the student can easily guess the missing words with high accuracy.",
    97: "Subword tokenization is like spelling names. If a child doesn't know the word 'Antigravity', they break it down into familiar syllables: 'Anti' + 'grav' + 'ity'. This ensures the tokenizer never hits an 'unknown' word since it can always break it down into character chunks.",
    98: "Decoder-only models (like GPT-2) are like playing word association games where you are only allowed to look at the words already spoken. You must write the next word using a causal mask that hides all future cards in the deck, forcing the model to generate one step at a time.",
    99: "Fine-tuning is like hiring a fully trained chef who knows how to cook global cuisine (Pre-trained BERT) and teaching them the specific recipes for your local restaurant (your custom classification dataset). They learn the new task in a few hours without needing to go to culinary school again.",
    100: "Hugging Face Spaces is like renting a small food stall in a busy marketplace (Hugging Face Hub). Instead of building a restaurant from scratch, you just place your menu (Gradio app) in the stall, and customers can instantly interact with it over the web."
}

WEEK14_MISCONCEPTIONS = {
    94: "Misconception: Attention solves sequence limits completely and has O(1) memory footprint. Fact: Attention has quadratic O(N^2) memory complexity. Doubling the sequence length quadruples the memory required, which is why LLM context lengths are tightly bounded.",
    95: "Misconception: LayerNorm behaves exactly like BatchNorm. Fact: BatchNorm normalizes across the batch dimension (which fails for variable-length sequences), whereas LayerNorm normalizes across the feature dimension for each individual token independently.",
    96: "Misconception: BERT is optimal for open-ended conversational text generation. Fact: BERT is an encoder model designed to output contextual representations. Generating text with BERT requires slow, mask-and-predict iteration, making decoder-only architectures (GPT) far superior for generation.",
    97: "Misconception: A subword tokenizer will split every single word into characters. Fact: Common words (like 'the', 'is') are kept as single tokens. Only rare or complex words (like 'backpropagation') are broken down into subword units, balancing vocabulary size and sequence length.",
    98: "Misconception: nanoGPT requires massive supercomputers to train. Fact: A small nanoGPT model (10-20M parameters) can be trained on a single consumer GPU (or even a CPU over a weekend) to generate Shakespeare-style text.",
    99: "Misconception: You must update all weights of BERT during fine-tuning. Fact: Freezing the base BERT weights and training only the final linear classifier classification head saves massive compute time and prevents catastrophic forgetting of pre-trained knowledge.",
    100: "Misconception: Quantization (reducing precision to int8) always breaks the model's capabilities. Fact: Post-training quantization of transformer weights to 8-bit integers typically drops accuracy by less than 1% while halving memory size and speeding up inference by 2x."
}

# Hinglish one-liners for Week 14 (Days 94-100)
WEEK14_HINGLISH = {
    94: "📢 <strong>Ek line mein:</strong> Scaled Dot-Product Attention har word ko Query, Key, aur Value matrices mein project karke unke contextual correlations calculate karta hai.",
    95: "📢 <strong>Ek line mein:</strong> RoPE (Rotary Embeddings) positional info ko features vector space mein rotate karke store karta hai, jisse model tokens ke beech ki relative doori ko behtar samajhta hai.",
    96: "📢 <strong>Ek line mein:</strong> BERT ek bidirectional model hai jo text ke dono side (left aur right) ko ek sath read karke context ki gehrai ko capture karta hai.",
    97: "📢 <strong>Ek line mein:</strong> BPE aur WordPiece tokenizers unknown words ko chhote subwords mein tod dete hain taaki model vocabulary limits ke bahar na jaaye.",
    98: "📢 <strong>Ek line mein:</strong> Decoder models (jaise GPT-2) causal mask ka use karte hain taaki predictions ke waqt aage ke words hide rahein aur model auto-regressively generate kare.",
    99: "📢 <strong>Ek line mein:</strong> BERT fine-tuning ka matlab hai pre-trained model ke upar ek chhota classifier lagakar apne custom dataset par train karna.",
    100: "📢 <strong>Ek line mein:</strong> Gradio aur HF Spaces se hum apne ML model ko ek clean interactive web interface dekar public share kar sakte hain."
}

# Fix Week 4 Day 30 missing objectives and closing div syntax error
def fix_week4():
    path = os.path.join(base_dir, "week4.html")
    if not os.path.exists(path):
        return
    print("Fixing week4.html syntax and objectives...")
    content = open(path, 'r', encoding='utf-8').read()
    
    # Check if syntax error is present: `<div id="tasks-section"`
    if '<div id="tasks-section"' in content and '<div id="tasks-section">' not in content:
        # Replace the broken tag
        content = content.replace('<div id="tasks-section"', '<div id="tasks-section">')
        
    # Inject Day 30 objectives if missing
    day30_marker = 'id="day-30"'
    if day30_marker in content:
        parts = content.split(day30_marker, 1)
        day_body = parts[1]
        
        # Check if class="objectives" is in day_body before next day or end
        day_end_idx = day_body.find("</div><!-- /day-30")
        if day_end_idx == -1:
            day_end_idx = len(day_body)
        
        day_content = day_body[:day_end_idx]
        remainder = day_body[day_end_idx:]
        
        if 'class="objectives"' not in day_content:
            # Let's build objectives HTML
            objectives_html = f"""
  <div class="objectives">
    <h3>🎯 By end of Day 30 you will be able to:</h3>
    <ul>
      <li>{"</li>\n      <li>".join(MISSING_OBJECTIVES[30])}</li>
    </ul>
  </div>
"""
            # Insert after the day-header meta-row div (which ends with </div>)
            header_end = day_content.find('</div>\n  </div>')
            if header_end == -1:
                header_end = day_content.find('</div>\n</div>')
            if header_end != -1:
                # Add offset
                offset = day_content.find('</div>', header_end) + 6
                day_content = day_content[:offset] + objectives_html + day_content[offset:]
            else:
                # Fallback to appending
                day_content = objectives_html + day_content
                
        content = parts[0] + day30_marker + day_content + remainder
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  week4.html fixed!")

# Main logic to modify week5 to week17 files
def process_week_files():
    for w in range(5, 19):
        path = os.path.join(base_dir, f"week{w}.html")
        if not os.path.exists(path):
            continue
            
        print(f"\nProcessing week{w}.html...")
        content = open(path, 'r', encoding='utf-8').read()
        
        days = WEEKS_DAYS[w]
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
            
            # ──────────────────────────────────────────────────────────────────
            # 1. INJECT OBJECTIVES IF MISSING (Weeks 6 Day 44, Week 14 Days 95-100)
            # ──────────────────────────────────────────────────────────────────
            if d in MISSING_OBJECTIVES and 'class="objectives"' not in day_body:
                objectives_html = f"""
  <div class="objectives">
    <h3>🎯 By end of Day {d} you will be able to:</h3>
    <ul>
      <li>{"</li>\n      <li>".join(MISSING_OBJECTIVES[d])}</li>
    </ul>
  </div>
"""
                # Insert right after the day-header closing tag
                meta_row_pos = day_body.find('class="meta-row"')
                if meta_row_pos != -1:
                    # Find closing div of meta-row
                    closing_div = day_body.find('</div>', meta_row_pos)
                    # And find the next closing div which finishes day-header
                    header_close = day_body.find('</div>', closing_div + 6)
                    if header_close != -1:
                        day_body = day_body[:header_close+6] + objectives_html + day_body[header_close+6:]
                    else:
                        day_body = objectives_html + day_body
                else:
                    day_body = objectives_html + day_body
                    
            # ──────────────────────────────────────────────────────────────────
            # 2. INJECT MATH INTUITION (Weeks 5-9 Algorithms)
            # ──────────────────────────────────────────────────────────────────
            if d in MATH_INTUITIONS and 'Math Intuition' not in day_body:
                math_html = f"""
  <div class="callout" style="background:rgba(108,140,255,.05);border-left:3px solid var(--blue);padding:1rem;margin:1rem 0;font-size:13.5px;">
    <strong>💡 Why does this work? (Math Intuition):</strong>
    <p style="margin-top:0.4rem;">{MATH_INTUITIONS[d]}</p>
  </div>
"""
                # Insert at the end of the theory section
                theory_pos = day_body.find('id="theory"')
                if theory_pos != -1:
                    # Find closing div of theory section or before tasks
                    tasks_pos = day_body.find('id="tasks-section"', theory_pos)
                    if tasks_pos != -1:
                        # Find the preceding div closing tag
                        prev_close = day_body.rfind('</div>', theory_pos, tasks_pos)
                        if prev_close != -1:
                            day_body = day_body[:prev_close] + math_html + day_body[prev_close:]
                        else:
                            day_body = day_body[:tasks_pos] + math_html + day_body[tasks_pos:]
                    else:
                        # Find giveaways or other section
                        tak_pos = day_body.find('class="takeaways"', theory_pos)
                        if tak_pos != -1:
                            day_body = day_body[:tak_pos] + math_html + day_body[tak_pos:]
                        else:
                            day_body += math_html
                else:
                    # Fallback to inserting before takeaways
                    tak_pos = day_body.find('class="takeaways"')
                    if tak_pos != -1:
                        day_body = day_body[:tak_pos] + math_html + day_body[tak_pos:]
                    else:
                        day_body += math_html
                        
            # ──────────────────────────────────────────────────────────────────
            # 3. INJECT FAILURE CASE (Weeks 5-17)
            # ──────────────────────────────────────────────────────────────────
            if d in FAILURE_CASES and 'What if you got this wrong?' not in day_body:
                err_msg, cause, fix = FAILURE_CASES[d]
                fail_html = f"""
  <div class="callout" style="background:rgba(229,107,140,.05);border-left:3px solid var(--pink);padding:1rem;margin:1rem 0;font-size:13.5px;">
    <strong>🚨 What if you got this wrong? (Common Error):</strong>
    <br><code style="background:rgba(0,0,0,0.15); padding:2px 6px; border-radius:4px; font-family:var(--font-mono); font-size:12px; color:var(--pink); display:inline-block; margin-top:0.4rem;">{err_msg}</code>
    <br><br><strong>Cause:</strong> {cause}
    <br><strong>Fix:</strong> {fix}
  </div>
"""
                # Insert before takeaways
                tak_pos = day_body.find('<div class="takeaways">')
                if tak_pos != -1:
                    day_body = day_body[:tak_pos] + fail_html + day_body[tak_pos:]
                else:
                    day_body += fail_html

            # ──────────────────────────────────────────────────────────────────
            # 4. INJECT LOCALIZED INDIAN COMPANY CONNECTION (Weeks 5-17)
            # ──────────────────────────────────────────────────────────────────
            if d in INDIAN_CONNECTIONS and 'Localised Connection' not in day_body:
                conn_html = f"""
  <div class="callout" style="background:rgba(180,124,252,.05);border-left:3px solid var(--purple);padding:1rem;margin:1rem 0;font-size:13.5px;">
    <strong>🇮🇳 Localised Connection (real usage):</strong> {INDIAN_CONNECTIONS[d]}
  </div>
"""
                # Insert before takeaways
                tak_pos = day_body.find('<div class="takeaways">')
                if tak_pos != -1:
                    day_body = day_body[:tak_pos] + conn_html + day_body[tak_pos:]
                else:
                    day_body += conn_html

            # ──────────────────────────────────────────────────────────────────
            # 5. INJECT "WHAT TO GOOGLE" SEARCH TERMS (Weeks 5-17)
            # ──────────────────────────────────────────────────────────────────
            if d in SEARCH_TERMS and '🔍 <strong>Search terms:</strong>' not in day_body:
                terms_html = f"""
  <div style="font-family:var(--font-mono);font-size:11px;color:var(--muted);margin-top:0.5rem;margin-bottom:1rem;">
    🔍 <strong>Search terms:</strong> <code>{SEARCH_TERMS[d]}</code>
  </div>
"""
                # Insert right before resources section
                res_pos = day_body.find('id="resources-section"')
                if res_pos != -1:
                    # Find preceding tag
                    prev_tag_pos = day_body.rfind('</div>', 0, res_pos)
                    if prev_tag_pos != -1:
                        day_body = day_body[:prev_tag_pos+6] + terms_html + day_body[prev_tag_pos+6:]
                    else:
                        day_body = day_body[:res_pos] + terms_html + day_body[res_pos:]
                else:
                    # Append before takeaways
                    tak_pos = day_body.find('<div class="takeaways">')
                    if tak_pos != -1:
                        day_body = day_body[:tak_pos] + terms_html + day_body[tak_pos:]
                    else:
                        day_body += terms_html

            # ──────────────────────────────────────────────────────────────────
            # 6. INJECT HYPERPARAMETER TIP (Weeks 5-17)
            # ──────────────────────────────────────────────────────────────────
            if d in HYPERPARAMETER_TIPS and 'Hyperparameter Tip' not in day_body:
                hp_html = f"""
  <div class="callout" style="background:rgba(247,169,75,.05);border-left:3px solid var(--orange);padding:1rem;margin:1rem 0;font-size:13.5px;">
    <strong>⚙️ Hyperparameter Tip:</strong> {HYPERPARAMETER_TIPS[d]}
  </div>
"""
                # Insert under the theory section or before tasks
                theory_pos = day_body.find('id="theory"')
                if theory_pos != -1:
                    tasks_pos = day_body.find('id="tasks-section"', theory_pos)
                    if tasks_pos != -1:
                        # Preceding div closing
                        prev_close = day_body.rfind('</div>', theory_pos, tasks_pos)
                        if prev_close != -1:
                            day_body = day_body[:prev_close] + hp_html + day_body[prev_close:]
                        else:
                            day_body = day_body[:tasks_pos] + hp_html + day_body[tasks_pos:]
                    else:
                        tak_pos = day_body.find('class="takeaways"', theory_pos)
                        if tak_pos != -1:
                            day_body = day_body[:tak_pos] + hp_html + day_body[tak_pos:]
                        else:
                            day_body += hp_html
                else:
                    # Append before takeaways
                    tak_pos = day_body.find('<div class="takeaways">')
                    if tak_pos != -1:
                        day_body = day_body[:tak_pos] + hp_html + day_body[tak_pos:]
                    else:
                        day_body += hp_html

            # ──────────────────────────────────────────────────────────────────
            # 7. INJECT COMMON INTERVIEW QUESTION (Weeks 5-17)
            # ──────────────────────────────────────────────────────────────────
            if d in INTERVIEW_QUESTIONS and 'Asked in interviews at' not in day_body:
                company, question = INTERVIEW_QUESTIONS[d]
                interview_html = f"""
  <div class="callout" style="background:rgba(79,209,165,.05);border-left:3px solid var(--green);padding:0.8rem 1.1rem;margin:1rem 0;font-size:13.5px;">
    <strong>🎤 Asked in interviews at: {company}</strong>
    <p style="margin-top:0.4rem;">{question}</p>
  </div>
"""
                # Insert before takeaways
                tak_pos = day_body.find('<div class="takeaways">')
                if tak_pos != -1:
                    day_body = day_body[:tak_pos] + interview_html + day_body[tak_pos:]
                else:
                    day_body += interview_html

            # ──────────────────────────────────────────────────────────────────
            # 8. WEEK 14 EXTRA FEATURES: ANALOGIES, MISCONCEPTIONS, HINGLISH (Days 94-100)
            # ──────────────────────────────────────────────────────────────────
            if w == 14:
                # Inject Analogy if missing
                if d in WEEK14_ANALOGIES and 'Analogy:' not in day_body:
                    analogy_html = f"""
  <div class="analogy">{WEEK14_ANALOGIES[d]}</div>
"""
                    theory_pos = day_body.find('id="theory"')
                    if theory_pos != -1:
                        day_body = day_body[:theory_pos+12] + analogy_html + day_body[theory_pos+12:]
                    else:
                        day_body = analogy_html + day_body
                        
                # Inject Misconception if missing
                if d in WEEK14_MISCONCEPTIONS and 'Common Misconception' not in day_body:
                    miscon = WEEK14_MISCONCEPTIONS[d]
                    miscon_html = f"""
  <div class="misconception">
    <strong>⚠️ Common Misconception:</strong> {miscon.split('Fact:')[0].replace('Misconception:', '').strip()}
    <br><br>
    <strong>Fact:</strong> {miscon.split('Fact:')[1].strip() if 'Fact:' in miscon else miscon}
  </div>
"""
                    tak_pos = day_body.find('<div class="takeaways">')
                    if tak_pos != -1:
                        day_body = day_body[:tak_pos] + miscon_html + day_body[tak_pos:]
                    else:
                        day_body += miscon_html

                # Inject Hinglish Summary if missing
                if d in WEEK14_HINGLISH and 'Hinglish' not in day_body and 'Ek line mein' not in day_body:
                    hinglish_html = f"""
  <div class="hinglish">
    {WEEK14_HINGLISH[d]}
  </div>
"""
                    tak_list_idx = day_body.find('<ol>', day_body.find('<div class="takeaways">'))
                    if tak_list_idx != -1:
                        day_body = day_body[:tak_list_idx] + hinglish_html + day_body[tak_list_idx:]
                    else:
                        # Append after takeaways title
                        tak_title_idx = day_body.find('<h3>', day_body.find('<div class="takeaways">'))
                        if tak_title_idx != -1:
                            close_h3 = day_body.find('</h3>', tak_title_idx)
                            if close_h3 != -1:
                                day_body = day_body[:close_h3+5] + hinglish_html + day_body[close_h3+5:]

            # ──────────────────────────────────────────────────────────────────
            # 9. STANDARDISE TASK TIMES & LEGEND
            # ──────────────────────────────────────────────────────────────────
            # Inject global scale legend if not present
            tasks_hdr_idx = day_body.find('id="tasks-section"')
            if tasks_hdr_idx != -1 and 'Global Task Difficulty Scale' not in day_body:
                legend_html = """
  <div class="callout" style="background:rgba(255,255,255,.02);border:1px solid var(--border);padding:0.8rem;margin:1rem 0;font-size:12px;border-radius:8px;">
    <strong>💡 Global Task Difficulty Scale:</strong>
    <span style="margin-left:10px;color:var(--green)">🟢 EASY (15-30 min)</span> | 
    <span style="margin-left:10px;color:var(--orange)">🟡 MEDIUM (45-75 min)</span> | 
    <span style="margin-left:10px;color:var(--pink)">🔴 HARD (90-180 min)</span>
  </div>
"""
                # Insert legend right after the tasks header closing tag
                hdr_close_div = day_body.find('</div>', tasks_hdr_idx)
                if hdr_close_div != -1:
                    day_body = day_body[:hdr_close_div+6] + legend_html + day_body[hdr_close_div+6:]
            
            # Standardize individual task times based on badges
            def repl_task_time(m):
                badge_content = m.group(1)
                time_span = m.group(2)
                
                # Check badge class
                new_time = "⏱ 30 min" # Default
                if 'tb-easy' in badge_content or 'EASY' in badge_content or '🟢' in badge_content:
                    new_time = "⏱ 25 min"
                elif 'tb-med' in badge_content or 'MEDIUM' in badge_content or '🟡' in badge_content:
                    new_time = "⏱ 45 min"
                elif 'tb-hard' in badge_content or 'HARD' in badge_content or '🔴' in badge_content:
                    new_time = "⏱ 90 min"
                elif 'tb-proj' in badge_content or 'tb-challenge' in badge_content or 'PROJ' in badge_content or 'CHALLENGE' in badge_content or 'PORTFOLIO' in badge_content or '🔵' in badge_content:
                    new_time = "⏱ 3 hours"
                
                # Re-assemble the task header content
                return f'{badge_content}\n        <span class="task-time">{new_time}</span>'
            
            # Match: <span class="task-badge ...">...</span> followed by any text and <span class="task-time">...</span>
            # E.g.
            # <span class="task-badge tb-easy">🟢 EASY</span>
            # <span class="task-title">NumPy train_test_split from scratch</span>
            # <span class="task-time">⏱ 30 min</span>
            day_body = re.sub(
                r'(<span class="task-badge\s+[^"]+">.*?</span>\s*<span class="task-title">.*?</span>)\s*(<span class="task-time">.*?</span>)',
                repl_task_time,
                day_body,
                flags=re.DOTALL
            )
            
            # ──────────────────────────────────────────────────────────────────
            # 10. TIERED RESOURCE LABELS
            # ──────────────────────────────────────────────────────────────────
            # Let's find every resource card in resources-grid
            def repl_res_card(m):
                card_html = m.group(0)
                # Skip if it already has res-difficulty
                if 'res-difficulty' in card_html:
                    return card_html
                
                # Determine difficulty level based on card details
                res_type_m = re.search(r'class="res-type"[^>]*>(.*?)</div>', card_html)
                res_title_m = re.search(r'class="res-title"[^>]*>(.*?)</span>', card_html)
                if not res_title_m:
                    res_title_m = re.search(r'<h4>(.*?)</h4>', card_html)
                res_desc_m = re.search(r'class="res-desc"[^>]*>(.*?)</div>', card_html)
                
                res_type = res_type_m.group(1).lower() if res_type_m else ""
                res_title = res_title_m.group(1).lower() if res_title_m else ""
                res_desc = res_desc_m.group(1).lower() if res_desc_m else ""
                
                # Heuristics
                level = "Intermediate"
                color = "var(--orange)"
                
                # Deep Dive triggers
                if ('paper' in res_type or 'research' in res_type or 'arxiv' in card_html or 
                    'math' in res_title or 'derivation' in res_title or 'under the hood' in res_title or 
                    'advanced' in res_title or 'rigorous' in res_desc or 'from scratch' in res_title):
                    level = "Deep Dive"
                    color = "var(--blue)"
                # Beginner triggers
                elif ('introduction' in res_title or 'intro' in res_title or 'beginner' in res_title or 
                      'basic' in res_title or 'crash course' in res_title or 'visual' in res_title or 
                      'youtube' in res_type or 'gentle' in res_desc):
                    level = "Beginner"
                    color = "var(--green)"
                
                badge_html = f'<span class="res-difficulty" style="font-family:var(--font-mono); font-size:8.5px; border:1px solid {color}; color:{color}; padding:1px 6px; border-radius:10px; font-weight:bold; flex-shrink:0;">{level}</span>'
                
                # Let's insert the badge in the res-type header.
                # Wrap res-type inside a flex row:
                if res_type_m:
                    full_res_type_tag = res_type_m.group(0)
                    new_type_row = f"""<div style="display:flex; justify-content:space-between; align-items:center; width:100%; margin-bottom:5px;">
            <div class="res-type" style="{res_type_m.group(0).split('style="')[1] if 'style="' in res_type_m.group(0) else ''}">{res_type_m.group(1)}</div>
            {badge_html}
          </div>"""
                    card_html = card_html.replace(full_res_type_tag, new_type_row)
                else:
                    # Fallback: Prepend badge inside res-body
                    res_body_idx = card_html.find('class="res-body"')
                    if res_body_idx != -1:
                        insert_pos = card_html.find('>', res_body_idx) + 1
                        card_html = card_html[:insert_pos] + f"\n{badge_html}\n" + card_html[insert_pos:]
                        
                return card_html
                
            day_body = re.sub(
                r'<a class="res-card[^>]*>.*?</a>',
                repl_res_card,
                day_body,
                flags=re.DOTALL
            )
            
            content = parts[0] + day_marker + day_body + remainder
            
        # Write back to file
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Finished modifying week{w}.html!")

if __name__ == '__main__':
    fix_week4()
    process_week_files()
    print("\nContent deepening pipeline completed successfully!")
