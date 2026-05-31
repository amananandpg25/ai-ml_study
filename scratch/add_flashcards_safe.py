import os
import re

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"

flashcards_data = {
    101: [
        ("What is the main difference between zero-shot and few-shot prompting?", "Zero-shot prompting relies on the model's pre-trained knowledge without examples, while few-shot prompting provides one or more input-output demonstrations to guide the model."),
        ("What is Chain of Thought (CoT) prompting?", "A prompting method that encourages the LLM to output its step-by-step reasoning process before arriving at the final answer, improving performance on logical tasks."),
        ("Why is temperature important in LLM generation?", "It controls generation randomness: lower values (close to 0) produce deterministic, logical output, while higher values (above 0.7) increase creativity and variety."),
        ("What is a System Prompt?", "An instruction set that defines the role, tone, constraints, and behavior rules for the LLM, isolated from user inputs.")
    ],
    102: [
        ("What is the purpose of rate limits in LLM APIs?", "To prevent service abuse, ensure fair resource sharing, and manage server capacity (measured in Requests Per Minute [RPM] or Tokens Per Minute [TPM])."),
        ("What are function calling capabilities in modern LLM APIs?", "The ability of the model to output structured JSON representing arguments to call specific programming functions, allowing LLMs to interact with external tools."),
        ("Why should you use streaming in LLM applications?", "It reduces perceived latency for the user by displaying tokens as they are generated, rather than waiting for the entire response to complete."),
        ("What is semantic text chunking?", "Dividing a large text document into logical chunks based on content meaning or sentence boundaries rather than rigid character lengths, ensuring context is preserved.")
    ],
    103: [
        ("What does LCEL stand for in LangChain?", "LangChain Expression Language, a declarative way to easily chain LangChain components together with built-in support for streaming, batching, and async operations."),
        ("What is a Runnable in LangChain?", "A standard interface implemented by LangChain components (like models, prompts, and output parsers) to allow chaining using the | operator."),
        ("What is the role of an Output Parser in LangChain?", "To parse the raw text output of an LLM into structured formats like Python dictionaries, lists, or Pydantic models."),
        ("What is the difference between a Chain and an Agent in LangChain?", "A Chain executes a fixed sequence of hard-coded steps, while an Agent uses an LLM dynamically to decide which actions/tools to take in what order.")
    ],
    104: [
        ("What is a Vector Database?", "A specialized database designed to store, index, and query high-dimensional vector embeddings efficiently, enabling fast semantic search."),
        ("What is Cosine Similarity?", "A similarity metric that measures the cosine of the angle between two vectors, indicating directional alignment regardless of vector magnitude."),
        ("What is HNSW?", "Hierarchical Navigable Small World, a state-of-the-art graph-based algorithm for approximate nearest neighbor (ANN) search in vector databases."),
        ("Why is a metadata filter useful in vector databases?", "It allows pre-filtering or post-filtering search queries based on non-vector attributes (e.g., date, category, owner) to narrow down results.")
    ],
    105: [
        ("What is the difference between Dense and Sparse Retrieval?", "Dense retrieval uses embedding vectors to search by semantic meaning, while sparse retrieval (like BM25) uses keyword matching and term frequency."),
        ("What is a Reranker in advanced RAG?", "A secondary model that evaluates the relevance of retrieved documents to the query and re-orders them, improving retrieval precision before feeding them to the LLM."),
        ("What is query expansion/rewriting?", "An optimization that uses an LLM to generate multiple variations or clarify a user's query to improve the chances of retrieving relevant documents."),
        ("What is the 'Lost in the Middle' phenomenon?", "The tendency of LLMs to ignore or fail to process information located in the middle of long input contexts, prioritizing the beginning and end.")
    ],
    106: [
        ("What is the ReAct agent framework?", "A framework that combines Reasoning (thinking steps) and Acting (calling tools) to solve complex tasks using an LLM."),
        ("What is a Tool in the context of LLM agents?", "A wrapper around a programming function (like a calculator, web search, or database query) that the agent can choose to run by outputting structured arguments."),
        ("What is an agent's loop limit?", "A safety constraint that limits the maximum number of reasoning-action iterations an agent can run to prevent infinite loops and runaway API costs."),
        ("How do agents maintain conversation state?", "By appending previous messages, actions, and observations to the LLM's conversation history window on each turn.")
    ],
    107: [
        ("What is an agentic workflow?", "A system design where LLMs are wrapped in iterative loops and conditional branches to act as decision-makers, rather than simple single-turn text generators."),
        ("Why is debugging agentic systems difficult?", "Because the execution path is non-deterministic and depends on intermediate LLM outputs, making tracing and logging tools essential."),
        ("What is the benefit of a multi-agent system over a single agent?", "Dividing a complex task among specialized agents (e.g., researcher, writer, editor) reduces prompt complexity and improves reliability."),
        ("What is human-in-the-loop (HITL) inside agentic systems?", "A checkpoint where the agent pauses and waits for user approval or feedback before executing a critical tool (like sending an email or running a transaction).")
    ],
    108: [
        ("What is Fine-Tuning?", "The process of continuing training a pre-trained model on a task-specific dataset to adapt its behavior, style, or knowledge."),
        ("What is LoRA?", "Low-Rank Adaptation, a parameter-efficient fine-tuning (PEFT) method that freezes the pre-trained weights and adds small trainable rank decomposition matrices to layers."),
        ("What is QLoRA?", "An extension of LoRA that quantizes the base model weights to 4-bit precision (NormalFloat4) and uses double quantization, massively reducing fine-tuning VRAM requirements."),
        ("What is the difference between pre-training and fine-tuning?", "Pre-training trains a model from scratch on raw text to learn language representation, while fine-tuning adapts that model to a specific task using supervised data.")
    ],
    109: [
        ("What is LLMOps?", "The set of practices, workflows, and tools used to deploy, monitor, evaluate, and maintain large language models in production systems."),
        ("What is tracing in LLMOps?", "Logging the step-by-step inputs, outputs, and intermediate states of complex LLM chains and agent runs to debug execution."),
        ("What are LLM Guardrails?", "Input/output validation layers that check queries and responses for safety, bias, hallucination, or private data before releasing them."),
        ("Why is traditional software monitoring insufficient for LLMs?", "Because LLM outputs are unstructured, non-deterministic, and subjective, requiring semantic drift and relevance evaluation rather than simple error status checks.")
    ],
    110: [
        ("What is LangGraph?", "A LangChain library designed to build stateful, multi-agent systems with cyclic execution flows, modeling agents as graphs."),
        ("What is AutoGen?", "A framework by Microsoft for building multi-agent conversational systems where agents can chat with each other to solve tasks."),
        ("What is the benefit of cyclic graphs in agent design?", "They allow the agent to iterate, correct errors, and self-reflect by returning to previous states based on tool feedback."),
        ("What is State in stateful multi-agent systems?", "A shared memory object updated by agents during the execution flow, containing parameters, variables, and conversation history.")
    ],
    111: [
        ("What is Model Context Protocol (MCP)?", "A universal, open standard that allows developers to write secure, reusable connectors that expose data sources and tools to LLMs."),
        ("Why is MCP useful?", "It replaces ad-hoc API integrations with a standard protocol, letting any MCP-compliant client connect to any MCP-compliant server."),
        ("What are the three core features exposed by MCP servers?", "Prompts (reusable templates), Resources (read-only data sources), and Tools (executable actions)."),
        ("How does MCP improve LLM safety?", "It runs tools and parses data within a defined schema, isolating the host application from arbitrary execution.")
    ],
    112: [
        ("What is FastAPI?", "A modern, high-performance web framework for building APIs with Python, based on standard Python type hints and ASGI."),
        ("Why is Docker used in production AI applications?", "It packages the application code, Python interpreter, system packages, and exact model libraries into a single container, guaranteeing identical execution in staging and production."),
        ("What is the difference between WSGI and ASGI?", "WSGI is synchronous and designed for standard web apps, while ASGI is asynchronous and supports concurrent connections like websockets and streaming."),
        ("Why should you avoid loading large models inside FastAPI endpoints?", "It causes massive memory bottlenecks and slow response times; models should be loaded once globally at startup or served via a dedicated model server.")
    ],
    113: [
        ("What is Server-Sent Events (SSE)?", "A standard protocol that allows a server to push real-time, unidirectional text updates (like tokens from an LLM) to a web client over HTTP."),
        ("How does streaming improve user experience?", "It decreases time-to-first-token (TTFT), making the application feel instantaneous even if the full generation takes several seconds."),
        ("What is the difference between streaming with WebSockets vs SSE?", "WebSockets support bidirectional, full-duplex communication (ideal for chat apps), while SSE is lightweight, runs over HTTP, and supports server-to-client streaming."),
        ("How do you parse streaming outputs on the client side?", "By reading the response stream chunk-by-chunk and dynamically updating the UI state with each incoming text fragment.")
    ],
    114: [
        ("What is Next.js?", "A popular React framework for production web development, supporting server-side rendering (SSR), static site generation, and API routes."),
        ("What is the Vercel AI SDK?", "A library designed to help frontend developers build streaming AI interfaces using React, Next.js, and popular LLM backends."),
        ("What is server-side rendering (SSR)?", "Generating the HTML of a webpage on the server for each request before sending it to the client, improving SEO and initial load times."),
        ("Why is Vercel AI SDK's useChat hook useful?", "It abstracts the complexity of managing chat input, loading states, server request streams, and updating message threads into a single hook.")
    ],
    115: [
        ("What is LangSmith?", "A platform by LangChain for debugging, testing, evaluating, and monitoring LLM applications and agent chains."),
        ("What is Arize Phoenix?", "An open-source AI observability platform used to visualize LLM traces, evaluate RAG pipelines, and analyze embedding distributions."),
        ("What is the difference between logging and tracing?", "Logging records isolated events with error/info tags, while tracing follows the entire nested execution path of queries across functions and APIs."),
        ("What is Semantic Drift?", "A change in the semantic distribution of user queries or model outputs over time, indicating changes in usage patterns or model performance.")
    ],
    116: [
        ("What is RAGAS?", "An evaluation framework that provides metrics for assessing Retrieval Augmented Generation (RAG) pipelines without ground truth data."),
        ("What is faithfulness in RAG evaluation?", "A metric that measures whether the LLM's generated response is grounded strictly in the retrieved context documents, indicating a lack of hallucination."),
        ("What is answer relevance in RAG evaluation?", "A metric that measures how directly the generated response addresses the user's initial query."),
        ("What is TruLens?", "A feedback loop framework by Arize that evaluates LLM application quality using metrics like context relevance, groundedness, and answer relevance.")
    ],
    117: [
        ("What is a production RAG pipeline?", "An end-to-end RAG system optimized for low latency, high document throughput, query preprocessing, secure access controls, and active telemetry monitoring."),
        ("Why is document indexing partition important?", "It allows isolating document retrieval by user or department, preventing unauthorized data access."),
        ("How does query preprocessing (like classification) improve RAG?", "It routes the query to different specialized indexes or bypasses RAG entirely if the query is a simple greeting."),
        ("What is hot-loading a vector index?", "Keeping the vector index in-memory (e.g., using FAISS or index caching) to ensure sub-millisecond similarity search.")
    ],
    118: [
        ("What is Flask?", "A lightweight, micro WSGI web application framework in Python designed to be simple, extensible, and easy to deploy."),
        ("What is a Blueprint in Flask?", "A way to organize a group of related views, templates, and static files to modularize large Flask applications."),
        ("What is a Route in Flask?", "A URL pattern mapped to a specific Python function (view function) that executes when that URL is accessed."),
        ("What is the difference between Flask and Django?", "Flask is a micro-framework (no built-in database, authentication, or admin panel), while Django is a batteries-included framework with everything pre-configured.")
    ],
    119: [
        ("What is a REST API?", "An architectural style for designing networked applications using HTTP requests to GET, POST, PUT, or DELETE resources."),
        ("What is HTTP Status Code 201?", "Created, indicating that the request succeeded and a new resource was successfully created on the server."),
        ("What is the importance of API versioning?", "It allows developers to release breaking changes to endpoints without breaking existing client integrations (e.g., /api/v1/ vs /api/v2/)."),
        ("Why is JSON the standard data format for REST APIs?", "Because it is lightweight, human-readable, and supported natively by JavaScript and almost all backend programming languages.")
    ],
    120: [
        ("How do you serve a serialized model in Python?", "By saving the trained model object using pickle or joblib, and loading it into memory on Flask application startup to predict on incoming request payloads."),
        ("What is Gunicorn?", "A Python WSGI HTTP Server for UNIX, used to run Flask/Django apps in production by handling concurrent requests using multiple worker processes."),
        ("Why shouldn't you run a Flask app in production using app.run()?", "Because the built-in development server is single-threaded, not secure, and does not handle high loads or concurrent connections."),
        ("How does batching inference improve production performance?", "It aggregates individual incoming requests into a single batch, allowing the model to make predictions simultaneously and reducing overhead.")
    ],
    121: [
        ("What is a Docker Image?", "A read-only, executable template containing instructions to build a Docker container, structured in layers."),
        ("What is a Docker Container?", "A runnable, isolated instance of a Docker Image that executes in sandboxed user-space on the host kernel."),
        ("What is the role of a Docker Registry?", "A storage and distribution system for Docker Images (like Docker Hub or AWS ECR), allowing sharing across teams and deployment environments."),
        ("What is the difference between a virtual machine (VM) and a Docker container?", "A VM includes a full guest OS and hypervisor (virtualized hardware), while a Docker container shares the host OS kernel and runs as isolated processes.")
    ],
    122: [
        ("What is a Dockerfile?", "A text file containing a list of CLI instructions that Docker uses to build a container image."),
        ("What is a Multi-Stage Build in Docker?", "A technique that uses multiple FROM statements in a Dockerfile, allowing you to build assets in temporary stages and copy only the final binaries to the production image, minimizing container size."),
        ("Why should you put pip install before copying your code in a Dockerfile?", "To leverage Docker's build cache; if your code changes but dependencies do not, Docker will skip reinstalling dependencies."),
        ("What is the USER instruction in a Dockerfile?", "An instruction that sets the non-root username or UID to run the container, improving security.")
    ],
    123: [
        ("What is Docker Compose?", "A tool for defining and running multi-container Docker applications, configured using a docker-compose.yml file."),
        ("Why is Docker Compose useful for ML stacks?", "It lets you launch the web app, vector database, and cache database (e.g., Redis) simultaneously with single-command orchestration and pre-defined network routing."),
        ("What is a Volume in Docker Compose?", "A mechanism to persist data generated and used by Docker containers, mapping container directories to host machine directories."),
        ("How do containers communicate with each other in Docker Compose?", "Through a shared bridge network, allowing containers to resolve each other by service name (e.g., http://vector-db:8000).")
    ],
    124: [
        ("What is CI/CD in production machine learning?", "Continuous Integration (automated testing and build checks) and Continuous Deployment (automatic shipping of verified code and models to servers)."),
        ("What is blue-green deployment?", "A release strategy that runs two identical production environments; only one serves traffic, allowing zero-downtime updates and instant rollbacks."),
        ("How do you verify model predictions in a deployment pipeline?", "By running integration tests that send test payloads and assert that predictions fall within acceptable metric ranges."),
        ("Why is health check endpoint monitoring important?", "It allows load balancers to detect if a model server has crashed or run out of memory, automatically restarting or rerouting traffic.")
    ]
}

def check_depth(content_str):
    c_clean = re.sub(r'<script.*?>.*?</script>|<style.*?>.*?</style>', '', content_str, flags=re.DOTALL)
    tags = re.findall(r'</?div\b[^>]*>', c_clean)
    depth = sum(1 if not t.startswith('</') else -1 for t in tags)
    return depth

def inject_flashcards_for_week(w, days):
    path = os.path.join(base_dir, f"week{w}.html")
    if not os.path.exists(path):
        print(f"File week{w}.html not found!")
        return
        
    print(f"Processing week{w}.html...")
    content = open(path, 'r', encoding='utf-8').read()
    
    initial_depth = check_depth(content)
    if initial_depth != 0:
        print(f"  ERROR: Initial div depth of week{w}.html is not 0 (it is {initial_depth})!")
        return

    for d in days:
        day_marker = f'id="day-{d}"'
        if day_marker not in content:
            day_marker = f"id='day-{d}'"
            if day_marker not in content:
                print(f"  Day {d} marker not found!")
                continue
                
        day_start_idx = content.find(day_marker)
        
        next_day_marker = f'id="day-{d+1}"'
        next_day_marker_alt = f"id='day-{d+1}'"
        
        next_day_pos = content.find(next_day_marker, day_start_idx)
        if next_day_pos == -1:
            next_day_pos = content.find(next_day_marker_alt, day_start_idx)
            
        if next_day_pos != -1:
            day_end_idx = next_day_pos
        else:
            day_end_idx = content.find("</main>", day_start_idx)
            if day_end_idx == -1:
                day_end_idx = len(content)
                
        day_content = content[day_start_idx:day_end_idx]
        
        if "Revision Flashcards" in day_content:
            print(f"  Day {d} already has flashcards, skipping.")
            continue
            
        # Locate takeaways block within this day
        takeaways_str = 'class="takeaways"'
        takeaways_pos = day_content.find(takeaways_str)
        if takeaways_pos == -1:
            takeaways_str = 'class="takeaway"'
            takeaways_pos = day_content.find(takeaways_str)
        if takeaways_pos == -1:
            takeaways_str = 'class="day-takeaways"'
            takeaways_pos = day_content.find(takeaways_str)
            
        if takeaways_pos == -1:
            print(f"  WARNING: Could not find takeaways block for Day {d}!")
            # Fallback
            complete_btn_str = 'class="complete-btn"'
            complete_btn_pos = day_content.find(complete_btn_str)
            if complete_btn_pos != -1:
                insert_pos_in_day = day_content.rfind('<div', 0, complete_btn_pos)
                if insert_pos_in_day == -1:
                    insert_pos_in_day = complete_btn_pos
            else:
                insert_pos_in_day = day_content.rfind('</div>')
        else:
            insert_pos_in_day = day_content.rfind('<div', 0, takeaways_pos)
            if insert_pos_in_day == -1:
                insert_pos_in_day = takeaways_pos
                
        cards = flashcards_data[d]
        cards_html = f"""
  <h2 class="sh2">🃏 Revision Flashcards — Day {d}</h2>
  <p class="flashcard-hint" style="font-size:10px; font-family:var(--font-mono); color:var(--muted); text-transform:uppercase; margin-bottom:8px;">CLICK EACH CARD TO FLIP ↓</p>
  <div class="flashcard-grid">
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[0][0]}</div>
        <div class="fc-back">{cards[0][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[1][0]}</div>
        <div class="fc-back">{cards[1][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[2][0]}</div>
        <div class="fc-back">{cards[2][1]}</div>
      </div>
    </div>
    <div class="flashcard" onclick="this.classList.toggle('flipped')" role="button" tabindex="0">
      <div class="fc-inner">
        <div class="fc-front">{cards[3][0]}</div>
        <div class="fc-back">{cards[3][1]}</div>
      </div>
    </div>
  </div>
"""
        modified_day_content = day_content[:insert_pos_in_day] + cards_html + "\n" + day_content[insert_pos_in_day:]
        
        # Test content integration
        test_content = content[:day_start_idx] + modified_day_content + content[day_end_idx:]
        test_depth = check_depth(test_content)
        if test_depth != 0:
            print(f"  CRITICAL ERROR: Injecting flashcards into Day {d} results in unbalanced HTML (depth = {test_depth})!")
            print(f"  Aborting injection for Day {d}!")
            continue
            
        content = test_content
        print(f"  Day {d}: Flashcards successfully injected!")
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Saved changes to week{w}.html. Final balance verified: {check_depth(content)}")

inject_flashcards_for_week(15, [101, 102, 103, 104, 105, 106, 107])
inject_flashcards_for_week(16, [108, 109, 110, 111, 112, 113, 114, 115, 116, 117])
inject_flashcards_for_week(17, [118, 119, 120, 121, 122, 123, 124])

print("Finished!")
