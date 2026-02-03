import json
import sys
from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

# Set up the YAML parser
yaml = YAML(typ='rt') # 'rt' (round-trip) preserves comments
yaml.preserve_quotes = True

project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root / "backend"))

def extract_tasks_from_list(task_list):
    """
    Given a list of tasks, extract each one as a snippet.
    """
    snippets = []
    if not isinstance(task_list, CommentedSeq):
        return []

    for task in task_list:
        if not isinstance(task, CommentedMap):
            continue

        # The 'name' field is our perfect description
        description = task.get('name', '')
        
        # We'll use the whole task as the code snippet
        from io import StringIO
        string_stream = StringIO()
        yaml.dump(task, string_stream)
        code = string_stream.getvalue()

        # Simple filter: if there's no name, it's not a great snippet
        if description and code:
            snippets.append({
                "type": "ansible-task",
                "description": description,
                "code": code,
            })
    return snippets

def find_tasks_in_doc(doc):
    """
    Recursively finds 'tasks:' keys in a document.
    This handles playbooks, roles, etc.
    """
    snippets = []
    
    if isinstance(doc, CommentedMap):
        for key, value in doc.items():
            if key == 'tasks':
                snippets.extend(extract_tasks_from_list(value))
            else:
                # Recurse into nested dictionaries or lists
                snippets.extend(find_tasks_in_doc(value))
                
    elif isinstance(doc, CommentedSeq):
        # Handle lists of plays (e.g., a top-level playbook file)
        for item in doc:
            snippets.extend(find_tasks_in_doc(item))
            
    return snippets

def parse_ansible_file(file_path: Path):
    """
    Parses a single YAML file, looking for Ansible tasks.
    """
    snippets = []
    try:
        content = file_path.read_text(encoding='utf-8')
        # Check for common Ansible keys before parsing
        if 'hosts:' not in content and 'tasks:' not in content and 'name:' not in content:
            return [] # Unlikely to be an Ansible file

        for doc in yaml.load_all(content):
            if not doc:
                continue
            snippets.extend(find_tasks_in_doc(doc))
            
    except Exception as e:
        # This will catch YAML parsing errors
        # print(f"  [!] Failed to parse {file_path}: {e}")
        pass # Suppress errors for non-Ansible YAML files
    return snippets

def main():
    raw_data_dir = project_root / "data" / "raw_repos"
    output_dir = project_root / "data" / "processed_snippets"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_filepath = output_dir / "ansible_snippets.json"
    all_snippets = []
    
    print(f"Scanning for Ansible YAML files in {raw_data_dir}...")
    
    # Find all .yaml and .yml files
    config_files = list(raw_data_dir.rglob("*.yaml"))
    config_files.extend(list(raw_data_dir.rglob("*.yml")))
            
    print(f"Found {len(config_files)} total YAML files. Filtering for Ansible...")

    for i, file_path in enumerate(config_files):
        # We can optimize by checking the path
        path_str = str(file_path).lower()
        if 'ansible' not in path_str and 'playbook' not in path_str and 'roles' not in path_str:
            continue # Skip files not in likely Ansible-named dirs

        print(f"Parsing ({i+1}/{len(config_files)}): {file_path}")
        snippets = parse_ansible_file(file_path)
        
        if snippets:
            relative_path = str(file_path.relative_to(raw_data_dir))
            for snippet in snippets:
                snippet["source"] = relative_path
            all_snippets.extend(snippets)

    print(f"\n--- Total Ansible snippets extracted: {len(all_snippets)} ---")
    
    print(f"Saving snippets to {output_filepath}...")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(all_snippets, f, indent=2)
        
    print("Done.")

if __name__ == "__main__":
    main()