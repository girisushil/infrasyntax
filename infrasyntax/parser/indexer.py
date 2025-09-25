import os
import logging
from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(name)

class ESIndexer:
def init(self):
self.es_client = Elasticsearch(
f"http://{os.getenv('ES_HOST')}:{os.getenv('ES_PORT')}",
request_timeout=30, max_retries=3, retry_on_timeout=True
)
self.index_name = os.getenv("ES_INDEX")
self.embedding_dims = int(os.getenv("EMBEDDING_DIMS"))

def create_index_if_not_exists(self):
    if not self.es_client.indices.exists(index=self.index_name):
        logger.info(f"Creating index '{self.index_name}'...")
        mapping = {
            "properties": {
                "raw_code_snippet": {"type": "text"},
                "associated_comments": {"type": "text"},
                "comment_vector": {
                    "type": "dense_vector", "dims": self.embedding_dims,
                    "index": True, "similarity": "cosine"
                },
                "repository_stars": {"type": "rank_feature"},
                "source_repository": {"type": "keyword"},
                "file_type": {"type": "keyword"},
                "path": {"type": "keyword"}
            }
        }
        self.es_client.indices.create(index=self.index_name, mappings=mapping)
    else:
        logger.info(f"Index '{self.index_name}' already exists.")

def get_all_document_ids(self):
    """Fetches all document IDs currently in the index to avoid re-indexing."""
    if not self.es_client.indices.exists(index=self.index_name): return set()
    
    ids = set()
    try:
        for hit in helpers.scan(self.es_client, index=self.index_name, query={"query": {"match_all": {}}, "_source": False}):
            ids.add(hit["_id"])
    except Exception as e:
        logger.error(f"Could not fetch document IDs from index: {e}")
    return ids

def index_batch(self, docs):
    actions = [
        {
            "_index": self.index_name, "_id": doc["_id"],
            "_source": {k: v for k, v in doc.items() if not k.startswith('_')}
        }
        for doc in docs if doc.get("_id")
    ]
    if not actions: return

    try:
        progress = tqdm(helpers.streaming_bulk(self.es_client, actions, chunk_size=100), total=len(actions), desc="Bulk Indexing")
        for ok, response in progress:
            if not ok: logger.warning(f"Error during bulk indexing: {response}")
    except helpers.BulkIndexError as e:
        logger.error(f"Bulk indexing failed with {len(e.errors)} errors.", exc_info=True)
