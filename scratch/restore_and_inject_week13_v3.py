with open('/Users/amananand/Downloads/SDE/ai:ml/_backup/week13.html', 'r', encoding='utf-8') as f:
    backup_content = f.read()

content = backup_content

new_diagrams = {
    88: """    <div class="mermaid">
      graph TD
      Docs["Documents List"] --> TF["Term Frequency (TF) <br/> How often word appears in document"]
      Docs --> IDF["Inverse Document Frequency (IDF) <br/> How rare word is across all documents"]
      TF --> Vector["TF-IDF Vector: TF * IDF <br/> High weight for important, discriminative words"]
      IDF --> Vector
    </div>\n    <div class="diagram-cap">TF-IDF term weighting vectorization flow</div>""",
    90: """    <div class="mermaid">
      graph LR
      Input["Sentence: Apple bought Beats in 2014"] --> POS["POS Tagger: <br/> Apple (PROPN), bought (VERB), Beats (PROPN), in (ADP), 2014 (NUM)"]
      Input --> NER["NER Tagger: <br/> Apple (ORG), Beats (ORG), 2014 (DATE)"]
    </div>\n    <div class="diagram-cap">POS and NER sequence tagging pipeline</div>""",
    91: """    <div class="mermaid">
      graph LR
      Text["Input Text Article"] --> Preproc["Tokenizer & Embedding Layer"] --> Classifier["Machine Learning Classifier (Naïve Bayes / SVM)"] --> Output["Label: Real or Fake News"]
    </div>\n    <div class="diagram-cap">Fake news text classification flow</div>""",
    92: """    <div class="mermaid">
      graph LR
      Tokens["Tokens: x_1, x_2, ..., x_t"] --> LSTM["LSTM Hidden Layer (States h_t)"] --> Dense["Dense Layer"] --> Output["Label (e.g. Sentiment probability)"]
    </div>\n    <div class="diagram-cap">Recurrent sequence classification architecture</div>""",
    93: """    <div class="mermaid">
      graph TD
      Raw["Raw Customer Reviews"] --> Pipeline["Modular spacy NLP Preprocessing Pipeline"] --> Vectorizer["TF-IDF / Word2Vec Embeddings"] --> Model["Trained Classifier Model"] --> Eval["Validation Metrics: Accuracy, Precision, Recall, F1"]
    </div>\n    <div class="diagram-cap">NLP capstone pipeline & model evaluation sequence</div>"""
}

new_resources = {
    87: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://spacy.io/usage/spacy-101" target="_blank">
        <div class="rc-type">📖 OFFICIAL</div>
        <div class="rc-title">spaCy 101: spaCy Fundamentals</div>
        <div class="rc-sub">Official walkthrough explaining pipelines, tokenization, and parsing in spaCy.</div>
      </a>
    </div>
  </div>""",
    88: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html" target="_blank">
        <div class="rc-type">📖 OFFICIAL</div>
        <div class="rc-title">TfidfVectorizer Documentation</div>
        <div class="rc-sub">Official Scikit-Learn documentation for TF-IDF feature extraction.</div>
      </a>
    </div>
  </div>""",
    89: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://jalammar.github.io/illustrated-word2vec/" target="_blank">
        <div class="rc-type">📝 ARTICLE</div>
        <div class="rc-title">The Illustrated Word2Vec — Jay Alammar</div>
        <div class="rc-sub">The classic visual guide explaining word vectors, CBOW, and Skip-Gram.</div>
      </a>
    </div>
  </div>""",
    90: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://course.spacy.io/en/" target="_blank">
        <div class="rc-type">🌐 COURSE</div>
        <div class="rc-title">spaCy 101 Interactive Course</div>
        <div class="rc-sub">The official interactive course covering advanced NLP pipelines in spaCy.</div>
      </a>
    </div>
  </div>""",
    91: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://huggingface.co/learn/nlp-course/chapter1/1" target="_blank">
        <div class="rc-type">🌐 COURSE</div>
        <div class="rc-title">Hugging Face NLP Course: Chapter 1</div>
        <div class="rc-sub">Introduction to NLP, tokenization, and transformer models.</div>
      </a>
    </div>
  </div>""",
    92: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://keras.io/examples/nlp/text_classification_from_scratch/" target="_blank">
        <div class="rc-type">💻 PRACTICE</div>
        <div class="rc-title">Keras Text Classification from Scratch</div>
        <div class="rc-sub">Complete code for training recurrent models on sentiment data.</div>
      </a>
    </div>
  </div>""",
    93: """  <div id="resources-section">
    <h2 class="sh2">📚 Resources</h2>
    <div class="resources-grid">
      <a class="resource-card" href="https://spacy.io/usage/processing-pipelines" target="_blank">
        <div class="rc-type">📖 OFFICIAL</div>
        <div class="rc-title">spaCy Language Processing Pipelines</div>
        <div class="rc-sub">Official guide to writing custom components and processing pipelines in spaCy.</div>
      </a>
    </div>
  </div>"""
}

# 1. Inject diagrams right after their first h3 elements
print("Injecting diagrams...")
day_h3s = {
    88: '<h3 class="sh3">1. Bag of Words (BoW) & Sparsity Constraints</h3>',
    90: '<h3 class="sh3">1. Syntactic Foundations: POS Tagging</h3>',
    91: '<h3 class="sh3">1. Document-Level vs. Token-Level Labeling</h3>',
    92: '<h3 class="sh3">1. Fake News Detection Pipeline</h3>',
    93: '<h3 class="sh3">1. Web Architecture: Gradio Blocks API</h3>'
}

for day_num, h3_tag in day_h3s.items():
    idx = content.find(h3_tag)
    if idx != -1:
        # We find the next closing paragraph or div to insert the diagram cleanly
        p_end = content.find('</p>', idx)
        if p_end != -1:
            insert_pos = p_end + 4
            content = content[:insert_pos] + "\\n\\n" + new_diagrams[day_num] + "\\n" + content[insert_pos:]
            print(f"  Injected diagram in Day {day_num}")
        else:
            print(f"  Could not find paragraph end for Day {day_num}")
    else:
        print(f"  Could not find h3 tag for Day {day_num}")

# 2. Inject resources sections at the end of each day
print("Injecting resources...")
for day_num in range(87, 94):
    closing_tag = f"</div><!-- /day-{day_num} -->"
    closing_idx = content.find(closing_tag)
    if closing_idx != -1:
        new_block = "\\n\\n" + new_resources[day_num] + "\\n\\n"
        content = content[:closing_idx] + new_block + content[closing_idx:]
        print(f"  Injected resources for Day {day_num}")
    else:
        print(f"  Warning: closing tag for Day {day_num} not found!")

# Save to file
with open('/Users/amananand/Downloads/SDE/ai:ml/week13.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved week13.html")
