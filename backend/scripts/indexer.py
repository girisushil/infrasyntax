# import json
# from pathlib import Path
# from elasticsearch import Elasticsearch
# from elasticsearch.helpers import bulk
# from sentence_transformers import SentenceTransformer
# import time
# import sys

# # --- 1. CONFIGURATION ---
# MODEL_NAME = 'all-mpnet-base-v2'
# INDEX_NAME = 'infrasyntax'
# ENRICHED_FILE = Path(__file__).parent.parent.parent / "data" / "processed_snippets" / "enriched_snippets.json"
# # Connects to the exposed Docker port on your Mac
# ELASTICSEARCH_URL = "http://127.0.0.1:9200" 

# # --- 2. DEFINE THE ELASTICSEARCH MAPPING ---
# INDEX_SETTINGS = {
#     "mappings": {
#         "properties": {
#             "description": {"type": "text"},
#             "code": {"type": "text"},
#             "technology": {"type": "keyword"},
#             "source_file": {"type": "keyword"},
#             "snippet_vector": {
#                 "type": "dense_vector",
#                 "dims": 768, 
#                 "index": "true",
#                 "similarity": "cosine"
#             }
#         }
#     }
# }

# def create_index(es):
#     """Creates the Elasticsearch index with our custom mapping."""
#     if es.indices.exists(index=INDEX_NAME):
#         print(f"Index '{INDEX_NAME}' already exists. Deleting...")
#         es.indices.delete(index=INDEX_NAME)
    
#     print(f"Creating new index '{INDEX_NAME}'...")
#     es.indices.create(index=INDEX_NAME, body=INDEX_SETTINGS)

# def get_documents(model):
#     """Generator function to read the JSON file, generate embeddings, and yield documents."""
#     print(f"Loading enriched snippets from {ENRICHED_FILE}...")
    
#     # --- Check for downloaded data file ---
#     if not ENRICHED_FILE.exists():
#         raise FileNotFoundError(
#             f"The final dataset was not found at {ENRICHED_FILE}. "
#             "Please ensure the file is downloaded from the remote server."
#         )

#     with open(ENRICHED_FILE, 'r', encoding='utf-8') as f:
#         snippets = json.load(f)

#     total = len(snippets)
#     print(f"Found {total} snippets to index.")
    
#     # Generate vectors in bulk (the neural network step)
#     all_descriptions = [s.get('description', '') for s in snippets]
#     print(f"Generating {len(all_descriptions)} embeddings with model '{MODEL_NAME}'...")
    
#     # This is the heavy NLP part
#     vectors = model.encode(all_descriptions, show_progress_bar=True, batch_size=128, convert_to_numpy=True)
    
#     print("Embedding generation complete.")

#     for i, snippet in enumerate(snippets):
#         yield {
#             "_index": INDEX_NAME,
#             "_id": snippet['id'],
#             "_source": {
#                 "description": snippet['description'],
#                 "code": snippet['code'],
#                 "technology": snippet['technology'],
#                 "source_file": snippet['source_file'],
#                 "snippet_vector": vectors[i].tolist()
#             }
#         }

# def main():
#     # --- INFINITE RETRY LOOP for Indexer Connection ---
#     es_client = None
#     while True:
#         try:
#             print(f"Connecting to Elasticsearch ({ELASTICSEARCH_URL})...")
#             # Connect using the robust host address
#             es_client = Elasticsearch(
#                 [ELASTICSEARCH_URL],
#                 verify_certs=False,
#                 ssl_show_warn=False
#             )
#             # Ping the service to confirm it's ready
#             if es_client.ping():
#                 print("--- Elasticsearch connection successful! Indexing starting. ---")
#                 break
#             else:
#                 print("Ping failed. Retrying in 10 seconds...")
#                 time.sleep(10)
#         except Exception as e:
#             # Catches network and connection exceptions
#             print(f"Connection failed: {e}. Retrying in 10 seconds...")
#             time.sleep(10)
    
#     es = es_client # Assign the client
    
#     # Proceed with indexing
#     create_index(es)
    
#     print("Loading neural network model...")
#     model = SentenceTransformer(MODEL_NAME)
    
#     print("Starting bulk indexing...")
#     start_time = time.time()
    
#     success, errors = bulk(
#         es,
#         get_documents(model),
#         chunk_size=500,
#         request_timeout=60
#     )
    
#     end_time = time.time()
    
#     print(f"\n--- Indexing Complete ---")
#     print(f"Successfully indexed {success} documents.")
#     print(f"Failed to index {len(errors)} documents.")
#     print(f"Total time: {end_time - start_time:.2f} seconds.")

# if __name__ == "__main__":
#     main()
# import json
# import os
# from pathlib import Path
# from elasticsearch import Elasticsearch, helpers
# from sentence_transformers import SentenceTransformer
# import time
# import sys

# # --- CONFIGURATION ---
# MODEL_NAME = 'all-mpnet-base-v2'
# INDEX_NAME = 'infrasyntax'
# ENRICHED_FILE = Path(__file__).parent.parent.parent / "data" / "processed_snippets" / "enriched_snippets.json"
# ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")

# INDEX_SETTINGS = {
#     "mappings": {
#         "properties": {
#             "description": {"type": "text"},
#             "code": {"type": "text"},
#             "technology": {"type": "keyword"},
#             "source_file": {"type": "keyword"},
#             "snippet_vector": {
#                 "type": "dense_vector",
#                 "dims": 768,
#                 "index": True,
#                 "similarity": "cosine"
#             }
#         }
#     }
# }

# def create_index(es):
#     if es.indices.exists(index=INDEX_NAME):
#         print(f"Index '{INDEX_NAME}' exists. Deleting...")
#         es.indices.delete(index=INDEX_NAME)
#     print(f"Creating new index '{INDEX_NAME}'...")
#     es.indices.create(index=INDEX_NAME, body=INDEX_SETTINGS)

# def get_documents(model):
#     if not ENRICHED_FILE.exists():
#         raise FileNotFoundError(f"❌ Missing data file: {ENRICHED_FILE}")

#     with open(ENRICHED_FILE, 'r', encoding='utf-8') as f:
#         snippets = json.load(f)

#     all_desc = [s.get('description', '') for s in snippets]
#     print(f"Generating embeddings for {len(all_desc)} snippets...")
#     vectors = model.encode(all_desc, show_progress_bar=True, batch_size=128, convert_to_numpy=True)

#     for i, snippet in enumerate(snippets):
#         yield {
#             "_index": INDEX_NAME,
#             "_id": snippet['id'],
#             "_source": {
#                 "description": snippet['description'],
#                 "code": snippet['code'],
#                 "technology": snippet['technology'],
#                 "source_file": snippet['source_file'],
#                 "snippet_vector": vectors[i].tolist()
#             }
#         }

# def main():
#     print(f"Connecting to Elasticsearch at {ELASTICSEARCH_URL}...")
#     es = Elasticsearch([ELASTICSEARCH_URL], verify_certs=False, ssl_show_warn=False)
#     if not es.ping():
#         raise RuntimeError(f"❌ Cannot connect to Elasticsearch at {ELASTICSEARCH_URL}")
#     print("✅ Connected successfully!")

#     create_index(es)

#     print("Loading Sentence-Transformer model...")
#     model = SentenceTransformer(MODEL_NAME)

#     print("Indexing data...")
#     start = time.time()
#     success, errors = helpers.bulk(es, get_documents(model), chunk_size=500, request_timeout=120)
#     print(f"✅ Indexed {success} docs, {len(errors)} errors, took {time.time() - start:.2f}s")

# if __name__ == "__main__":
#     main()


import json
import os
from pathlib import Path
from elasticsearch import Elasticsearch, helpers
from sentence_transformers import SentenceTransformer
import time
import sys
import torch

# --- CONFIGURATION ---
MODEL_NAME = 'all-mpnet-base-v2'
INDEX_NAME = 'infrasyntax'
ENRICHED_FILE = Path(__file__).parent.parent.parent / "data" / "processed_snippets" / "enriched_snippets.json"
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")

# Processing batch size (higher = faster but more RAM). 
# 128
BATCH_SIZE = 128 

INDEX_SETTINGS = {
    "mappings": {
        "properties": {
            "description": {"type": "text"},
            "code": {"type": "text"},
            "technology": {"type": "keyword"},
            "source_file": {"type": "keyword"},
            "snippet_vector": {
                "type": "dense_vector",
                "dims": 768,
                "index": True,
                "similarity": "cosine"
            }
        }
    }
}

def get_device():
    """
    Auto-detects the best available device.
    Prioritizes MPS (Mac GPU) -> CUDA (Nvidia GPU) -> CPU.
    """
    if torch.backends.mps.is_available():
        print("🚀 Using macOS GPU (MPS) acceleration!")
        return "mps"
    elif torch.cuda.is_available():
        print("🚀 Using NVIDIA GPU (CUDA) acceleration!")
        return "cuda"
    else:
        print("⚠️  No GPU detected. Using CPU (slower).")
        return "cpu"

def create_index(es):
    if es.indices.exists(index=INDEX_NAME):
        print(f"Index '{INDEX_NAME}' exists. Deleting...")
        es.indices.delete(index=INDEX_NAME)
    print(f"Creating new index '{INDEX_NAME}'...")
    es.indices.create(index=INDEX_NAME, body=INDEX_SETTINGS)

def generate_actions(model, snippets):
    """
    Generator that yields Elasticsearch documents in batches.
    This prevents loading all embeddings into memory at once.
    """
    total_snippets = len(snippets)
    print(f"Processing {total_snippets} snippets in batches of {BATCH_SIZE}...")

    # Iterate through the list in chunks
    for i in range(0, total_snippets, BATCH_SIZE):
        batch_snippets = snippets[i : i + BATCH_SIZE]
        
        # Extract text for just this batch
        batch_descriptions = [s.get('description', '') for s in batch_snippets]
        
        # Generate embeddings for ONLY this batch
        # convert_to_numpy=True moves data efficiently back to CPU for ES transmission
        embeddings = model.encode(
            batch_descriptions, 
            batch_size=BATCH_SIZE, 
            show_progress_bar=False, 
            convert_to_numpy=True
        )

        # Yield docs for this batch
        for j, snippet in enumerate(batch_snippets):
            yield {
                "_index": INDEX_NAME,
                "_id": snippet['id'],
                "_source": {
                    "description": snippet['description'],
                    "code": snippet['code'],
                    "technology": snippet['technology'],
                    "source_file": snippet['source_file'],
                    "snippet_vector": embeddings[j].tolist()
                }
            }
        
        # Optional: Print progress every 10 batches to avoid console spam
        if (i // BATCH_SIZE) % 10 == 0:
            print(f"   Processed {min(i + BATCH_SIZE, total_snippets)}/{total_snippets}...")

def main():
    print(f"Connecting to Elasticsearch at {ELASTICSEARCH_URL}...")
    es = Elasticsearch([ELASTICSEARCH_URL], verify_certs=False, ssl_show_warn=False)
    if not es.ping():
        raise RuntimeError(f"❌ Cannot connect to Elasticsearch at {ELASTICSEARCH_URL}")
    print("✅ Connected successfully!")

    create_index(es)

    print("Loading Sentence-Transformer model...")
    device = get_device()
    # Load model onto the specific device (GPU)
    model = SentenceTransformer(MODEL_NAME, device=device)

    if not ENRICHED_FILE.exists():
        raise FileNotFoundError(f"❌ Missing data file: {ENRICHED_FILE}")

    print("Loading data file...")
    with open(ENRICHED_FILE, 'r', encoding='utf-8') as f:
        snippets = json.load(f)

    print("Indexing data...")
    start = time.time()
    
    # helpers.bulk consumes the generator, streaming data to ES
    success, errors = helpers.bulk(
        es, 
        generate_actions(model, snippets), 
        chunk_size=500, 
        request_timeout=120
    )
    
    print(f"✅ Indexed {success} docs, {len(errors)} errors")
    print(f"⏱️  Total time: {time.time() - start:.2f}s")

if __name__ == "__main__":
    main()