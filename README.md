# InfraSyntax: Intelligent NLP Search Engine for Configuration Files

InfraSyntax is a fully containerized, production-ready semantic search engine. It allows developers to find relevant configuration snippets by searching with natural language goals (e.g., "set up a secure SSL redirect") instead of guessing exact keywords.

This implementation has been upgraded with production-level features, including robust error handling, centralized configuration, structured logging, and performance optimizations.

---

## System Architecture

The project follows a standard data pipeline architecture, ensuring a clear separation of concerns.

+----------------+      +---------------------+      +-----------------+
|                |      |                     |      |                 |
|  GitHub        +------>  1. Scraper         +------>  Scraped Files  |
|  (Raw Data)    |      |  (Python/PyGithub)  |      |  (Raw Text +     |
|                |      |                     |      |  Metadata)      |
+----------------+      +---------------------+      +-------+---------+
|
|
+----------------+      +---------------------+      +-------+---------+
|                |      |                     |      |                 |
|  Frontend      +<----->  4. Backend API     +<----->  3. Elasticsearch|
|  (React)       |      |  (FastAPI)          |      |  (Indexed Data) |
|                |      |                     |      |                 |
+----------------+      +---------+-----------+      +-----------------+
^
|
+-----------+-----------+
|                       |
|  2. Parser & Indexer  |
|  (Python/S-BERT)      |
|                       |
+-----------------------+


1.  **Scraper:** Acquires raw configuration files and their metadata (like repository stars) from GitHub. It is **resumable** and handles API rate limits gracefully.
2.  **Parser & Indexer:** Processes raw files. It segments them into logical chunks, generates semantic vector embeddings, and indexes this structured data into Elasticsearch using an **efficient bulk-ingestion** process.
3.  **Elasticsearch:** Serves as the high-performance search index, supporting **Reciprocal Rank Fusion (RRF)** to intelligently combine keyword and semantic search results.
4.  **Backend API & Frontend:** A **FastAPI** backend, configured via environment variables, exposes a search endpoint. A **React** frontend provides the user interface.

---

## Production-Ready Features

* **Centralized Configuration:** All settings are managed in a `.env` file, validated by Pydantic in the backend for robustness.
* **Structured Logging:** All modules write to a central log file (`infrasyntax.log`) with clear, filterable log levels (`INFO`, `WARNING`, `ERROR`).
* **Resumable & Robust Scripts:** The scraper and indexer can be stopped and restarted without losing progress, skipping already processed files.
* **State-of-the-Art Ranking:** Uses **Reciprocal Rank Fusion (RRF)** to combine keyword and semantic search scores, providing more balanced and relevant results than simple boosting.
* **Efficient & Scalable:** Uses batch processing for generating embeddings and bulk APIs for indexing, making it capable of handling hundreds of thousands of documents.
* **Containerized & Reproducible:** The entire application stack is managed with Docker Compose for a one-command setup.

---

## Getting Started

### 1. Initial Setup

- **Install Docker:** Get it from the [official website](https://www.docker.com/products/docker-desktop/).
- **Clone the repository.**

### 2. Configuration

- **Create your `.env` file:**
  ```bash
  cp .env.example .env
Edit the .env file:

Open the new .env file and add your GITHUB_TOKEN. You can get one here (select the public_repo scope).

3. Running the Full Pipeline
Execute these steps from your terminal in the project's root directory.

Run the Scraper (Phase 1):
This downloads config files into scraped_data/. It's resumable.

Bash

# Install Python dependencies locally
pip install -r scraper/requirements.txt
python scraper/run_scraper.py
Run the Parser & Indexer (Phase 2):
This processes the raw files and loads them into Elasticsearch. It's also resumable.

Bash

# Start Elasticsearch in the background
docker-compose up -d elasticsearch

# Wait for ~30 seconds for Elasticsearch to be ready
echo "Waiting for Elasticsearch to start..."
sleep 30

# Install Python dependencies locally
pip install -r parser/requirements.txt
python parser/run_parser.py
Run the Full Application (Phase 3 & 4):
This starts the backend API and the frontend UI.

Bash

docker-compose up --build -d backend frontend
4. Access the Services
Frontend UI: http://localhost:3000

Backend API Docs: http://localhost:8000/docs
