import json
import re
import sys
from pathlib import Path

# We are no longer using ANTLR for Nginx.
# It's too brittle for real-world files.

project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root / "backend"))


def find_snippets(file_content: str):
    """
    A custom parser for Nginx files.
    It finds blocks (server, location, upstream) and grabs
    their preceding comments.
    """
    snippets = []
    lines = file_content.splitlines()
    
    # Regex to find the start of a block
    # Matches "server {", "location / {", "upstream my_app {", etc.
    block_start_re = re.compile(r'^\s*(server|location|upstream)\s*.*?{', re.IGNORECASE)
    
    comment_buffer = []
    current_block_lines = []
    block_type = None
    brace_level = 0

    for i, line in enumerate(lines):
        if block_type is None:
            # We are not inside a block, look for a new one
            
            # 1. Check for comments
            if line.strip().startswith('#'):
                comment_buffer.append(line.strip()[1:].strip())
                continue
                
            # 2. Check for block start
            match = block_start_re.match(line)
            if match:
                block_type = match.group(1).lower()
                current_block_lines = [line]
                brace_level = line.count('{') - line.count('}')
                
                # If brace level is already 0 (e.g., "server {}" on one line)
                if brace_level == 0:
                    snippets.append({
                        "type": block_type,
                        "description": "\n".join(comment_buffer),
                        "code": "\n".join(current_block_lines),
                        "start_line": i + 1,
                    })
                    block_type = None
                    current_block_lines = []
                    comment_buffer = []

            # 3. If it's a blank line or non-comment, clear comment buffer
            elif not line.strip():
                comment_buffer = [] # Comments must be immediately before
            else:
                comment_buffer = [] # Not a comment, not a block
                
        else:
            # We are inside a block, just count braces
            current_block_lines.append(line)
            brace_level += line.count('{')
            brace_level -= line.count('}')
            
            if brace_level <= 0:
                # We found the end of the block
                snippets.append({
                    "type": block_type,
                    "description": "\n".join(comment_buffer),
                    "code": "\n".join(current_block_lines),
                    "start_line": i + 1 - len(current_block_lines),
                })
                
                # Reset for the next block
                block_type = None
                current_block_lines = []
                comment_buffer = []

    return snippets


def parse_file(file_path: Path):
    try:
        content = file_path.read_text(encoding='utf-8')
        return find_snippets(content)
    except Exception as e:
        print(f"  [!] Failed to parse {file_path}: {e}")
        return []

def main():
    raw_data_dir = project_root / "data" / "raw_repos"
    output_dir = project_root / "data" / "processed_snippets"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_filepath = output_dir / "nginx_snippets.json"
    all_snippets = []
    
    print(f"Scanning for Nginx config files in {raw_data_dir}...")
    
    config_files = list(raw_data_dir.rglob("*.conf"))
    print(f"Found {len(config_files)} total .conf files.")

    for i, file_path in enumerate(config_files):
        # We also remove the old restrictive filter.
        # We'll just parse every .conf file.
        print(f"Parsing ({i+1}/{len(config_files)}): {file_path}")
        snippets = parse_file(file_path)
        
        if snippets:
            relative_path = str(file_path.relative_to(raw_data_dir))
            for snippet in snippets:
                snippet["source"] = relative_path
            all_snippets.extend(snippets)

    print(f"\n--- Total Nginx snippets extracted: {len(all_snippets)} ---")
    
    print(f"Saving snippets to {output_filepath}...")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(all_snippets, f, indent=2)
        
    print("Done.")

if __name__ == "__main__":
    main()