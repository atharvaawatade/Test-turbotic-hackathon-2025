"""Main application entry point."""
import json
from pathlib import Path
from src import config
from src.utils import is_valid_issue

OUT_FILE = Path("issues.json")

def process_issues(issues):
    """Filter & save issues to a JSON file (example)."""
    filtered = [i for i in issues if is_valid_issue(i)]
    OUT_FILE.write_text(json.dumps(filtered, indent=2))
    print(f"Saved {len(filtered)} issue(s) to {OUT_FILE}")

if __name__ == "__main__":
    # demo run with dummy data
    demo_issues = [
        {"title": "Bug: crash on start", "body": "Steps to reproduce...", "labels": ["bug"]},
        {"title": "", "body": "", "labels": []},
    ]
    process_issues(demo_issues)
