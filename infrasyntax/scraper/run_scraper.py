import os
import json
import time
import logging
from github import Github, RateLimitExceededException, GithubException
from tqdm import tqdm
from dotenv import load_dotenv

Setup centralized logger
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(file), '..')))
from shared.logger import setup_logger
logger = setup_logger()

--- Configuration ---
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
raise ValueError("FATAL: GITHUB_TOKEN environment variable not set.")

OUTPUT_DIR = "scraped_data"
METADATA_FILE = os.path.join(OUTPUT_DIR, "metadata.json")
MAX_RESULTS_PER_QUERY = int(os.getenv("MAX_RESULTS_PER_QUERY", 500))
SEARCH_QUERIES = [
"filename:nginx.conf", "filename:docker-compose.yml", "filename:Dockerfile",
"extension:tf language:hcl", "filename:.travis.yml", 'path:.github/workflows filename:*.yml'
]

def load_existing_metadata():
if os.path.exists(METADATA_FILE):
with open(METADATA_FILE, 'r') as f:
return json.load(f)
return {}

def scrape_github():
logger.info("🚀 Starting GitHub scraper...")
g = Github(GITHUB_TOKEN)

os.makedirs(OUTPUT_DIR, exist_ok=True)
metadata = load_existing_metadata()
logger.info(f"Loaded {len(metadata)} existing metadata records. Will skip these files.")

total_files_processed = 0

for query in SEARCH_QUERIES:
    logger.info(f"Searching for: '{query}'...")
    try:
        results = g.search_code(query)
        progress_bar = tqdm(results, total=MAX_RESULTS_PER_QUERY, desc=f"Query '{query[:20]}...'")
        
        for i, content_file in enumerate(progress_bar):
            if i >= MAX_RESULTS_PER_QUERY: break
            
            try:
                repo = content_file.repository
                repo_name = repo.full_name.replace("/", "_")
                file_path_safe = content_file.path.replace("/", "_")
                unique_id = f"{repo_name}_{file_path_safe}"

                if unique_id in metadata: continue # Skip if already processed

                file_content = content_file.decoded_content.decode('utf-8', errors='ignore')
                with open(os.path.join(OUTPUT_DIR, f"{unique_id}.txt"), "w", encoding="utf-8") as f:
                    f.write(file_content)

                metadata[unique_id] = {
                    "source_repository": repo.html_url, "path": content_file.path,
                    "repository_stars": repo.stargazers_count,
                    "file_type": os.path.splitext(content_file.name)[1] or content_file.name
                }
                total_files_processed += 1
                time.sleep(0.2) # Be a good API citizen

            except Exception as e:
                logger.warning(f"Could not process file {content_file.path}: {e}", exc_info=False)
                continue

    except RateLimitExceededException:
        limit = g.get_rate_limit().core
        reset_time = limit.reset.strftime('%H:%M:%S')
        wait_seconds = max(0, (limit.reset - time.time())) + 5
        logger.warning(f"Rate limit exceeded. Waiting for {wait_seconds:.0f} seconds (resets at {reset_time})...")
        time.sleep(wait_seconds)
        continue
    except GithubException as e:
        logger.error(f"GitHub API error for query '{query}': {e}", exc_info=True)
        continue

with open(METADATA_FILE, "w", encoding="utf-8") as meta_f:
    json.dump(metadata, meta_f, indent=2)

logger.info(f"✅ Scraping finished. Added {total_files_processed} new files.")
if name == "main":
scrape_github()
