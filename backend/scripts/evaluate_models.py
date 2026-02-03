import time
import json
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer, CrossEncoder
from tqdm import tqdm

# --- CONFIGURATION ---
SNIPPETS_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "processed_snippets" / "enriched_snippets.json"
INDEX_NAME = 'infrasyntax'
ELASTICSEARCH_URL = "http://127.0.0.1:9200"

# Models
RETRIEVAL_MODEL_NAME = 'all-mpnet-base-v2'
RERANK_MODEL_NAME = 'cross-encoder/ms-marco-MiniLM-L-6-v2'

# Evaluation Settings
SAMPLE_SIZE = 50   # Number of test queries
TOP_K = 10         # Final results to evaluate
RRF_K = 60         # Standard constant for RRF formula

def load_data():
    if not SNIPPETS_PATH.exists():
        raise FileNotFoundError(f"Data not found at {SNIPPETS_PATH}")
    with open(SNIPPETS_PATH, 'r') as f:
        return json.load(f)

def compute_rrf(rank_dict_a, rank_dict_b):
    """
    Computes Reciprocal Rank Fusion score.
    Input: Two dicts {doc_id: rank}
    Output: Sorted list of (doc_id, score)
    """
    all_ids = set(rank_dict_a.keys()) | set(rank_dict_b.keys())
    rrf_scores = {}
    
    for doc_id in all_ids:
        # Default rank is infinite (very low score) if not found in list
        rank_a = rank_dict_a.get(doc_id, float('inf'))
        rank_b = rank_dict_b.get(doc_id, float('inf'))
        
        # RRF Formula: 1 / (k + r1) + 1 / (k + r2)
        # Note: Ranks are 1-based indices here
        score_a = 0 if rank_a == float('inf') else 1 / (RRF_K + rank_a)
        score_b = 0 if rank_b == float('inf') else 1 / (RRF_K + rank_b)
        
        rrf_scores[doc_id] = score_a + score_b
        
    # Sort by RRF score descending
    return sorted(rrf_scores.items(), key=lambda item: item[1], reverse=True)

def run_evaluation():
    print("--- 📊 Starting InfraSyntax RRF + Cross-Encoder Evaluation ---")
    
    print("Loading Models...")
    bi_encoder = SentenceTransformer(RETRIEVAL_MODEL_NAME)
    cross_encoder = CrossEncoder(RERANK_MODEL_NAME)
    es = Elasticsearch([ELASTICSEARCH_URL], verify_certs=False, ssl_show_warn=False)

    # Prepare Ground Truth
    all_snippets = load_data()
    valid_snippets = [s for s in all_snippets if s.get('description') and (s.get('id') or s.get('_id'))]
    test_set = random.sample(valid_snippets, min(SAMPLE_SIZE, len(valid_snippets)))
    
    print(f"Testing on {len(test_set)} random queries...")
    results = []

    for target in tqdm(test_set, desc="Evaluating"):
        query = target['description']
        # Fallback for ID if 'id' key is missing in JSON but exists in logic
        target_id = target.get('id', target.get('_id'))
        
        # --- 1. BASELINE: Bi-Encoder Only ---
        start_base = time.time()
        query_vector = bi_encoder.encode(query).tolist()
        
        base_query = {
            "size": TOP_K,
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'snippet_vector') + 1.0",
                        "params": {"query_vector": query_vector}
                    }
                }
            },
            "_source": ["id"]
        }
        resp_base = es.search(index=INDEX_NAME, body=base_query)
        latency_base = (time.time() - start_base) * 1000
        
        # Check Rank Baseline
        rank_base = float('inf')
        for i, hit in enumerate(resp_base['hits']['hits']):
            hit_id = hit['_source'].get('id', hit['_id'])
            if hit_id == target_id:
                rank_base = i + 1
                break

        # --- 2. ADVANCED: RRF (Hybrid) + Cross-Encoder ---
        start_adv = time.time()
        
        # A. Keyword Search (BM25)
        kw_query = {
            "size": 50,
            "query": {"multi_match": {"query": query, "fields": ["description^3", "code"]}},
            "_source": ["id", "description"]
        }
        resp_kw = es.search(index=INDEX_NAME, body=kw_query)
        
        # B. Vector Search (Dense)
        vec_query = {
            "size": 50,
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'snippet_vector') + 1.0",
                        "params": {"query_vector": query_vector}
                    }
                }
            },
            "_source": ["id", "description"]
        }
        resp_vec = es.search(index=INDEX_NAME, body=vec_query)
        
        # C. Perform RRF Fusion
        # Create {id: rank} maps
        ranks_kw = {h['_source'].get('id', h['_id']): i+1 for i, h in enumerate(resp_kw['hits']['hits'])}
        ranks_vec = {h['_source'].get('id', h['_id']): i+1 for i, h in enumerate(resp_vec['hits']['hits'])}
        
        fused_candidates = compute_rrf(ranks_kw, ranks_vec) # Returns [(id, score), ...]
        
        # D. Re-Ranking (Cross-Encoder)
        # We need the descriptions for the top 50 fused IDs to run Cross-Encoder
        # We fetch them from our previous responses (or you could mget them)
        candidate_map = {h['_source'].get('id', h['_id']): h['_source'] for h in resp_kw['hits']['hits'] + resp_vec['hits']['hits']}
        
        top_fused_ids = [c[0] for c in fused_candidates[:50]]
        pairs_to_rank = []
        valid_candidate_ids = []
        
        for cid in top_fused_ids:
            if cid in candidate_map:
                pairs_to_rank.append([query, candidate_map[cid].get('description', '')])
                valid_candidate_ids.append(cid)
                
        if pairs_to_rank:
            ce_scores = cross_encoder.predict(pairs_to_rank)
            # Combine IDs with CE Scores
            final_ranked = sorted(zip(valid_candidate_ids, ce_scores), key=lambda x: x[1], reverse=True)
            final_top_ids = [x[0] for x in final_ranked[:TOP_K]]
        else:
            final_top_ids = []

        latency_adv = (time.time() - start_adv) * 1000

        # Check Rank Advanced
        rank_adv = float('inf')
        if target_id in final_top_ids:
            rank_adv = final_top_ids.index(target_id) + 1

        # --- Record Results ---
        results.append({
            "Pipeline": "Baseline (Bi-Encoder)",
            "Query": query,
            "MRR": 1.0 / rank_base if rank_base != float('inf') else 0.0,
            "Recall@10": 1 if rank_base <= 10 else 0,
            "Latency (ms)": latency_base
        })

        results.append({
            "Pipeline": "InfraSyntax (RRF + Cross-Encoder)",
            "Query": query,
            "MRR": 1.0 / rank_adv if rank_adv != float('inf') else 0.0,
            "Recall@10": 1 if rank_adv <= 10 else 0,
            "Latency (ms)": latency_adv
        })

    # --- Generate Report ---
    df = pd.DataFrame(results)
    summary = df.groupby("Pipeline").agg({
        "MRR": "mean",
        "Recall@10": "mean",
        "Latency (ms)": "mean"
    }).reset_index()

    print("\n" + "="*50)
    print("🚀 RRF + CROSS-ENCODER PERFORMANCE ANALYSIS")
    print("="*50)
    print(summary.to_string(index=False))
    
    # Plots
    generate_plots(summary)

def generate_plots(summary):
    # Setup the figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # 1. FIX WARNINGS: Add hue=... and legend=False
    sns.barplot(
        data=summary, 
        x="Pipeline", 
        y="MRR", 
        hue="Pipeline",  # Fixes FutureWarning
        legend=False,    # Fixes FutureWarning
        ax=axes[0], 
        palette="viridis"
    )
    axes[0].set_title("Mean Reciprocal Rank (Higher is Better)")
    
    sns.barplot(
        data=summary, 
        x="Pipeline", 
        y="Recall@10", 
        hue="Pipeline", 
        legend=False, 
        ax=axes[1], 
        palette="magma"
    )
    axes[1].set_title("Recall@10 (Higher is Better)")
    
    sns.barplot(
        data=summary, 
        x="Pipeline", 
        y="Latency (ms)", 
        hue="Pipeline", 
        legend=False, 
        ax=axes[2], 
        palette="rocket"
    )
    axes[2].set_title("Average Latency (Lower is Better)")
    
    plt.tight_layout()

    # 2. FIX FILE PATH CRASH
    # This gets the folder where THIS script (evaluate_models.py) lives
    script_dir = Path(__file__).parent.resolve()
    
    # Save directly in the same folder as the script, or go up one level
    # Option A: Save in the same folder as the script
    output_path = script_dir / "analysis_report.png"
    
    # Option B: If you specifically wanted it in the backend root:
    # output_path = script_dir.parent / "analysis_report.png"

    print(f"Saving plot to: {output_path}")
    plt.savefig(output_path)
# def generate_plots(summary):
#     sns.set_theme(style="whitegrid")
#     fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
#     # 1. MRR
#     sns.barplot(data=summary, x="Pipeline", y="MRR", ax=axes[0], palette="viridis")
#     axes[0].set_title("Accuracy (Mean Reciprocal Rank)\nRRF Fusion finds the 'Best' match faster")
#     axes[0].set_ylim(0, 1.1)

#     # 2. Recall
#     sns.barplot(data=summary, x="Pipeline", y="Recall@10", ax=axes[1], palette="magma")
#     axes[1].set_title("Recall@10 (Hit Rate)\nHybrid search misses fewer edge cases")
#     axes[1].set_ylim(0, 1.1)

#     # 3. Latency
#     sns.barplot(data=summary, x="Pipeline", y="Latency (ms)", ax=axes[2], palette="rocket")
#     axes[2].set_title("Latency (ms)\nTrade-off for higher accuracy")

#     plt.tight_layout()
#     output = Path("backend/analysis_report.png")
#     plt.savefig(output)
#     print(f"\n✅ Analysis Graphs saved to: {output.resolve()}")

if __name__ == "__main__":
    run_evaluation()