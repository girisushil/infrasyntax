import networkx as nx
import hcl2
import yaml
import re
import json
import pickle
from pathlib import Path

# Graph Storage Path
SNIPPETS_FILE = Path(__file__).parent.parent.parent / "data" / "processed_snippets" / "enriched_snippets.json"
GRAPH_FILE = Path(__file__).parent.parent.parent / "data" / "dependency_graph.pkl"

def build_graph():
    print("Building Dependency Graph...")
    
    # 1. Load your existing snippets
    with open(SNIPPETS_FILE, 'r') as f:
        snippets = json.load(f)
    
    # Initialize Directed Graph
    G = nx.DiGraph()
    
    # Helper: Map resource names to Snippet IDs
    # e.g., "aws_instance.web" -> "snippet-uuid-123"
    resource_map = {}
    
    # --- PASS 1: Register Nodes (Snippets) ---
    for snippet in snippets:
        G.add_node(snippet['id'], type=snippet['technology'])
        
        # Create a lookup key for Terraform resources
        # We need to parse the code to find its "logical name"
        if snippet['technology'] == 'terraform':
            try:
                # HCL parsing to find 'resource "aws_instance" "web"'
                parsed = hcl2.loads(snippet['code'])
                if 'resource' in parsed:
                    for res_type, res_data in parsed['resource'][0].items():
                        res_name = list(res_data.keys())[0]
                        # logical_key = "aws_instance.web"
                        logical_key = f"{res_type}.{res_name}"
                        resource_map[logical_key] = snippet['id']
            except Exception:
                continue # Skip complex/invalid snippets

    # --- PASS 2: Create Edges (Dependencies) ---
    for snippet in snippets:
        if snippet['technology'] == 'terraform':
            # Regex to find references like "aws_security_group.allow_tls.id"
            # This pattern looks for "word.word" inside the code
            references = re.findall(r'([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)', snippet['code'])
            
            for ref_type, ref_name in references:
                target_key = f"{ref_type}.{ref_name}"
                
                # If we found a valid link to another snippet in our DB
                if target_key in resource_map:
                    target_id = resource_map[target_key]
                    
                    # Don't link to self
                    if target_id != snippet['id']:
                        # Add Edge: Current Snippet -> DEPENDS ON -> Target Snippet
                        G.add_edge(snippet['id'], target_id, relation="depends_on")
                        print(f"🔗 Linked {snippet['id']} -> {target_id} ({target_key})")

    # Save the graph to disk
    print(f"Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    with open(GRAPH_FILE, 'wb') as f:
        pickle.dump(G, f)

if __name__ == "__main__":
    build_graph()