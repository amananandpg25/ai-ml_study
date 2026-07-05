# AI/ML Roadmap Coursework - Content Audit Report

This report documents all structural, logical, typographic, and gamification issues found in the coursework files (`week*.html`, `roadmap.html`, `dashboard.html`, `resources.html`).

## Executive Summary

- **Total Issues Identified**: 86
- **Critical (Actionable Bugs)**: 0
- **Medium (Code Escapes, Math Delimiters)**: 69
- **Warning / Low (Inconsistencies, Typos, Code Cleanliness)**: 17

---

## Issues List


## [MEDIUM] Severity Issues

### Slop/Placeholder Content in `resources.html` (Line 723)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  trip up many beginners with unexpected NaN results. ✪ Best for: Day 15 missing val
  ```

### Literal Escape in Code Block in `week10.html` (Line 213)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import numpy as np  # 1. Define sequence shapes (Batch size = 1, Timesteps = 3, Features = 2) timesteps = 3 features = 2
  ```

### Slop/Placeholder Content in `week10.html` (Line 712)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  ion, causing parameters to overflow to `NaN`.          To solve this, we use **Grad
  ```

### Slop/Placeholder Content in `week10.html` (Line 712)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  y brakes clip karke gaadi ko slip hone (NaN crash) se bacha leta hai. Layer Normali
  ```

### Slop/Placeholder Content in `week10.html` (Line 712)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  enting exploding gradients from causing NaN parameter overflows. CBy skipping backp
  ```

### Literal Escape in Code Block in `week10.html` (Line 1563)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import numpy as np import tensorflow as tf from tensorflow.keras.preprocessing.text import Tokenizer from tensorflow.ker
  ```

### Slop/Placeholder Content in `week11.html` (Line 309)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  AThe Discriminator gradients explode to NaN. BThe Generator collapses to outputting
  ```

### Slop/Placeholder Content in `week12.html` (Line 400)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  ntially, causing numerical instability (NaN values).     We enforce gradient clippi
  ```

### Slop/Placeholder Content in `week12.html` (Line 400)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  loding gradients that trigger numerical NaN instability. BIt scales down the model'
  ```

### Slop/Placeholder Content in `week12.html` (Line 400)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  A: The loss value suddenly turns into "NaN" or "inf" after a few batches, and the
  ```

### Unbalanced Math Delimiters in `week13.html` (Line 2585)
- **Severity**: MEDIUM
- **Description**: Odd count of '$' (201) in file. Last '$' is likely unclosed math or unescaped currency.
- **Context**:
  ```html
  re, and $d$ is a constant gap
  ```

### Slop/Placeholder Content in `week13.html` (Line 2691)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  ing LSTM-CRF training fail with massive NaN outputs  Symptom: PyTorch loss updates
  ```

### Slop/Placeholder Content in `week13.html` (Line 2691)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  Symptom: PyTorch loss updates trigger NaN after a few steps.       Resolution: In
  ```

### Slop/Placeholder Content in `week14.html` (Line 318)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  rrect probability distributions without NaN errors for large numbers.git add . && g
  ```

### Literal Escape in Code Block in `week15.html` (Line 558)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  from openai import OpenAI import os, tiktoken  client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])  # --- Basic call -
  ```

### Literal Escape in Code Block in `week15.html` (Line 797)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  from openai import OpenAI import tiktoken, os  client = OpenAI() enc = tiktoken.encoding_for_model("gpt-4o-mini")  SYSTE
  ```

### Literal Escape in Code Block in `week15.html` (Line 1227)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  from langchain_openai import ChatOpenAI from langchain_core.prompts import ChatPromptTemplate from langchain_core.output
  ```

### Literal Escape in Code Block in `week15.html` (Line 1670)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import chromadb from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction  # Sample notes (in
  ```

### Literal Escape in Code Block in `week15.html` (Line 1938)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  from langchain_text_splitters import RecursiveCharacterTextSplitter  # RecursiveCharacterTextSplitter is the best genera
  ```

### Literal Escape in Code Block in `week15.html` (Line 2104)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  # pip install pypdf rank-bm25 sentence-transformers chromadb langchain openai from pypdf import PdfReader from langchain
  ```

### Literal Escape in Code Block in `week15.html` (Line 2376)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import json, openai, math  client = openai.OpenAI()  # --- Define tools as JSON schemas --- TOOLS = [     {         "typ
  ```

### Literal Escape in Code Block in `week16.html` (Line 247)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n', '\\"'] instead of actual characters.
- **Context**:
  ```html
  from datasets import Dataset  # --- Alpaca format --- alpaca_examples = [     {         "instruction": "Explain gradient
  ```

### Literal Escape in Code Block in `week16.html` (Line 307)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  # Option A: Save just the LoRA adapters (tiny, ~16MB for r=16) peft_model.save_pretrained("./my_lora_adapter") tokenizer
  ```

### Literal Escape in Code Block in `week16.html` (Line 373)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n', '\\"'] instead of actual characters.
- **Context**:
  ```html
  import json, openai from datasets import Dataset from tqdm import tqdm  client = openai.OpenAI()  SEED_EXAMPLES = [
  ```

### Literal Escape in Code Block in `week16.html` (Line 667)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\"'] instead of actual characters.
- **Context**:
  ```html
  import os  # 3 env vars — that's all LangSmith needs os.environ["\"LANGCHAIN_TRACING_V2\""]   = "true" os.environ["\"LAN
  ```

### Literal Escape in Code Block in `week16.html` (Line 703)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\"'] instead of actual characters.
- **Context**:
  ```html
  from langsmith import Client from langsmith.evaluation import evaluate, LangChainStringEvaluator  client = Client()  # 1
  ```

### Literal Escape in Code Block in `week16.html` (Line 1090)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\"'] instead of actual characters.
- **Context**:
  ```html
  from langgraph.graph import StateGraph, END from langgraph.prebuilt import ToolNode from langchain_openai import ChatOpe
  ```

### Literal Escape in Code Block in `week16.html` (Line 1143)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\"'] instead of actual characters.
- **Context**:
  ```html
  from langgraph.checkpoint.memory import MemorySaver  # compile with checkpointer for persistence and interrupts memory =
  ```

### Literal Escape in Code Block in `week16.html` (Line 1263)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\"'] instead of actual characters.
- **Context**:
  ```html
  # Graph structure: # START → classify_query → {needs_search: web_search, no_search: generate_report} → END # With interr
  ```

### Literal Escape in Code Block in `week16.html` (Line 1915)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n', '\\"'] instead of actual characters.
- **Context**:
  ```html
  # pip install fastapi uvicorn["standard"] pydantic openai chromadb sentence-transformers from fastapi import FastAPI, De
  ```

### Unbalanced Math Delimiters in `week16.html` (Line 2048)
- **Severity**: MEDIUM
- **Description**: Odd count of '$' (9) in file. Last '$' is likely unclosed math or unescaped currency.
- **Context**:
  ```html
  - API_KEY=${API_KEY}       - R
  ```

### Literal Escape in Code Block in `week16.html` (Line 2352)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  from fastapi import FastAPI from fastapi.responses import StreamingResponse from openai import AsyncOpenAI from pydantic
  ```

### Literal Escape in Code Block in `week16.html` (Line 2399)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  async function streamChat(message, historyDiv) {     // Use fetch for POST SSE (EventSource only supports GET)     const
  ```

### Literal Escape in Code Block in `week16.html` (Line 2439)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\"'] instead of actual characters.
- **Context**:
  ```html
  # pip install streamlit openai # streamlit run app.py import streamlit as st from openai import OpenAI  st.title("🤖 AI C
  ```

### Literal Escape in Code Block in `week17.html` (Line 576)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\"'] instead of actual characters.
- **Context**:
  ```html
  from flask import Flask, request, g from flask_limiter import Limiter from flask_limiter.util import get_remote_address
  ```

### Unbalanced Math Delimiters in `week18.html` (Line 1569)
- **Severity**: MEDIUM
- **Description**: Odd count of '$' (5) in file. Last '$' is likely unclosed math or unescaped currency.
- **Context**:
  ```html
  local/bin:$PATH EXPOSE 8000 CM
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  Priya | 92"]         LJ3["ID 3: Arjun | NaN"]     end      L1 --> IJ1     R1 --> IJ
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  l | 85.0 2  | Priya | 92.0 3  | Arjun | NaN     3. Right Merge (how='right')     L
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  | Rahul | 85.0 2  | Priya | 92.0 4  | NaN   | 78.0     4. Outer Merge (how='outer
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  l | 85.0 2  | Priya | 92.0 3  | Arjun | NaN 4  | NaN   | 78.0   Visual comparison o
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  2  | Priya | 92.0 3  | Arjun | NaN 4  | NaN   | 78.0   Visual comparison of inner,
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  n, while missing values are filled with NaN.  In ML, you'll often merge feature tab
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  OF 4 What does  do by default? A Fills NaN with 0 B Drops any row that has at leas
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  0 B Drops any row that has at least one NaN C Drops columns with more than 50% NaN
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  NaN C Drops columns with more than 50% NaN D Replaces NaN with column mean ✅ Corre
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  lumns with more than 50% NaN D Replaces NaN with column mean ✅ Correct! dropna() by
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  t drops any row containing at least one NaN. Use dropna(subset=["col"]) to only dro
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  to only drop rows where ALL values are NaN. ❌ dropna() removes rows with ANY null
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  m left table, matching rows from right (NaN for no match). This mirrors SQL LEFT JO
  ```

### Slop/Placeholder Content in `week2.html` (Line 331)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  s, "$5,000" salaries, date strings, and NaN values).Load it.Notice how Pandas reads
  ```

### Unbalanced Math Delimiters in `week2.html` (Line 2579)
- **Severity**: MEDIUM
- **Description**: Odd count of '$' (11) in file. Last '$' is likely unclosed math or unescaped currency.
- **Context**:
  ```html
  : {r[1]} (${r[2]}k)") conn.clo
  ```

### Slop/Placeholder Content in `week3.html` (Line 138)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  sion, RandomForest, etc.) cannot handle NaN values by default — they will throw a V
  ```

### Slop/Placeholder Content in `week3.html` (Line 138)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  ost always wrong:     Filling numerical NaN with 0 tells the model "this value IS z
  ```

### Slop/Placeholder Content in `week4.html` (Line 2762)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  -15)` when taking logarithms to prevent NaN errors. KL Divergence measures differen
  ```

### Slop/Placeholder Content in `week5.html` (Line 549)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  : Target values contain missing values (NaN) or inputs have extreme outliers causin
  ```

### Slop/Placeholder Content in `week5.html` (Line 549)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  y, Country categorical values, and some NaN inputs). Define ColumnTransformer for s
  ```

### Unbalanced Math Delimiters in `week5.html` (Line 1596)
- **Severity**: MEDIUM
- **Description**: Odd count of '$' (35) in file. Last '$' is likely unclosed math or unescaped currency.
- **Context**:
  ```html
  ; large $k$ values smooth boun
  ```

### Slop/Placeholder Content in `week6.html` (Line 22)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'undefined' (undefined literal in text (could indicate JavaScript parsing bug)).
- **Context**:
  ```html
  ew features are useful D Adjusted R² is undefined when R² > 0.8 ✅ Correct! R² can only in
  ```

### Unbalanced Math Delimiters in `week6.html` (Line 1710)
- **Severity**: MEDIUM
- **Description**: Odd count of '$' (21) in file. Last '$' is likely unclosed math or unescaped currency.
- **Context**:
  ```html
  ative $R^2$ indicates that you
  ```

### Literal Escape in Code Block in `week7.html` (Line 176)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import numpy as np import matplotlib.pyplot as plt from sklearn.svm import SVC from sklearn.datasets import load_breast_
  ```

### Literal Escape in Code Block in `week7.html` (Line 464)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import numpy as np from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text from sklearn.datasets import
  ```

### Literal Escape in Code Block in `week7.html` (Line 748)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import numpy as np import matplotlib.pyplot as plt from sklearn.ensemble import RandomForestClassifier, BaggingClassifie
  ```

### Literal Escape in Code Block in `week7.html` (Line 1030)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import numpy as np import pandas as pd import xgboost as xgb from sklearn.datasets import load_breast_cancer from sklear
  ```

### Literal Escape in Code Block in `week7.html` (Line 1307)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import pandas as pd import numpy as np import matplotlib.pyplot as plt import seaborn as sns from sklearn.pipeline impor
  ```

### Slop/Placeholder Content in `week7.html` (Line 1324)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  ded, TotalCharges cleaned (whitespace → NaN → median)    6+ EDA visualisations with
  ```

### Literal Escape in Code Block in `week7.html` (Line 1589)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import pandas as pd import numpy as np import shap import matplotlib.pyplot as plt from sklearn.pipeline import Pipeline
  ```

### Slop/Placeholder Content in `week8.html` (Line 2121)
- **Severity**: MEDIUM
- **Description**: Found placeholder/slop text 'NaN' (NaN literal in text (could indicate broken calculation or data representation)).
- **Context**:
  ```html
  ng loop loss stays high or converges to NaN because the weights updates behave erra
  ```

### Literal Escape in Code Block in `week9.html` (Line 610)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import numpy as np  def pool2d_forward(X, pool_size=2, stride=2, mode='max'):     # X shape: (H, W, C) - Height, Width,
  ```

### Literal Escape in Code Block in `week9.html` (Line 924)
- **Severity**: MEDIUM
- **Description**: Code block contains raw escape sequences ['\\n'] instead of actual characters.
- **Context**:
  ```html
  import tensorflow as tf from tensorflow.keras import layers, models import time import numpy as np  # 1. Construct modul
  ```


## [LOW] Severity Issues

### Unbalanced Math Delimiters in `roadmap.html` (Line 2606)
- **Severity**: LOW
- **Description**: Odd count of '$' (1) due to unescaped currency sign (e.g., 'p</td><td>$5 credit/month</td>'). In KaTeX pages, raw '$' can break rendering.
- **Context**:
  ```html
  p</td><td>$5 credit/month</td>
  ```

### Empty Math Equation in `week12.html` (Line 235)
- **Severity**: LOW
- **Description**: Found empty block math equation ($$ $$).
- **Context**:
  ```html
  $$
    $$
  ```

### Empty Math Equation in `week12.html` (Line 240)
- **Severity**: LOW
- **Description**: Found empty block math equation ($$ $$).
- **Context**:
  ```html
  $$
    $$
  ```

### Empty Math Equation in `week12.html` (Line 241)
- **Severity**: LOW
- **Description**: Found empty block math equation ($$ $$).
- **Context**:
  ```html
  $$
    $$
  ```

### Empty Math Equation in `week12.html` (Line 246)
- **Severity**: LOW
- **Description**: Found empty block math equation ($$ $$).
- **Context**:
  ```html
  $$
    $$
  ```

### Empty Math Equation in `week12.html` (Line 247)
- **Severity**: LOW
- **Description**: Found empty block math equation ($$ $$).
- **Context**:
  ```html
  $$
    $$
  ```

### Empty Math Equation in `week12.html` (Line 252)
- **Severity**: LOW
- **Description**: Found empty block math equation ($$ $$).
- **Context**:
  ```html
  $$
    $$
  ```

### Empty Math Equation in `week12.html` (Line 253)
- **Severity**: LOW
- **Description**: Found empty block math equation ($$ $$).
- **Context**:
  ```html
  $$
    $$
  ```

### Empty Math Equation in `week12.html` (Line 254)
- **Severity**: LOW
- **Description**: Found empty block math equation ($$ $$).
- **Context**:
  ```html
  $$
    $$
  ```

### Typo (Double Word) in `week14.html` (Line 1)
- **Severity**: LOW
- **Description**: Duplicated word 'for  for'.
- **Context**:
  ```html
  g Face  library, configure a LoRA setup for  for sequence classification. Target the  an
  ```

### Empty Math Equation in `week14.html` (Line 147)
- **Severity**: LOW
- **Description**: Found empty inline math equation ($ $).
- **Context**:
  ```html
  $ $
  ```

### Empty Math Equation in `week14.html` (Line 148)
- **Severity**: LOW
- **Description**: Found empty inline math equation ($ $).
- **Context**:
  ```html
  $ $
  ```

### Empty Math Equation in `week14.html` (Line 149)
- **Severity**: LOW
- **Description**: Found empty inline math equation ($ $).
- **Context**:
  ```html
  $ $
  ```

### Empty Math Equation in `week14.html` (Line 162)
- **Severity**: LOW
- **Description**: Found empty inline math equation ($ $).
- **Context**:
  ```html
  $ $
  ```

### Empty Math Equation in `week14.html` (Line 351)
- **Severity**: LOW
- **Description**: Found empty inline math equation ($ $).
- **Context**:
  ```html
  $ $
  ```

### Empty Math Equation in `week14.html` (Line 351)
- **Severity**: LOW
- **Description**: Found empty inline math equation ($ $).
- **Context**:
  ```html
  $ $
  ```

### Typo (Double Word) in `week3.html` (Line 1)
- **Severity**: LOW
- **Description**: Duplicated word 'to  to'.
- **Context**:
  ```html
  one Color of the marker boundaries. Set to  to remove borders.       python — scatter_
  ```

