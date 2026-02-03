# import os
# import tempfile
# import subprocess
# import json
# import shutil

# # Checkov is a heavy CLI tool. We run it via subprocess for isolation.
# CHECKOV_PATH = shutil.which("checkov")

# def scan_snippet(code: str, technology: str) -> dict:
#     """
#     Runs a static security analysis (SAST) on the provided code snippet.
#     Returns a list of failed checks and a safety score.
#     """
#     if not CHECKOV_PATH:
#         return {"status": "error", "message": "Checkov not installed"}

#     # Map our technology names to Checkov frameworks
#     framework_map = {
#         "terraform": "terraform",
#         "docker": "dockerfile",
#         "kubernetes": "kubernetes",
#         # Nginx and Ansible are supported but require specific handling
#         "nginx": "secrets", # Fallback to secret scanning for generic files
#     }
    
#     framework = framework_map.get(technology)
#     if not framework:
#         return {"status": "skipped", "reason": "Technology not supported by scanner"}

#     # Create a temporary file to scan
#     with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=f".{technology}") as temp:
#         temp.write(code)
#         temp_path = temp.name

#     try:
#         # Run Checkov in silent mode, outputting JSON
#         cmd = [
#             CHECKOV_PATH,
#             "-f", temp_path,
#             "--framework", framework,
#             "--output", "json",
#             "--quiet",
#             "--soft-fail" # Don't crash on failure
#         ]
        
#         result = subprocess.run(cmd, capture_output=True, text=True)
        
#         # Checkov output parsing
#         try:
#             output_json = json.loads(result.stdout)
            
#             # Handle case where output is a list (multiple runners) or dict
#             if isinstance(output_json, list):
#                 # Usually the first runner has the relevant results for single files
#                 results_summary = output_json[0].get("results", {})
#             else:
#                 results_summary = output_json.get("results", {})

#             failed_checks = results_summary.get("failed_checks", [])
#             passed_checks = results_summary.get("passed_checks", [])
            
#             # Calculate a simple safety score (0-100)
#             total = len(failed_checks) + len(passed_checks)
#             score = 100
#             if total > 0:
#                 score = int((len(passed_checks) / total) * 100)

#             return {
#                 "status": "scanned",
#                 "safety_score": score,
#                 "vulnerabilities": [
#                     {"id": c["check_id"], "name": c["check_name"]} 
#                     for c in failed_checks
#                 ]
#             }

#         except json.JSONDecodeError:
#             return {"status": "error", "message": "Failed to parse scanner output"}

#     finally:
#         # Cleanup temp file
#         if os.path.exists(temp_path):
#             os.remove(temp_path)

import re

def scan_snippet(code: str, technology: str) -> dict:
    """
    Scans code for common security vulnerabilities using Regex patterns.
    Lightweight, fast, and works on partial snippets.
    """
    issues = []
    score = 100
    
    # Normalize for case-insensitive checking
    code_lower = code.lower()

    # --- 1. GLOBAL CHECKS ---
    
    # Detect hardcoded AWS Secret Keys (approximate regex)
    if re.search(r'(?<![A-Za-z0-9/+=])[A-Za-z0-9/+=]{40}(?![A-Za-z0-9/+=])', code):
        # Filter out common false positives by checking context
        if "secret" in code_lower or "key" in code_lower:
            issues.append({
                "id": "SEC-001", 
                "name": "Potential Hardcoded Credential/Secret", 
                "severity": "High"
            })
            score -= 50

    # Detect Generic Passwords
    if re.search(r'password\s*=\s*["\'].+["\']', code_lower):
        issues.append({
            "id": "SEC-002", 
            "name": "Hardcoded Password Detected", 
            "severity": "High"
        })
        score -= 40

    # --- 2. TERRAFORM CHECKS ---
    if technology == 'terraform':
        # Open Security Groups (0.0.0.0/0)
        if '0.0.0.0/0' in code:
            issues.append({
                "id": "TF-001", 
                "name": "Open Security Group (0.0.0.0/0) allows global access", 
                "severity": "High"
            })
            score -= 40

        # Unencrypted S3 Buckets
        if 'aws_s3_bucket' in code_lower and 'server_side_encryption' not in code_lower:
            issues.append({
                "id": "TF-002", 
                "name": "S3 Bucket appears unencrypted", 
                "severity": "Medium"
            })
            score -= 20

        # Public ACLs
        if 'acl' in code_lower and 'public' in code_lower:
            issues.append({
                "id": "TF-003", 
                "name": "S3 Bucket has Public ACL", 
                "severity": "High"
            })
            score -= 50

    # --- 3. PYTHON CHECKS ---
    elif technology == 'python':
        if 'eval(' in code or 'exec(' in code:
            issues.append({
                "id": "PY-001", 
                "name": "Dangerous function 'eval()' or 'exec()' detected", 
                "severity": "High"
            })
            score -= 40

    # Ensure score stays valid (0-100)
    final_score = max(0, score)

    return {
        "status": "scanned",
        "safety_score": final_score,
        "vulnerabilities": issues
    }