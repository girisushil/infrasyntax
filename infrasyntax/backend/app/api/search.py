import logging
from fastapi import APIRouter, Query, HTTPException, Depends
from typing import List, Optional
from pydantic import BaseModel, Field
from ..services import search_service

logger = logging.getLogger(name)
router = APIRouter()

Pydantic models for type-safe API responses
class SearchResult(BaseModel):
raw_code_snippet: str
associated_comments: Optional[str] = None
repository_stars: int
source_repository: str
path: str
file_type: str

class SearchResponse(BaseModel):
query: str
count: int
results: List[SearchResult]

@router.get("/search", response_model=SearchResponse, tags=["Search"])
def search_snippets(q: str = Query(..., min_length=3, description="Natural language search query")):
if not q:
raise HTTPException(status_code=400, detail="Query parameter 'q' cannot be empty.")
try:
results = search_service.perform_search(query=q)
return {"query": q, "count": len(results), "results": results}
except Exception as e:
logger.error(f"Search failed for query '{q}': {e}", exc_info=True)
raise HTTPException(status_code=500, detail="An internal error occurred during search.")
