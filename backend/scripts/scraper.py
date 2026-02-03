import os
import subprocess
import time
from pathlib import Path
from dotenv import load_dotenv
from github import Github, RateLimitExceededException

# A list of diverse, high-quality search queries
QUERIES = [
    # Nginx focused
    "filename:nginx.conf stars:>100",
    '"reverse proxy" in:readme language:nginx stars:>50',
    '"load balancer" in:readme language:nginx stars:>50',
    # Docker focused
    "filename:Dockerfile stars:>200",
    "filename:docker-compose.yml stars:>100",
    # Kubernetes focused
    "filename:kustomization.yaml stars:>100",
    "filename:deployment.yaml stars:>100",
    '"kubernetes manifest" in:readme stars:>50',
    '"ingress controller" in:readme stars:>100',
    '"helm chart" in:readme stars:>50',
]

# The total number of unique repositories we want to clone
TOTAL_LIMIT = 2000

def main():
    """
    Finds and clones a large, diverse set of GitHub repositories
    containing DevOps configuration files.
    """
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(dotenv_path=env_path)
    github_token = os.getenv("GITHUB_TOKEN")

    if not github_token:
        print("Error: GITHUB_TOKEN not found. Please check your .env file.")
        return

    g = Github(github_token)
    print("Successfully authenticated with GitHub.")

    output_dir = Path(__file__).parent.parent.parent / "data" / "raw_repos"
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Cloning repositories into: {output_dir}")

    cloned_count = 0
    # Use a set to keep track of cloned repo full_names to avoid duplicates
    cloned_repos = set()

    for query in QUERIES:
        if cloned_count >= TOTAL_LIMIT:
            print("Reached the total clone limit. Exiting.")
            break

        print(f"\n--- Running query: '{query}' ---")
        
        try:
            repositories = g.search_repositories(query=query)
            print(f"Query found {repositories.totalCount} potential repositories.")
            
            for repo in repositories:
                if cloned_count >= TOTAL_LIMIT:
                    break
                
                if repo.full_name in cloned_repos:
                    # We have already processed this repo from a different query
                    continue

                repo_dir = output_dir / repo.full_name.replace("/", "_")
                if repo_dir.exists():
                    print(f"Skipping {repo.full_name}, directory already exists.")
                    cloned_repos.add(repo.full_name)
                    continue

                print(f"Cloning {repo.full_name}...")
                try:
                    subprocess.run(
                        ["git", "clone", "--depth", "1", repo.clone_url, str(repo_dir)],
                        check=True,
                        capture_output=True,
                        text=True
                    )
                    cloned_count += 1
                    cloned_repos.add(repo.full_name)
                    print(f"Successfully cloned {repo.full_name}. ({cloned_count}/{TOTAL_LIMIT})")
                
                except subprocess.CalledProcessError as e:
                    print(f"Failed to clone {repo.full_name}: {e.stderr}")

        except RateLimitExceededException:
            print("GitHub API rate limit exceeded. Waiting for 60 seconds...")
            time.sleep(60)
            continue # Retry the same query after waiting
        except Exception as e:
            print(f"An unexpected error occurred with query '{query}': {e}")

    print(f"\n--- Cloning complete. Total unique repositories cloned: {cloned_count} ---")

if __name__ == "__main__":
    main()