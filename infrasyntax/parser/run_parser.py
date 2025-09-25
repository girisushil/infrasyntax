import os
import json
import logging
from tqdm import tqdm
from segmenter import segment_file
from indexer import ESIndexer
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

Setup centralized logger
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(file), '..')))
from shared.logger import setup_logger
logger = setup_logger()

load_dotenv()
RAW_FILES_DIR = "scraped_data"
METADATA_FILE = os.path.join(RAW_FILES_DIR, "metadata.json")
MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 64))

class Pipeline:
def init(self):
logger.info("🚀 Initializing Parser & Indexer Pipeline...")
self.model = self._load_model()
self.indexer = ESIndexer()
self.metadata = self._load_metadata()
self.processed_ids = self.indexer.get_all_document_ids()
logger.info(f"Found {len(self.processed_ids)} documents already in Elasticsearch. They will be skipped.")

def _load_model(self):
    logger.info(f"Loading NLP model: '{MODEL_NAME}'...")
    return SentenceTransformer(MODEL_NAME)

def _load_metadata(self):
    logger.info("Loading metadata from scraper...")
    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def run(self):
    self.indexer.create_index_if_not_exists()
    all_files = [f for f in os.listdir(RAW_FILES_DIR) if f.endswith('.txt')]
    
    docs_to_process = []
    for filename in tqdm(all_files, desc="1/3: Preparing documents"):
        file_id = os.path.splitext(filename)[0]
        if file_id not in self.metadata: continue

        try:
            with open(os.path.join(RAW_FILES_DIR, filename), 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            logger.warning(f"Could not read file {filename}: {e}")
            continue

        file_meta = self.metadata[file_id]
        blocks = segment_file(content, file_meta.get('file_type', 'unknown'))
        
        for i, block in enumerate(blocks):
            doc_id = f"{file_id}_block_{i}"
            if doc_id in self.processed_ids: continue # Skip if already indexed

            docs_to_process.append({
                "_id": doc_id, "raw_code_snippet": block["code"], "associated_comments": block["comments"],
                **file_meta
            })
    
    if not docs_to_process:
        logger.info("✅ No new documents to process. Index is up to date.")
        return

    logger.info(f"Found {len(docs_to_process)} new documents to index.")
    
    # Process in batches for memory efficiency
    for i in tqdm(range(0, len(docs_to_process), BATCH_SIZE), desc="2/3: Generating embeddings"):
        batch = docs_to_process[i:i + BATCH_SIZE]
        comments = [doc["associated_comments"] for doc in batch if doc["associated_comments"]]
        
        if comments:
            embeddings = self.model.encode(comments, show_progress_bar=False, convert_to_numpy=True)
            embed_idx = 0
            for doc in batch:
                if doc["associated_comments"]:
                    doc["comment_vector"] = embeddings[embed_idx].tolist()
                    embed_idx += 1
    
    logger.info("3/3: Bulk indexing all new documents...")
    self.indexer.index_batch(docs_to_process)
    logger.info("✅ Pipeline finished successfully.")
if name == "main":
pipeline = Pipeline()
pipeline.run()
