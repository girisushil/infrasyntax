# InfraSyntax: A Goal-Oriented Search Engine for Configuration Files

**InfraSyntax** is a specialized Information Retrieval (IR) system designed to bridge the gap between high-level natural language intent and machine-readable configuration code. 

Developers often struggle with the "syntax gap"—knowing *what* they want to achieve (e.g., "set up a secure SSL redirect") but lacking the precise, error-prone syntax for tools like Kubernetes, Docker, or Nginx. InfraSyntax indexes production-grade snippets from real-world projects to provide functional, copy-pasteable solutions based on natural language objectives.

---

## 🚀 System Overview
* **Natural Language Querying:** Move beyond keyword matching to intent-based search.
* **Semantic Enrichment:** Every snippet is context-aware, enriched by local LLM (Phi-3 Mini) descriptions.
* **Dependency-RAG:** A Knowledge Graph backend that identifies supporting snippets (e.g., finding the matching Service for a retrieved K8s Deployment).
* **Multi-Format Extraction:** Custom parsers for Dockerfiles, Kubernetes manifests, YAML configurations, and GitHub Actions.

---

## 🛠 Engineering & Implementation

### 1. Data Acquisition at Scale
We scraped **1,970 high-quality repositories** from GitHub, prioritizing organizational repos with high star/fork counts.
* **Raw Data:** ~90 GB of repository content.
* **Refinement:** Implemented **ANTLR-based parsers** to move beyond RegEx. This allowed us to structure and isolate **250,000+ individual code snippets** across various DevOps formats.

### 2. The Ingestion Pipeline (Pitt CRC)
To generate high-quality search metadata, we ran a large-scale ingestion pipeline on the **Pitt Center for Research Computing (CRC)**:
* **Inference:** Used a local **Phi-3 Mini** model to generate natural language descriptions for all 250k snippets.
* **Contextualization:** These descriptions allow the engine to map a user's goal (e.g., "rate limiting") to specific blocks of code that may not contain that exact keyword.

### 3. Retrieval & Re-ranking Architecture
To ensure high precision, we implemented a hybrid retrieval pipeline:
* **Stage 1 (Retrieval):** A Bi-Encoder model performs a fast semantic search over the vector space.
* **Stage 2 (Re-ranking):** A Cross-Encoder evaluates the top-k candidates for deeper contextual relevance.
* **Fusion:** Utilized **Reciprocal Rank Fusion (RRF)** to combine scores and deliver the most accurate snippets at the top of the results.



---

## 📊 Visualizations & Performance

### Search Latency Analysis
We benchmarked the query response time comparison between our baseline Bi-Encoder and the improved Hybrid Pipeline. While the Cross-Encoder adds a re-ranking step, the trade-off significantly improves the quality of the top-ranked results.

### Knowledge Graph (Dependency-RAG)
Using **NetworkX**, we mapped the relationships between configuration files:
* **Nodes:** 250,000+ snippets.
* **Edges:** 12,918 dependency links.
This graph allows the system to recommend "supporting" snippets. If a user selects a configuration for a web server, the system can automatically surface the required environment variables or sidecar configs.



---

## 🧪 Tech Stack
* **Language:** Python
* **Data Parsing:** ANTLR4 (Grammar-based extraction)
* **Search & IR:** Sentence-Transformers (Bi-Encoders/Cross-Encoders), RRF
* **Compute:** Pitt CRC Cluster (HPC)
* **LLM:** Phi-3 Mini (Local Ingestion)
* **Graph Theory:** NetworkX
* **Data Source:** GitHub API (DevOps-focused crawl)

---

## 🏁 Impact
InfraSyntax transforms static configuration documentation into a dynamic, goal-oriented experience. By indexing 250k+ production snippets with LLM-generated context, it significantly reduces the "search-to-deployment" time for DevOps engineers and system administrators.
