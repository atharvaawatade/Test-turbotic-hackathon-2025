"""Helper utilities for the project."""

def normalize_text(s: str) -> str:
    """Return lowercased, stripped text or empty string for None."""
    if s is None:
        return ""
    return s.strip().lower()

def is_valid_issue(issue: dict) -> bool:
    """Very small example validator for issue-like dicts."""
    title = normalize_text(issue.get("title"))
    body = normalize_text(issue.get("body"))
    return bool(title) or bool(body)
