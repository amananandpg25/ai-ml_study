import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

# 1. Resource Data for Week 12
w12_resources = {
    80: [
        {"type": "Blog", "title": "Lilian Weng — Attention Mechanism", "desc": "The definitive mathematical and conceptual breakdown of attention.", "url": "https://lilianweng.github.io/posts/2018-06-24-attention/"},
        {"type": "Visualisation", "title": "Jay Alammar — Illustrated Attention", "desc": "Visualizing neural machine translation mechanics step-by-step.", "url": "http://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/"},
        {"type": "YouTube", "title": "Andrej Karpathy — Attention Lecture", "desc": "Build GPT/attention blocks from scratch in PyTorch.", "url": "https://www.youtube.com/watch?v=kCc8FmEb1nY"},
        {"type": "Tutorial", "title": "BLEU Score Metric in Python", "desc": "How to calculate BLEU scores for machine translations.", "url": "https://machinelearningmastery.com/calculate-bleu-score-for-text-python/"}
    ],
    81: [
        {"type": "Tutorial", "title": "PyTorch Seq2Seq Translation", "desc": "Official PyTorch tutorial on sequence-to-sequence translation.", "url": "https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html"},
        {"type": "Paper", "title": "Show and Tell: A Neural Image Caption Generator", "desc": "Landmark paper introducing CNN encoders and LSTM decoders.", "url": "https://arxiv.org/abs/1411.4555"},
        {"type": "GitHub", "title": "PyTorch Image Captioning GitHub", "desc": "Clean PyTorch implementation of image captioning.", "url": "https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning"}
    ],
    82: [
        {"type": "Dataset", "title": "Flickr8k Dataset (Kaggle)", "desc": "Download link and notebooks for Flickr8k captioning dataset.", "url": "https://www.kaggle.com/datasets/adityadn/flickr8k"},
        {"type": "Paper", "title": "MobileNetV2: Inverted Residuals & Bottlenecks", "desc": "MobileNetV2 architecture details for lightweight visual backbones.", "url": "https://arxiv.org/abs/1801.04381"},
        {"type": "Docs", "title": "PyTorch Transfer Learning Guide", "desc": "Learn how to use pre-trained backbones in PyTorch.", "url": "https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html"}
    ],
    83: [
        {"type": "Docs", "title": "PyTorch Custom Modules & Layers", "desc": "Tutorial on subclassing nn.Module to define custom layers.", "url": "https://pytorch.org/tutorials/beginner/pytorch_with_examples.html"},
        {"type": "Blog", "title": "Colah — Understanding LSTM Networks", "desc": "The most famous blog post explaining LSTM gates visually.", "url": "https://colah.github.io/posts/2015-08-LSTM/"}
    ],
    84: [
        {"type": "Docs", "title": "NLTK BLEU Score API Documentation", "desc": "Official reference for calculating BLEU-1 to BLEU-4.", "url": "https://www.nltk.org/api/nltk.translate.bleu_score.html"},
        {"type": "Tutorial", "title": "PyTorch Custom Training Loops", "desc": "Standard PyTorch training loops with loss tracking.", "url": "https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html"}
    ],
    85: [
        {"type": "Blog", "title": "Greedy vs Beam Search Decoding", "desc": "Detailed comparison of inference search heuristics in NLP.", "url": "https://machinelearningmastery.com/beam-search-decoder-natural-language-processing/"},
        {"type": "Blog", "title": "How to Sample from Language Models", "desc": "Understanding temperature, top-k, and top-p sampling.", "url": "https://towardsdatascience.com/how-to-sample-from-language-models-682b686b245e"}
    ],
    86: [
        {"type": "Docs", "title": "Gradio Blocks Documentation", "desc": "How to design premium multi-column layouts using gr.Blocks.", "url": "https://gradio.app/docs/#blocks"},
        {"type": "Docs", "title": "Hugging Face Spaces Deployment", "desc": "Official guide to deploying Gradio apps on HF Hub.", "url": "https://huggingface.co/docs/hub/spaces-overview"}
    ]
}

# 2. Resource Data for Week 13
w13_resources = {
    87: [
        {"type": "Course", "title": "spaCy 101 — Official Course", "desc": "Free interactive course covering tokenization & pipelines.", "url": "https://course.spacy.io/en/"},
        {"type": "Book", "title": "NLTK Book (Free Online)", "desc": "Natural Language Processing with Python - complete book.", "url": "https://www.nltk.org/book/"},
        {"type": "Tool", "title": "Regexr — Interactive Regex Guide", "desc": "Write, debug, and test regular expressions for text cleaning.", "url": "https://regexr.com/"}
    ],
    88: [
        {"type": "Docs", "title": "Scikit-Learn Text Feature Extraction", "desc": "Documentation for CountVectorizer and TfidfVectorizer.", "url": "https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction"},
        {"type": "Blog", "title": "TF-IDF Explained & Implemented", "desc": "A complete mathematical explanation of term weighting.", "url": "https://towardsdatascience.com/tf-idf-explained-and-implemented-with-python-39649541f282"}
    ],
    89: [
        {"type": "Docs", "title": "Hugging Face Word2Vec Model Hub", "desc": "Load pre-trained Word2Vec vectors in python.", "url": "https://huggingface.co/docs/transformers/model_doc/word2vec"},
        {"type": "Notes", "title": "Stanford CS224N Word Vector Notes", "desc": "Official Stanford Deep Learning NLP lecture notes on word vectors.", "url": "https://web.stanford.edu/class/cs224n/readings/cs224n-2019-notes01-wordvecs1.pdf"},
        {"type": "Paper", "title": "Word2Vec (Mikolov et al.)", "desc": "The seminal Google paper on efficient vector estimation of words.", "url": "https://arxiv.org/abs/1301.3781"}
    ],
    90: [
        {"type": "Docs", "title": "spaCy Named Entity Recognition", "desc": "Extracting entities like GPE, ORG, and PERSON.", "url": "https://spacy.io/usage/linguistic-features#named-entities"},
        {"type": "Docs", "title": "spaCy Part-of-Speech Tagging", "desc": "Linguistic features and dependency parsers in spaCy.", "url": "https://spacy.io/usage/linguistic-features#pos-tagging"}
    ],
    91: [
        {"type": "Tutorial", "title": "PyTorch LSTM Sequence Classifier", "desc": "Sequence models and LSTM classifiers in PyTorch.", "url": "https://pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html"},
        {"type": "Blog", "title": "Conditional Random Fields (CRF)", "desc": "How CRF layers optimize structured sequence tag labelings.", "url": "https://towardsdatascience.com/conditional-random-fields-explained-e5812c236a85"}
    ],
    92: [
        {"type": "Paper", "title": "TextRank: Bringing Order into Text", "desc": "Mihalcea & Tarau paper introducing PageRank for summaries.", "url": "https://arxiv.org/abs/1408.1134"},
        {"type": "Blog", "title": "Text Summarization using TF-IDF", "desc": "Simple extractive document summarization using python.", "url": "https://towardsdatascience.com/text-summarization-using-tf-idf-e3db91ecbff9"}
    ],
    93: [
        {"type": "Docs", "title": "Gradio Benchmarking & Metrics", "desc": "How to measure inference speeds in Gradio Blocks interfaces.", "url": "https://gradio.app/docs/"},
        {"type": "Docs", "title": "Hugging Face Evaluate Library", "desc": "Universal evaluate API for classification metrics.", "url": "https://huggingface.co/docs/evaluate/index"}
    ]
}

def inject_resources(file_path, resources):
    content = open(file_path, 'r', encoding='utf-8').read()
    
    for day, cards in resources.items():
        # Build injected HTML
        cards_html = ""
        for c in cards:
            cards_html += f"""
    <a class="resource-card" href="{c['url']}" target="_blank">
      <div class="rc-type">{c['type']}</div>
      <h4>{c['title']}</h4>
      <p class="rc-sub">{c['desc']}</p>
    </a>"""
            
        injected_html = f"""
  <div id="day-{day}-resources-section">
  <h2 class="sh2">📚 Day {day} Resources</h2>
  <div class="resources-grid">{cards_html}
  </div>
  </div>
  
  """
        
        # We find the complete button for this day
        btn_pattern = rf'<button class="complete-btn" id="btn-day-{day}"'
        if btn_pattern in content:
            content = content.replace(btn_pattern, injected_html + btn_pattern)
            print(f"  Injected resources for Day {day} in {os.path.basename(file_path)}")
        else:
            # Fallback for week12.html / week13.html closing tag style without spacing
            btn_pattern_no_space = rf'<button class="complete-btn" id="btn-day-{day}"'
            print(f"  Warning: complete-btn for Day {day} not found in {os.path.basename(file_path)}")
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Injecting resources into week12.html...")
inject_resources(os.path.join(base_dir, "week12.html"), w12_resources)

print("Injecting resources into week13.html...")
inject_resources(os.path.join(base_dir, "week13.html"), w13_resources)

print("Finished resource injection script!")
