import json
import uuid
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
processed_dir = project_root / "data" / "processed_snippets"
output_filepath = processed_dir / "all_snippets.json"

# This maps our filenames to a clean 'technology' tag
TECHNOLOGY_MAP = {
    "nginx_snippets.json": "nginx",
    "docker_snippets.json": "docker",
    "yaml_snippets.json": "kubernetes", # We'll tag all as K8s for now
    "ansible_snippets.json": "ansible",
    "github_actions_snippets.json": "github-actions",
    "terraform_snippets.json": "terraform",
}

def main():
    print("Starting snippet unification...")
    all_snippets = []

    for filename, tech_name in TECHNOLOGY_MAP.items():
        filepath = processed_dir / filename
        if not filepath.exists():
            print(f"  [!] Warning: File not found, skipping: {filename}")
            continue

        print(f"  -> Processing {filename} as '{tech_name}'...")
        with open(filepath, 'r', encoding='utf-8') as f:
            snippets = json.load(f)

        for snippet in snippets:
            # Create a new, standardized snippet format
            clean_snippet = {
                "id": str(uuid.uuid4()), # Generate a unique ID
                "technology": tech_name,
                "description": snippet.get("description", "").strip(),
                "code": snippet.get("code", "").strip(),
                "source_file": snippet.get("source", ""),
            }
            all_snippets.append(clean_snippet)
        
        print(f"     ...added {len(snippets)} snippets.")

    print(f"\n--- Total snippets unified: {len(all_snippets)} ---")

    print(f"Saving to {output_filepath}...")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(all_snippets, f, indent=2)
        
    print("Done. All snippets are now in 'all_snippets.json'.")

if __name__ == "__main__":
    main()