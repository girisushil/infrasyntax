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

def get_preceding_comments(doc, node_key):
    """
    Extracts comments that appear directly before a node.
    """
    comments = []
    if not hasattr(doc, 'ca'):
        return ""
        
    comment_info = doc.ca.items.get(node_key)
    if comment_info and comment_info[0] and comment_info[0].value:
        comment_lines = comment_info[0].value.split('\n')
        for line in comment_lines:
            cleaned_line = line.strip().lstrip('#').strip()
            if cleaned_line:
                comments.append(cleaned_line)
    return "\n".join(comments)

def extract_steps(steps_list):
    """
    Given a list of steps, extract each one as a snippet.
    """
    snippets = []
    if not isinstance(steps_list, CommentedSeq):
        return []

    for step in steps_list:
        if not isinstance(step, CommentedMap):
            continue

        # A step's 'name' is the best description
        # If no name, the 'uses' field is the next best
        description = step.get('name', step.get('uses', ''))
        
        # We'll use the whole step as the code snippet
        from io import StringIO
        string_stream = StringIO()
        yaml.dump(step, string_stream)
        code = string_stream.getvalue()

        if description and code:
            snippets.append({
                "type": "github-actions-step",
                "description": description,
                "code": code,
            })
    return snippets

def parse_workflow_file(file_path: Path):
    """
    Parses a single GitHub Actions YAML file.
    """
    snippets = []
    try:
        content = file_path.read_text(encoding='utf-8')
        doc = yaml.load(content) # A workflow file is a single doc
        if not doc or not isinstance(doc, CommentedMap):
            return []

        if 'jobs' in doc and isinstance(doc['jobs'], CommentedMap):
            for job_name, job_node in doc['jobs'].items():
                if (isinstance(job_node, CommentedMap) and 
                    'steps' in job_node and 
                    isinstance(job_node['steps'], CommentedSeq)):
                    
                    # Extract the steps from this job
                    job_steps = extract_steps(job_node['steps'])
                    for step in job_steps:
                        # Add job context to the snippet
                        step['job_name'] = job_name
                    snippets.extend(job_steps)
            
    except Exception as e:
        print(f"  [!] Failed to parse {file_path}: {e}")
    return snippets

def main():
    raw_data_dir = project_root / "data" / "raw_repos"
    output_dir = project_root / "data" / "processed_snippets"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_filepath = output_dir / "github_actions_snippets.json"
    all_snippets = []
    
    print(f"Scanning for GitHub Actions workflow files in {raw_data_dir}...")
    
    # GitHub Actions files are *always* in this directory
    config_files = list(raw_data_dir.rglob(".github/workflows/*.yaml"))
    config_files.extend(list(raw_data_dir.rglob(".github/workflows/*.yml")))
            
    print(f"Found {len(config_files)} total workflow files.")

    for i, file_path in enumerate(config_files):
        print(f"Parsing ({i+1}/{len(config_files)}): {file_path}")
        snippets = parse_workflow_file(file_path)
        
        if snippets:
            relative_path = str(file_path.relative_to(raw_data_dir))
            for snippet in snippets:
                snippet["source"] = relative_path
            all_snippets.extend(snippets)

    print(f"\n--- Total GitHub Actions snippets extracted: {len(all_snippets)} ---")
    
    print(f"Saving snippets to {output_filepath}...")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(all_snippets, f, indent=2)
        
    print("Done.")

if __name__ == "__main__":
    main()