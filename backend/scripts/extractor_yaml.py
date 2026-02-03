import json
import sys
from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

# Set up the YAML parser
yaml = YAML(typ='rt') # 'rt' (round-trip) preserves comments
yaml.preserve_quotes = True

project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root / "backend"))

def get_preceding_comments(doc, node_key):
    """
    Extracts comments that appear directly before a node (e.g., a service).
    """
    comments = []
    if not hasattr(doc, 'ca'):
        return ""
        
    comment_info = doc.ca.items.get(node_key)
    if comment_info and comment_info[0] and comment_info[0].value:
        # Get the comment lines and clean them
        comment_lines = comment_info[0].value.split('\n')
        for line in comment_lines:
            cleaned_line = line.strip().lstrip('#').strip()
            if cleaned_line:
                comments.append(cleaned_line)
    return "\n".join(comments)

def extract_kubernetes_snippets(doc):
    """
    Extracts a single Kubernetes resource (Deployment, Service, etc.)
    """
    # We treat the entire valid K8s document as one snippet.
    # The 'kind' key is our primary indicator.
    if isinstance(doc, CommentedMap) and 'kind' in doc and 'apiVersion' in doc:
        description = get_preceding_comments(doc, 'kind')
        
        # We need to convert the CommentedMap back to a string
        from io import StringIO
        string_stream = StringIO()
        yaml.dump(doc, string_stream)
        code = string_stream.getvalue()

        return {
            "type": f"kubernetes-{doc.get('kind', 'resource').lower()}",
            "description": description,
            "code": code,
        }
    return None

def extract_compose_snippets(doc):
    """
    Extracts individual services from a docker-compose file.
    """
    snippets = []
    if isinstance(doc, CommentedMap) and 'services' in doc:
        services = doc.get('services')
        if not isinstance(services, CommentedMap):
            return [] # Invalid services block

        for service_name, service_node in services.items():
            if not isinstance(service_node, CommentedMap):
                continue
            
            description = get_preceding_comments(services, service_name)
            
            # Re-dump this specific service block
            from io import StringIO
            string_stream = StringIO()
            yaml.dump({service_name: service_node}, string_stream)
            code = string_stream.getvalue()
            
            snippets.append({
                "type": "docker-compose-service",
                "description": description,
                "code": code,
            })
    return snippets

def parse_yaml_file(file_path: Path):
    """
    Parses a single YAML file, which may contain multiple documents.
    """
    snippets = []
    try:
        content = file_path.read_text(encoding='utf-8')
        # Load all documents (separated by '---')
        for doc in yaml.load_all(content):
            if not doc: # Skip empty documents
                continue
                
            # Try Kubernetes parser
            k8s_snippet = extract_kubernetes_snippets(doc)
            if k8s_snippet:
                snippets.append(k8s_snippet)
                continue # A doc is one thing, not both
            
            # Try Docker Compose parser
            compose_snippets = extract_compose_snippets(doc)
            if compose_snippets:
                snippets.extend(compose_snippets)

    except Exception as e:
        print(f"  [!] Failed to parse {file_path}: {e}")
    return snippets

def main():
    raw_data_dir = project_root / "data" / "raw_repos"
    output_dir = project_root / "data" / "processed_snippets"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_filepath = output_dir / "yaml_snippets.json"
    all_snippets = []
    
    print(f"Scanning for YAML config files in {raw_data_dir}...")
    
    # Find all .yaml and .yml files
    config_files = list(raw_data_dir.rglob("*.yaml"))
    config_files.extend(list(raw_data_dir.rglob("*.yml")))
            
    print(f"Found {len(config_files)} total YAML files.")

    for i, file_path in enumerate(config_files):
        print(f"Parsing ({i+1}/{len(config_files)}): {file_path}")
        snippets = parse_yaml_file(file_path)
        
        if snippets:
            relative_path = str(file_path.relative_to(raw_data_dir))
            for snippet in snippets:
                snippet["source"] = relative_path
            all_snippets.extend(snippets)

    print(f"\n--- Total K8s/Compose snippets extracted: {len(all_snippets)} ---")
    
    print(f"Saving snippets to {output_filepath}...")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(all_snippets, f, indent=2)
        
    print("Done.")

if __name__ == "__main__":
    main()