import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
roadmap_path = os.path.join(base_dir, "roadmap.html")

content = open(roadmap_path, 'r', encoding='utf-8').read()

# 1. Replace TOC Grid in master Hub
old_toc = """    <div class="toc-grid">
      <div class="toc-card" style="border-top-color:var(--m1)" onclick="showSection('m1w1')">
        <div class="tc-month">MONTH 1 · DAYS 1–30</div>
        <div class="tc-title" style="color:var(--m1)">Foundations</div>
        <div class="tc-days">Python · SQL · Preprocessing · Math for AI · Visualization · Git</div>
      </div>
      <div class="toc-card" style="border-top-color:var(--m2)" onclick="showSection('m2w5')">
        <div class="tc-month">MONTH 2 · DAYS 31–60</div>
        <div class="tc-title" style="color:var(--m2)">Machine Learning</div>
        <div class="tc-days">Supervised · Unsupervised · Regression · SVM · Decision Trees · Neural Networks · CNNs · RNNs · GANs · Transformers · NLP</div>
      </div>
      <div class="toc-card" style="border-top-color:var(--m3)" onclick="showSection('m3w9')">
        <div class="tc-month">MONTH 3 · DAYS 61–90</div>
        <div class="tc-title" style="color:var(--m3)">Deep Learning</div>
        <div class="tc-days">Perceptron · FNN · CNN · RNN · LSTM · TensorFlow · GANs</div>
      </div>
      <div class="toc-card" style="border-top-color:var(--m4)" onclick="showSection('m4w13')">
        <div class="tc-month">MONTH 4 · DAYS 91–120</div>
        <div class="tc-title" style="color:var(--m4)">Modern AI Stack</div>
        <div class="tc-days">NLP · Transformers · LLMs · GenAI · OpenAI APIs · RAG · AI Agents</div>
      </div>
      <div class="toc-card" style="border-top-color:var(--mfin)" onclick="showSection('fin1')">
        <div class="tc-month">FINAL 15 DAYS · 121–135</div>
        <div class="tc-title" style="color:var(--mfin)">Deployment & Capstone</div>
        <div class="tc-days">Flask · Docker · Kubernetes · Hugging Face · Portfolio · Interview Prep</div>
      </div>
    </div>"""

new_toc = """    <div class="toc-grid">
      <div class="toc-card" style="border-top-color:var(--m1)" onclick="showSection('m1w1')">
        <div class="tc-month">MONTH 1 · DAYS 1–30</div>
        <div class="tc-title" style="color:var(--m1)">Foundations</div>
        <div class="tc-days">Python · SQL · Preprocessing · Math for AI · Visualization · Git</div>
      </div>
      <div class="toc-card" style="border-top-color:var(--m2)" onclick="showSection('m2w5')">
        <div class="tc-month">MONTH 2 · DAYS 31–58</div>
        <div class="tc-title" style="color:var(--m2)">Machine Learning</div>
        <div class="tc-days">Supervised · Regression · SVMs · Decision Trees · XGBoost · Neural Networks · Backprop</div>
      </div>
      <div class="toc-card" style="border-top-color:var(--m3)" onclick="showSection('m3w9')">
        <div class="tc-month">MONTH 3 · DAYS 59–86</div>
        <div class="tc-title" style="color:var(--m3)">Deep Learning</div>
        <div class="tc-days">CNNs · Computer Vision · RNNs · LSTMs · GAN Zoo · PyTorch · Attention & Image Captioning</div>
      </div>
      <div class="toc-card" style="border-top-color:var(--m4)" onclick="showSection('m4w13')">
        <div class="tc-month">MONTH 4 · DAYS 87–117</div>
        <div class="tc-title" style="color:var(--m4)">Modern AI Stack</div>
        <div class="tc-days">NLP · Transformers · BERT · LLM Engineering · RAG · Observability & Evaluation · FastAPI</div>
      </div>
      <div class="toc-card" style="border-top-color:var(--mfin)" onclick="showSection('fin1')">
        <div class="tc-month">FINAL · DAYS 118–135</div>
        <div class="tc-title" style="color:var(--mfin)">Deployment & Capstone</div>
        <div class="tc-days">Flask · Docker · Kubernetes · Cloud Deploy · MLOps · Capstone Project · Portfolio Polish · Interview Sprint</div>
      </div>
    </div>"""

content = content.replace(old_toc, new_toc)

# 2. Week 12: Tag to MONTH 3 · DAYS 80–86 and update days-grid
content = content.replace(
    '<div class="section-tag">MONTH 3 · DAYS 80–90</div>',
    '<div class="section-tag">MONTH 3 · DAYS 80–86</div>'
)
content = content.replace(
    '<h2 style="color:var(--m3)">Week 12 — Attention Mechanism & Major Image Captioning Capstone</h2>',
    '<h2 style="color:var(--m3)">Week 12 — Attention Mechanism & Image Captioning</h2>'
)

# Week 12 days-grid old block in roadmap.html
old_w12_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 80</div>
            <div class="day-title">The Attention Mechanism</div>
            <ul class="day-list">
              <li>Why sequence-to-sequence bottlenecks without context focus</li>
              <li>Additive (Bahdanau) vs Dot-Product (Luong) Attention math</li>
              <li>Calculating attention weights and context vectors</li>
              <li>BLEU score metric for machine translation & captioning</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 81</div>
            <div class="day-title">Multi-Modal Architectures: CNN + RNN</div>
            <ul class="day-list">
              <li>Stitching modalities: Vision (CNN) encoder + Sequence (RNN) decoder</li>
              <li>Extracting feature grids from deep pre-trained CNN layers</li>
              <li>Passing context state to LSTM hidden state</li>
              <li>Teacher forcing strategy during sequence training</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 82–90</div>
            <div class="day-title">Month 3 Capstone: Image Caption Generator</div>
            <ul class="day-list">
              <li>Flickr8k dataset: downloading, loading, tokenizing captions</li>
              <li>Building an Attention-augmented encoder-decoder in Keras/PyTorch</li>
              <li>Training pipeline with BLEU validation evaluation metrics</li>
              <li>Deploying Gradio Web App for real-time image upload captioning</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>"""

new_w12_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 80</div>
            <div class="day-title">The Attention Mechanism</div>
            <ul class="day-list">
              <li>Why Seq2Seq bottlenecks without context focus</li>
              <li>Additive (Bahdanau) vs Dot-Product (Luong) Attention math</li>
              <li>Calculating attention weights and context vectors</li>
              <li>BLEU score metric for machine translation & captioning</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 81</div>
            <div class="day-title">Multi-Modal Architectures: CNN + RNN</div>
            <ul class="day-list">
              <li>Stitching modalities: Vision (CNN) encoder + Sequence (RNN) decoder</li>
              <li>Extracting feature grids from deep pre-trained CNN layers</li>
              <li>Passing context state to LSTM hidden state</li>
              <li>Teacher forcing strategy during sequence training</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 82</div>
            <div class="day-title">Capstone Part 1: Dataset & Feature Extraction</div>
            <ul class="day-list">
              <li>Flickr8k dataset download and cleaning</li>
              <li>Pre-processing caption descriptions and vocabulary building</li>
              <li>Feature extraction with MobileNetV2 / ResNet</li>
              <li>Saving feature maps to disk for training speedup</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 83</div>
            <div class="day-title">Capstone Part 2: Attention-Augmented Decoder</div>
            <ul class="day-list">
              <li>Defining the custom attention layer subclass in PyTorch/Keras</li>
              <li>Building the LSTM decoder sequence generator</li>
              <li>Connecting CNN features and tokenized text embeddings</li>
              <li>Compiling the multi-input deep model</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 84</div>
            <div class="day-title">Capstone Part 3: Training & Evaluation Loop</div>
            <ul class="day-list">
              <li>Writing custom training loop or fitting with checkpoints</li>
              <li>Monitoring loss reduction and validation performance</li>
              <li>Calculating BLEU-1, BLEU-2, BLEU-3, BLEU-4 metrics</li>
              <li>Preventing overfitting with early stopping and dropout</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 85</div>
            <div class="day-title">Capstone Part 4: Greedy vs. Beam Search</div>
            <ul class="day-list">
              <li>Implementing greedy search decoding for captions</li>
              <li>Writing Beam Search decoder with temperature parameter</li>
              <li>Comparing translation quality and diversity of beams</li>
              <li>Testing model on arbitrary out-of-distribution images</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m3)">
            <div class="day-label">DAY 86</div>
            <div class="day-title">Capstone Part 5: Web App Deployment</div>
            <ul class="day-list">
              <li>Creating a clean Gradio interface for image upload</li>
              <li>Loading serialized weights and running inference pipelines</li>
              <li>Pushing to Hugging Face Spaces / GitHub</li>
              <li>Writing final project report and documenting failures</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
        </div>"""

content = content.replace(old_w12_grid, new_w12_grid)

# 3. Week 13: Update days-grid
old_w13_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 91</div>
            <div class="day-title">NLP Preprocessing Pipeline</div>
            <ul class="day-list">
              <li>Tokenisation (word, sentence, subword)</li>
              <li>Stopword removal, lowercasing, punctuation</li>
              <li>Stemming (Porter) vs Lemmatisation (spaCy)</li>
              <li>Regular expressions for text cleaning</li>
              <li>Practice: Clean and preprocess 10,000 tweets</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 92</div>
            <div class="day-title">Text Representation — BoW, TF-IDF</div>
            <ul class="day-list">
              <li>Bag of Words: simple but effective</li>
              <li>TF-IDF: term frequency × inverse document frequency</li>
              <li>N-grams: bigrams, trigrams</li>
              <li>Limitations of sparse representations</li>
              <li>Build news classifier with TF-IDF + Logistic Regression</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 93</div>
            <div class="day-title">Word Embeddings — Word2Vec, GloVe</div>
            <ul class="day-list">
              <li>Dense vector representations of words</li>
              <li>Word2Vec: CBOW vs Skip-gram</li>
              <li>GloVe: global co-occurrence statistics</li>
              <li>Analogies: king - man + woman = queen</li>
              <li>Load pre-trained GloVe, explore similarity</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 94</div>
            <div class="day-title">Named Entity Recognition + POS Tagging</div>
            <ul class="day-list">
              <li>Part-of-Speech tagging with spaCy</li>
              <li>Named Entity Recognition: PERSON, ORG, GPE</li>
              <li>Dependency parsing</li>
              <li>Practice: Extract all companies and locations from news articles</li>
            </ul>
            <div class="day-hours">⏱ 4 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 95</div>
            <div class="day-title">Text Classification + Sequence Labeling</div>
            <ul class="day-list">
              <li>Document classification pipeline</li>
              <li>Sequence labeling with LSTM</li>
              <li>CRF layer for NER</li>
              <li>Evaluation: F1 score for NLP</li>
              <li>Practice: Build multi-class news classifier</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 96–97</div>
            <div class="day-title">Project: Fake News Detector + Text Summariser</div>
            <ul class="day-list">
              <li>Fake news dataset from Kaggle</li>
              <li>TF-IDF + SVM + BERT comparison</li>
              <li>Extractive summarisation with NLTK</li>
              <li>Deploy as web app</li>
              <li>GitHub: complete README with methodology</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>"""

new_w13_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 87</div>
            <div class="day-title">NLP Preprocessing Pipeline</div>
            <ul class="day-list">
              <li>Tokenisation (word, sentence, subword)</li>
              <li>Stopword removal, lowercasing, punctuation</li>
              <li>Stemming (Porter) vs Lemmatisation (spaCy)</li>
              <li>Regular expressions for text cleaning</li>
              <li>Practice: Clean and preprocess 10,000 tweets</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 88</div>
            <div class="day-title">Text Representation: BoW & TF-IDF</div>
            <ul class="day-list">
              <li>Bag of Words: simple but effective</li>
              <li>TF-IDF: term frequency × inverse document frequency</li>
              <li>N-grams: bigrams, trigrams</li>
              <li>Limitations of sparse representations</li>
              <li>Build news classifier with TF-IDF + Logistic Regression</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 89</div>
            <div class="day-title">Word Embeddings: Word2Vec & GloVe</div>
            <ul class="day-list">
              <li>Dense vector representations of words</li>
              <li>Word2Vec: CBOW vs Skip-gram</li>
              <li>GloVe: global co-occurrence statistics</li>
              <li>Analogies: king - man + woman = queen</li>
              <li>Load pre-trained GloVe, explore similarity</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 90</div>
            <div class="day-title">Named Entity Recognition & POS Tagging</div>
            <ul class="day-list">
              <li>Part-of-Speech tagging with spaCy</li>
              <li>Named Entity Recognition: PERSON, ORG, GPE</li>
              <li>Dependency parsing</li>
              <li>Practice: Extract companies/locations from news</li>
            </ul>
            <div class="day-hours">⏱ 4 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 91</div>
            <div class="day-title">Text Classification & Sequence Labeling</div>
            <ul class="day-list">
              <li>Document classification pipeline</li>
              <li>Sequence labeling with LSTM</li>
              <li>CRF layer for NER</li>
              <li>Evaluation: F1 score for NLP</li>
              <li>Practice: Build multi-class news classifier</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 92</div>
            <div class="day-title">Capstone Part 1: Fake News & TextRank</div>
            <ul class="day-list">
              <li>Fake news dataset from Kaggle</li>
              <li>TF-IDF + SVM + BERT comparison</li>
              <li>Extractive summarisation with NLTK</li>
              <li>Deploy as web app</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 93</div>
            <div class="day-title">Capstone Part 2: Gradio & Benchmarking</div>
            <ul class="day-list">
              <li>Creating a combined dashboard UI with Gradio</li>
              <li>Comparing model performance and execution speeds</li>
              <li>Adding comprehensive README to GitHub</li>
              <li>Documenting final deliverables and project results</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
        </div>"""

content = content.replace(old_w13_grid, new_w13_grid)

# 4. Week 14: Update days-grid
old_w14_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 98</div>
            <div class="day-title">Attention Mechanism — From RNN to Self-Attention</div>
            <ul class="day-list">
              <li>Encoder-Decoder with attention (Seq2Seq)</li>
              <li>Self-attention: Q, K, V matrices</li>
              <li>Scaled dot-product attention formula</li>
              <li>Multi-head attention</li>
              <li>Watch: Andrej Karpathy GPT from scratch (best resource ever)</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 99</div>
            <div class="day-title">Transformer Architecture Complete</div>
            <ul class="day-list">
              <li>Positional encoding (sine/cosine)</li>
              <li>Encoder: self-attn + feed-forward + layer norm</li>
              <li>Decoder: masked self-attn + cross-attention</li>
              <li>Why transformers replaced RNNs entirely</li>
              <li>Read "Attention Is All You Need" paper abstract</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 100</div>
            <div class="day-title">BERT — Bidirectional Transformers</div>
            <ul class="day-list">
              <li>BERT: pre-training with MLM + NSP</li>
              <li>Fine-tuning BERT for classification</li>
              <li>Hugging Face transformers library</li>
              <li>Practice: Sentiment analysis with bert-base-uncased</li>
              <li>Understand CLS token, attention masks, tokeniser</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 101</div>
            <div class="day-title">Hugging Face Ecosystem Mastery</div>
            <ul class="day-list">
              <li>Model Hub: search, load, inference</li>
              <li>Pipelines: text-classification, zero-shot, summarisation</li>
              <li>Tokenisers: AutoTokenizer, padding, truncation</li>
              <li>Datasets library for loading data</li>
              <li>Deploy model on Hugging Face Spaces (Gradio)</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 102</div>
            <div class="day-title">Fine-Tuning Transformers (Trainer API)</div>
            <ul class="day-list">
              <li>Hugging Face Trainer API</li>
              <li>TrainingArguments: epochs, batch size, lr</li>
              <li>Compute_metrics function</li>
              <li>Save and push model to HF Hub</li>
              <li>Practice: Fine-tune DistilBERT on custom dataset</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 103–104</div>
            <div class="day-title">Project: Multi-task NLP App</div>
            <ul class="day-list">
              <li>Build an app with: classification + NER + summarisation</li>
              <li>Use 3 different HuggingFace models</li>
              <li>Gradio interface with tabs for each task</li>
              <li>Deploy on Hugging Face Spaces (free!)</li>
              <li>Add to GitHub portfolio</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>"""

new_w14_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 94</div>
            <div class="day-title">Mathematics of Scaled Dot-Product Attention</div>
            <ul class="day-list">
              <li>Self-attention: Query, Key, Value matrices</li>
              <li>Scaled dot-product attention formula</li>
              <li>Multi-head attention mechanisms</li>
              <li>Implementing self-attention in PyTorch from scratch</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 95</div>
            <div class="day-title">Transformer Architecture & RoPE</div>
            <ul class="day-list">
              <li>Positional encoding: sine/cosine vs rotary positional embeddings (RoPE)</li>
              <li>Encoder: self-attn + feed-forward + layer normalization</li>
              <li>Decoder: masked self-attn + cross-attention</li>
              <li>Why Transformers replaced RNNs entirely</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 96</div>
            <div class="day-title">BERT — Bidirectional Encoder</div>
            <ul class="day-list">
              <li>Pre-training: Masked Language Model (MLM) + Next Sentence Prediction (NSP)</li>
              <li>Fine-tuning BERT for classification</li>
              <li>Hugging Face transformers library</li>
              <li>Sentiment analysis with bert-base-uncased</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 97</div>
            <div class="day-title">Hugging Face Ecosystem & Tokenizers</div>
            <ul class="day-list">
              <li>Model Hub: search, load, inference</li>
              <li>Pipelines: classification, zero-shot, summarisation</li>
              <li>Tokenisers: AutoTokenizer, padding, truncation</li>
              <li>Datasets library for loading data</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 98</div>
            <div class="day-title">Parameter-Efficient Fine-Tuning & LoRA</div>
            <ul class="day-list">
              <li>PEFT vs full fine-tuning</li>
              <li>Low-Rank Adaptation (LoRA) math and concepts</li>
              <li>Fine-tuning models using PEFT library</li>
              <li>Applying LoRA to BERT/distilBERT</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 99</div>
            <div class="day-title">Capstone Part 1: Advanced IR & RAG</div>
            <ul class="day-list">
              <li>Document parsing and semantic chunking</li>
              <li>Building dense indexing for retrieval</li>
              <li>Evaluating retrieval using MRR / MAP metrics</li>
              <li>Setting up HuggingFace inference endpoint</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 100</div>
            <div class="day-title">Capstone Part 2: Deployment & Model Serving</div>
            <ul class="day-list">
              <li>Building FastAPI wrappers for inference</li>
              <li>Serving models efficiently in Docker containers</li>
              <li>Deploying app to Hugging Face Spaces (Gradio)</li>
              <li>Adding complete project documentation to GitHub</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
        </div>"""

content = content.replace(old_w14_grid, new_w14_grid)

# 5. Week 15: Update days-grid
old_w15_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 105</div>
            <div class="day-title">Understanding LLMs — How GPT Works</div>
            <ul class="day-list">
              <li>Autoregressive generation, causal self-attention</li>
              <li>Pre-training (unsupervised) vs Instruction tuning (SFT, RLHF)</li>
              <li>Decoding strategies: greedy, beam search, temperature, top-k/top-p</li>
              <li>Compute requirements: parameters, active parameters (MoE)</li>
              <li>Playground: Interact with open-source LLMs</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 106</div>
            <div class="day-title">Prompt Engineering — Master the Art</div>
            <ul class="day-list">
              <li>Zero-shot, Few-shot, Chain-of-Thought prompting</li>
              <li>System prompts, user prompts, assistant prompts</li>
              <li>Structured output generation (JSON mode, function calling)</li>
              <li>Prompt injection, jailbreaks, and safety alignment</li>
              <li>Practice: Write robust prompts for entity extraction</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 107</div>
            <div class="day-title">OpenAI API — Full Practical Guide</div>
            <ul class="day-list">
              <li>API Key setup, client instantiation</li>
              <li>Chat completions endpoint, streaming responses</li>
              <li>JSON mode, function calling, tool use</li>
              <li>Rate limits, retries, costs tracking</li>
              <li>Practice: Build a CLI chatbot with memory</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 108</div>
            <div class="day-title">Running Local LLMs with Ollama (Free!)</div>
            <ul class="day-list">
              <li>Ollama setup, downloading llama3.2, mistral, phi3, gemma2 models</li>
              <li>Running models in terminal vs local web UI</li>
              <li>Python wrapper for local inference</li>
              <li>Understanding quantization: Q4_K_M vs Q8_0</li>
              <li>Build local privacy-safe document assistant</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 109</div>
            <div class="day-title">LangChain — LLM Application Framework</div>
            <ul class="day-list">
              <li>LangChain Expression Language (LCEL)</li>
              <li>Chains, PromptTemplates, OutputParsers</li>
              <li>Memory systems (ConversationBufferMemory, SQLite)</li>
              <li>Retrieval QA chain</li>
              <li>Practice: Build a SQL agent that translates text to queries</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 110–111</div>
            <div class="day-title">Project: AI Writing Assistant</div>
            <ul class="day-list">
              <li>Complete app: Flask backend + Tailwind CSS frontend</li>
              <li>Use local LLM (Ollama) or OpenAI API (user choice)</li>
              <li>Features: summarize, expand, change tone, fix grammar</li>
              <li>Include: dynamic sidebar, live character counts, copy button</li>
              <li>Deploy to GitHub with clean instructions</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>"""

new_w15_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 101</div>
            <div class="day-title">Prompt Engineering — Art of Talking to LLMs</div>
            <ul class="day-list">
              <li>Few-shot prompting, chain-of-thought, system prompts</li>
              <li>Structured outputs: JSON, function calling</li>
              <li>Prompt injections, guardrails, and safety</li>
              <li>Practice: Write robust templates for data extraction</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 102</div>
            <div class="day-title">LLM APIs — OpenAI, Anthropic & Google</div>
            <ul class="day-list">
              <li>Connecting to GPT-4o, Claude 3.5 Sonnet, Gemini 2.0</li>
              <li>Streaming responses, system messages</li>
              <li>Pricing, token counts, rate limit handling</li>
              <li>Building interactive chat UI CLI / Web demo</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 103</div>
            <div class="day-title">LangChain & LCEL — LLM Orchestration</div>
            <ul class="day-list">
              <li>LangChain Expression Language (LCEL)</li>
              <li>Chains, prompt templates, output parsers</li>
              <li>Memory systems (session state, buffer memory)</li>
              <li>Practice: Build SQL agent or query router</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 104</div>
            <div class="day-title">Vector Databases — Semantic Search</div>
            <ul class="day-list">
              <li>Dense representations: ChromaDB, FAISS, Pinecone</li>
              <li>Similarity metrics: Cosine, Dot Product, L2</li>
              <li>Indexing strategies and metadata filtering</li>
              <li>Practice: Indexing and querying 500 documents</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 105</div>
            <div class="day-title">Advanced RAG — Beyond Naive Retrieval</div>
            <ul class="day-list">
              <li>Query expansion, sub-queries, re-ranking</li>
              <li>Sentence window retrieval, parent document retriever</li>
              <li>Evaluating RAG pipelines with Ragas / TruLens</li>
              <li>Practice: Optimising retrieval accuracy</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 106</div>
            <div class="day-title">LLM Agents & Tool Use</div>
            <ul class="day-list">
              <li>ReAct loop (Reasoning + Action)</li>
              <li>Giving LLMs tools: search, calculator, custom python scripts</li>
              <li>State management and loops</li>
              <li>Practice: Build research agent that writes reports</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 107</div>
            <div class="day-title">Capstone — Agentic Systems</div>
            <ul class="day-list">
              <li>Designing and building a fully custom agentic app</li>
              <li>Handling multi-turn dialog and routing</li>
              <li>Benchmarking and user evaluation</li>
              <li>Deployment and portfolio publishing</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
        </div>"""

content = content.replace(old_w15_grid, new_w15_grid)

# 6. Week 16: Update days-grid
old_w16_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 112</div>
            <div class="day-title">RAG Architecture — The Complete Picture</div>
            <ul class="day-list">
              <li>Document parsing, chunking strategies (recursive character, semantic)</li>
              <li>Retrieval metrics: Hit rate, MRR, NDCG</li>
              <li>Prompt structures for context injections</li>
              <li>RAG limitations (hallucinations, multi-hop reasoning)</li>
              <li>Build simple in-memory RAG system</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 113</div>
            <div class="day-title">Vector Databases — ChromaDB + FAISS</div>
            <ul class="day-list">
              <li>ChromaDB: Setup, collection management, querying</li>
              <li>FAISS: Indexes (FlatL2, IVF, HNSW) and search speeds</li>
              <li>Metadata filtering for targeted context retrieval</li>
              <li>PyTorch sentence-transformers for embedding generations</li>
              <li>Practice: Store and search 1,000 PDF pages</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 114–115</div>
            <div class="day-title">Build a Complete RAG System</div>
            <ul class="day-list">
              <li>Architecture: User Query → Embeddings → Vector Search → Context Injection → LLM</li>
              <li>Implement: Sentence Window Retrieval for better precision</li>
              <li>Reranking: Use Cross-Encoders (cohre/bge-reranker)</li>
              <li>Gradio web application with source attribution highlights</li>
              <li>Deploy to Hugging Face Spaces</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 116</div>
            <div class="day-title">AI Agents + Tool Use</div>
            <ul class="day-list">
              <li>ReAct loop (Reasoning + Action)</li>
              <li>Exposing tools (search API, calculator, custom code runner)</li>
              <li>Handling multi-step loops, retry logic, tool exceptions</li>
              <li>LangChain Agents (Structured Chat, XML)</li>
              <li>Build research agent that scrapes web and writes summary</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 117</div>
            <div class="day-title">Advanced RAG Techniques</div>
            <ul class="day-list">
              <li>Query expansion (hypothetical document embeddings - HyDE)</li>
              <li>Parent Document Retriever</li>
              <li>RAG evaluation: Faithfulness, Answer Relevance, Context Recall (RAGAS framework)</li>
              <li>Comparing setups: chunk sizes vs retrieval parameters</li>
              <li>Optimize RAG system build on Day 114</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 118–120</div>
            <div class="day-title">Month 4 Major Project: Chat with Your Documents</div>
            <ul class="day-list">
              <li>Massive project: FastAPI backend + Next.js (or Streamlit) frontend</li>
              <li>Features: upload PDF/docx/txt, semantic indexing, conversational interface</li>
              <li>Optimizations: caching embeddings, streaming LLM tokens</li>
              <li>Observability: trace agent steps using LangSmith / Phoenix</li>
              <li>Complete GitHub repository with deployment config (Docker Compose)</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>"""

new_w16_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 108</div>
            <div class="day-title">Fine-Tuning LLMs — LoRA, QLoRA & PEFT</div>
            <ul class="day-list">
              <li>Quantisation: 4-bit, 8-bit precision (bitsandbytes)</li>
              <li>QLoRA: fine-tuning quantized models with LoRA adapters</li>
              <li>Supervised Fine-Tuning (SFT) Trainer from TRL</li>
              <li>Fine-tune Llama-3-8B/Mistral-7B on custom dataset</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 109</div>
            <div class="day-title">LLMOps — Tracing, Evaluation & Guardrails</div>
            <ul class="day-list">
              <li>Observability: Arize Phoenix, LangSmith, LangFuse</li>
              <li>Tracing LLM steps, latency, token consumption</li>
              <li>NeMo Guardrails: inputs, outputs, topical check</li>
              <li>Evaluating model responses for hallucination</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 110</div>
            <div class="day-title">Multi-Agent Systems — LangGraph & AutoGen</div>
            <ul class="day-list">
              <li>Multi-agent coordination: router, supervisor patterns</li>
              <li>LangGraph: graph-based stateful agent workflows</li>
              <li>AutoGen: conversational agents collaborating</li>
              <li>Build coding assistant and reviewer multi-agent app</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 111</div>
            <div class="day-title">Model Context Protocol (MCP) Standard</div>
            <ul class="day-list">
              <li>What is MCP? The open-source universal tool protocol</li>
              <li>Client-Server architecture of MCP</li>
              <li>Building custom MCP Servers to expose tools to LLMs</li>
              <li>Integrating MCP tools with cursor and coding assistants</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 112</div>
            <div class="day-title">FastAPI + Docker — Production Deployment</div>
            <ul class="day-list">
              <li>Designing high-concurrency async REST APIs in FastAPI</li>
              <li>Pydantic v2 schemas and request validation</li>
              <li>Containerizing FastAPI applications with Docker</li>
              <li>Configuring Gunicorn/Uvicorn workers for scale</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 113</div>
            <div class="day-title">Streaming Responses & Real-Time APIs</div>
            <ul class="day-list">
              <li>Server-Sent Events (SSE) protocol</li>
              <li>Async streaming generators in FastAPI</li>
              <li>Handling client-side chunks rendering</li>
              <li>WebSockets for duplex live chatting</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 114</div>
            <div class="day-title">Next.js & Vercel AI SDK</div>
            <ul class="day-list">
              <li>Setting up Next.js App Router for frontend UI</li>
              <li>Integrating Vercel AI SDK for hook-based streaming</li>
              <li>Building responsive chat interfaces</li>
              <li>Handling multi-modal inputs on the client</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 115</div>
            <div class="day-title">LLM Observability with LangSmith & Phoenix</div>
            <ul class="day-list">
              <li>Instrumenting production chains with OTEL telemetry</li>
              <li>Tracking agent step trace outputs</li>
              <li>Measuring user feedback and prompt versions</li>
              <li>Analyzing latency and costs of API calls</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 116</div>
            <div class="day-title">LLM Evaluation (RAGAS & TruLens)</div>
            <ul class="day-list">
              <li>Evaluating Answer Relevance and Context Recall</li>
              <li>Using LLM-as-a-judge for automated testing</li>
              <li>TruLens triad evaluation model</li>
              <li>Continuous evaluation in CI/CD pipelines</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--m4)">
            <div class="day-label">DAY 117</div>
            <div class="day-title">Week 16 Capstone: Production RAG</div>
            <ul class="day-list">
              <li>Building a full production RAG chatbot</li>
              <li>FastAPI async streaming backend + Next.js frontend</li>
              <li>Observability, vector databases, and caching</li>
              <li>Deploying multi-container stack to Render/Railway</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
        </div>"""

content = content.replace(old_w16_grid, new_w16_grid)

# 7. Week 17: Update days-grid
# Note: we also want to change the heading in this section
# Heading in raw backup was: <h2 style="color:var(--mfin)">Days 121–127 — Flask + Docker + Kubernetes + Deployment</h2>
# It was already replaced by fix_roadmap_master.py to: <h2 style="color:var(--mfin)">Week 17 — Days 118–124 — Flask + Docker + Kubernetes + Deployment</h2>
# We replace it with: <h2 style="color:var(--mfin)">Week 17 — Flask + Docker Deploy</h2>
content = content.replace(
    '<h2 style="color:var(--mfin)">Week 17 — Days 118–124 — Flask + Docker + Kubernetes + Deployment</h2>',
    '<h2 style="color:var(--mfin)">Week 17 — Flask + Docker Deploy</h2>'
)

# Replace days-grid for fin1
old_fin1_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 121</div>
            <div class="day-title">Flask — AI App Development</div>
            <ul class="day-list">
              <li>Flask routes, request/response, JSON API</li>
              <li>Loading ML model: pickle, joblib, TensorFlow SavedModel</li>
              <li>POST endpoint for predictions</li>
              <li>Jinja2 templates for HTML UI</li>
              <li>Build: prediction API for your best ML model</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 122</div>
            <div class="day-title">Flask Advanced + FastAPI</div>
            <ul class="day-list">
              <li>Flask: Blueprints, error handling, CORS</li>
              <li>FastAPI: async, Pydantic models, auto docs</li>
              <li>Why FastAPI &gt; Flask for ML APIs in 2026</li>
              <li>Build same API in both, compare</li>
              <li>Test with Thunder Client / curl</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 123</div>
            <div class="day-title">Docker — Containerise Everything</div>
            <ul class="day-list">
              <li>What is Docker? Why containers?</li>
              <li>Dockerfile: FROM, COPY, RUN, CMD, EXPOSE</li>
              <li>docker build, run, stop, push</li>
              <li>Docker Hub: push your AI app image</li>
              <li>Containerise your Flask ML API</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 124</div>
            <div class="day-title">Docker Compose + Multi-Container Apps</div>
            <ul class="day-list">
              <li>docker-compose.yml structure</li>
              <li>Services: app + database + vector store</li>
              <li>Networks and volumes</li>
              <li>Environment variables with .env files</li>
              <li>Compose your RAG app with app + ChromaDB</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 125</div>
            <div class="day-title">Kubernetes Basics (Conceptual + Hands-on)</div>
            <ul class="day-list">
              <li>Pods, Deployments, Services, Ingress</li>
              <li>kubectl basics: apply, get, describe, logs</li>
              <li>Minikube for local K8s</li>
              <li>Deploy your Flask app on local K8s cluster</li>
              <li>Why K8s matters for production ML systems</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 126</div>
            <div class="day-title">Cloud Deployment — Free Platforms</div>
            <ul class="day-list">
              <li>Hugging Face Spaces: Gradio apps for free</li>
              <li>Render.com: deploy Docker containers free</li>
              <li>Railway.app: PostgreSQL + app together</li>
              <li>GitHub Actions: CI/CD pipeline basics</li>
              <li>Deploy 2 projects on different platforms</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 127</div>
            <div class="day-title">MLOps Basics + Experiment Tracking</div>
            <ul class="day-list">
              <li>What is MLOps? The lifecycle of an ML system</li>
              <li>MLflow: experiment tracking, model registry (free)</li>
              <li>Weights & Biases free tier</li>
              <li>Model versioning best practices</li>
              <li>Add MLflow tracking to your best model</li>
            </ul>
            <div class="day-hours">⏱ 4 hrs</div>
          </div>
        </div>"""

new_fin1_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 118</div>
            <div class="day-title">Flask Fundamentals — Routes & Views</div>
            <ul class="day-list">
              <li>Flask setup, routing rules, template rendering</li>
              <li>Handling GET/POST requests and form data</li>
              <li>Using Blueprints for application organization</li>
              <li>Building simple HTML frontends for ML models</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 119</div>
            <div class="day-title">REST API Design — JSON & Versioning</div>
            <ul class="day-list">
              <li>RESTful architecture principles</li>
              <li>Serializing and deserializing JSON payloads</li>
              <li>Custom error handlers and HTTP status codes</li>
              <li>API versioning (v1/v2) best practices</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 120</div>
            <div class="day-title">Serving ML Models with Flask</div>
            <ul class="day-list">
              <li>Loading models via Pickle and Joblib</li>
              <li>Handling model inference inside Flask routes</li>
              <li>Configuring Gunicorn for WSGI production serving</li>
              <li>Benchmarking prediction endpoints under load</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 121</div>
            <div class="day-title">Docker Fundamentals — Containers</div>
            <ul class="day-list">
              <li>Understanding container virtualization vs virtual machines</li>
              <li>Core commands: docker pull, build, run, stop, ps, logs</li>
              <li>Exposing container ports and checking networks</li>
              <li>Pushing built images to Docker Hub repository</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 122</div>
            <div class="day-title">Writing Dockerfiles & Multi-Stage Builds</div>
            <ul class="day-list">
              <li>Dockerfile directives: FROM, COPY, RUN, CMD, ENV</li>
              <li>Optimizing layers and caching for fast builds</li>
              <li>Writing multi-stage builds to minimize image sizes</li>
              <li>Practice: Containerizing Flask and FastAPI ML APIs</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 123</div>
            <div class="day-title">Docker Compose — Multi-Container Stacks</div>
            <ul class="day-list">
              <li>Defining services in docker-compose.yml</li>
              <li>Setting up network bridging between containers</li>
              <li>Configuring environment variables via .env files</li>
              <li>Compose stack: Flask web app + Chroma DB server</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 124</div>
            <div class="day-title">Week 17 Capstone — Production ML System</div>
            <ul class="day-list">
              <li>Building and containerizing an end-to-end ML API</li>
              <li>Setting up multi-container docker compose pipeline</li>
              <li>Deploying containerized stack to Render/Railway</li>
              <li>Verifying live endpoint using curl requests</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs</div>
          </div>
        </div>"""

content = content.replace(old_fin1_grid, new_fin1_grid)

# 8. Week 18 / Capstone: Update heading and tag, and replace days-grid
content = content.replace(
    '<div class="section-tag">FINAL · DAYS 128–135</div>',
    '<div class="section-tag">FINAL · DAYS 125–135</div>'
)
content = content.replace(
    '<h2 style="color:var(--mfin)">Days 128–135 — Capstone Project + Portfolio Polish</h2>',
    '<h2 style="color:var(--mfin)">Week 18 — Capstone & Portfolio Polish</h2>'
)

# Expose K8s / Cloud deploy / MLOps in Day 125-127 cards inside fin2
old_fin2_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 128–131</div>
            <div class="day-title">CAPSTONE PROJECT — Choose Your Track</div>
            <ul class="day-list">
              <li>Track A: Production RAG chatbot (FastAPI backend + Next.js frontend + vector store)</li>
              <li>Track B: Advanced Computer Vision app (YOLO/U-Net + Flask API + Render deploy)</li>
              <li>Track C: Fine-tuned LLM classifier (QLoRA mistral/llama fine-tune + Gradio dashboard)</li>
              <li>Must include: complete EDA, model pipeline, dockerization, and live cloud deployment</li>
            </ul>
            <div class="day-hours">⏱ 6–8 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 132</div>
            <div class="day-title">GitHub Portfolio Polish</div>
            <ul class="day-list">
              <li>Create a high-impact GitHub profile readme and pinned repositories</li>
              <li>For all 4 main projects: clean code, requirements.txt, and complete README.md</li>
              <li>Add system design architecture flowcharts to project write-ups</li>
              <li>Verify no API keys or database credentials are exposed in git history</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 133</div>
            <div class="day-title">Resume + LinkedIn Optimisation</div>
            <ul class="day-list">
              <li>Refactor resume to list projects using STAR method (focus on metrics and tech)</li>
              <li>Incorporate key terms: PyTorch, scikit-learn, Docker, FastAPI, RAG, MLOps</li>
              <li>Optimize LinkedIn profile headline, summary, and experience sections</li>
              <li>Publish a summary post of your roadmap journey to build a personal brand</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 134–135</div>
            <div class="day-title">Final Interview Prep Sprint</div>
            <ul class="day-list">
              <li>Algorithm walkthroughs: Linear Reg derivation, SVM math, Transformer self-attention</li>
              <li>System design mock interviews: scaling ML APIs, caching database retrieval results</li>
              <li>Coding practice: top 20 ML engineering coding questions (LeetCode/HackerRank)</li>
              <li>Celebrate completion of the 135-day roadmap! 🎓</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>"""

new_fin2_grid = """        <div class="days-grid">
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 125</div>
            <div class="day-title">Kubernetes Basics</div>
            <ul class="day-list">
              <li>Pods, Deployments, Services, and Ingress</li>
              <li>Using kubectl: apply, get, describe, logs, delete</li>
              <li>Running Minikube locally for development</li>
              <li>Deploying containerized Flask app on local cluster</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 126</div>
            <div class="day-title">Cloud Deployment — Render & Railway</div>
            <ul class="day-list">
              <li>Configuring Render/Railway for continuous deployment</li>
              <li>Setting up automatic build hooks from GitHub</li>
              <li>Configuring persistent disks and environmental secrets</li>
              <li>Building basic CI/CD pipeline using GitHub Actions</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 127</div>
            <div class="day-title">MLOps Basics + Experiment Tracking</div>
            <ul class="day-list">
              <li>What is MLOps? Lifecycle of ML models</li>
              <li>Setting up MLflow tracking server locally</li>
              <li>Logging hyper-parameters, metrics, and models</li>
              <li>Using weights & biases for training telemetry</li>
            </ul>
            <div class="day-hours">⏱ 4 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 128–131</div>
            <div class="day-title">CAPSTONE PROJECT — Choose Your Track</div>
            <ul class="day-list">
              <li>Track A: Production RAG application with Next.js frontend</li>
              <li>Track B: Advanced computer vision app deployed to cloud</li>
              <li>Track C: Fine-tuned LLM chatbot specialized in domain</li>
              <li>Implement: EDA, model pipeline, logging, UI, dockerized deploy</li>
            </ul>
            <div class="day-hours">⏱ 6-8 hrs/day</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 132</div>
            <div class="day-title">GitHub Portfolio Polish</div>
            <ul class="day-list">
              <li>Refactoring capstone repository for clean code structure</li>
              <li>Writing a professional README with architecture diagrams</li>
              <li>Adding requirements.txt, Dockerfiles, and setup scripts</li>
              <li>Creating clean repository landing page (pinned repos)</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 133</div>
            <div class="day-title">Resume & LinkedIn Optimization</div>
            <ul class="day-list">
              <li>Adding AI/ML projects and tech keywords to resume</li>
              <li>Formatting work experience for ML engineer roles</li>
              <li>Writing LinkedIn profile headline and about sections</li>
              <li>Publishing first "Build in Public" post about Capstone</li>
            </ul>
            <div class="day-hours">⏱ 5 hrs</div>
          </div>
          <div class="day-card" style="border-left-color:var(--mfin)">
            <div class="day-label">DAY 134–135</div>
            <div class="day-title">Final Interview Prep Sprint & Celebration</div>
            <ul class="day-list">
              <li>Mock interview questions on ML theory and system design</li>
              <li>Reviewing coding and system design cheat sheets</li>
              <li>Exposing endpoints and sharing portfolios on social channels</li>
              <li>Celebrating roadmap completion and setting next steps!</li>
            </ul>
            <div class="day-hours">⏱ 6 hrs/day</div>
          </div>
        </div>"""

content = content.replace(old_fin2_grid, new_fin2_grid)

# Save changes
with open(roadmap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("roadmap.html day tags and grids aligned successfully!")
