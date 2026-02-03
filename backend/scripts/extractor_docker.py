import json
import re
import sys
from pathlib import Path

# We are abandoning ANTLR for Dockerfiles.
# A line-based regex parser is more robust for this task.

project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root / "backend"))

# Regex to find an instruction.
# Matches "RUN ...", "COPY ...", etc., ignoring case.
INSTRUCTION_RE = re.compile(r'^\s*([a-zA-Z]+)\s+(.*)', re.IGNORECASE)
INTERESTING_INSTRUCTIONS = {'run', 'copy', 'add', 'cmd', 'entrypoint', 'healthcheck', 'shell'}

def find_snippets(file_content: str):
    """
    A custom, line-by-line parser for Dockerfiles.
    It's more robust than ANTLR for this task.
    """
    snippets = []
    lines = file_content.splitlines()
    
    comment_buffer = []
    current_multiline_code = []
    current_multiline_type = None
    multiline_start_line = 0

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # --- Handle multi-line commands ---
        if current_multiline_code:
            current_multiline_code.append(line)
            # Check if this is the end of the multi-line block
            if not stripped_line.endswith('\\'):
                snippets.append({
                    "type": f"docker-{current_multiline_type}",
                    "description": "\n".join(comment_buffer),
                    "code": "\n".join(current_multiline_code),
                    "start_line": multiline_start_line,
                })
                # Reset
                comment_buffer = []
                current_multiline_code = []
                current_multiline_type = None
            continue

        # --- Not in a multi-line command ---
        if stripped_line.startswith('#'):
            comment_buffer.append(stripped_line[1:].strip())
            continue
        
        if not stripped_line:
            comment_buffer = [] # Reset on empty lines
            continue

        match = INSTRUCTION_RE.match(line) # Use original line for match
        if match:
            instruction_type = match.group(1).lower()
            
            if instruction_type in INTERESTING_INSTRUCTIONS:
                # This is an instruction we care about
                if stripped_line.endswith('\\'):
                    # Start of a new multi-line block
                    current_multiline_code = [line]
                    current_multiline_type = instruction_type
                    multiline_start_line = i + 1
                else:
                    # Single-line instruction
                    snippets.append({
                        "type": f"docker-{instruction_type}",
                        "description": "\n".join(comment_buffer),
                        "code": line,
                        "start_line": i + 1,
                    })
                
                comment_buffer = [] # Clear buffer after use
            else:
                comment_buffer = [] # Not an interesting instruction
        else:
            comment_buffer = [] # Not a comment or instruction

    return snippets

def parse_file(file_path: Path):
    try:
        content = file_path.read_text(encoding='utf-8')
        return find_snippets(content)
    except Exception as e:
        print(f"  [!] Failed to read or parse {file_path}: {e}")
        return []

def main():
    """Main script to find all Dockerfiles and extract snippets."""
    raw_data_dir = project_root / "data" / "raw_repos"
    output_dir = project_root / "data" / "processed_snippets"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_filepath = output_dir / "docker_snippets.json"
    all_snippets = []
    
    print(f"Scanning for Dockerfiles in {raw_data_dir}...")
    
    # Find all files named 'Dockerfile' (case-insensitive)
    config_files = []
    for f in raw_data_dir.rglob("*"):
        if f.name.lower() == "dockerfile":
            config_files.append(f)
            
    print(f"Found {len(config_files)} total Dockerfiles.")

    for i, file_path in enumerate(config_files):
        print(f"Parsing ({i+1}/{len(config_files)}): {file_path}")
        snippets = parse_file(file_path)
        
        if snippets:
            relative_path = str(file_path.relative_to(raw_data_dir))
            for snippet in snippets:
                snippet["source"] = relative_path
            all_snippets.extend(snippets)

    print(f"\n--- Total Docker snippets extracted: {len(all_snippets)} ---")
    
    print(f"Saving snippets to {output_filepath}...")
    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(all_snippets, f, indent=2)
        
    print("Done.")

if __name__ == "__main__":
    main()