# simple config module
import os

REPO_NAME = os.getenv("GITHUB_REPO", "owner/repo")
POLL_INTERVAL_SECONDS = int(os.getenv("POLL_INTERVAL_SECONDS", "300"))
