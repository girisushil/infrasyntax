import logging
from elasticsearch import Elasticsearch
from ..core.model import model_loader
from ..core.config import settings

logger = logging.getLogger(name)
es_client = Elasticsearch(f"http://{settings.ES_HOST}:{settings.ES_PORT}", request_timeout=10)
model = model_loader.get_model()

def perform_search(query: str) -> list:
"""Performs a hybrid search using Reciprocal Rank Fusion (RRF)."""
logger.info(f"Performing RRF search for query: '{query}'")

try:
    query_vector = model.encode(query).tolist()

    # RRF combines the rank scores of multiple query types
    es_query = {
        "query": { "multi_match": { "query": query, "fields": ["associated_comments^2", "raw_code_snippet"]}},
        "knn": { "field": "comment_vector", "query_vector": query_vector, "k": 20, "num_candidates": 100 },
        "rank": { "rrf": {} }
    }
    
    response = es_client.search(
        index=settings.ES_INDEX,
        body=es_query,
        size=15
    )
    return [hit["_source"] for hit in response["hits"]["hits"]]

except Exception as e:
    logger.error(f"Elasticsearch search failed: {e}", exc_info=True)
    # Fallback to a simpler keyword search on failure
    logger.warning(f"Falling back to simple keyword search for query: '{query}'")
    fallback_query = { "multi_match": { "query": query, "fields": ["associated_comments", "raw_code_snippet"]}}
    response = es_client.search(index=settings.ES_INDEX, query=fallback_query, size=10)
    return [hit["_source"] for hit in response["hits"]["hits"]]
