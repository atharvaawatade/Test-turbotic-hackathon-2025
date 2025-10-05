from pathlib import Path
from src.main import process_issues, OUT_FILE

def test_process_issues(tmp_path):
    # change output file to tmp path for test
    test_file = tmp_path / "test_issues.json"
    # monkeypatch the OUT_FILE variable
    import src.main as main_mod
    main_mod.OUT_FILE = test_file

    issues = [
        {"title": "Issue 1", "body": "something"},
        {"title": "", "body": ""}
    ]
    process_issues(issues)
    assert test_file.exists()
    content = test_file.read_text()
    assert "Issue 1" in content
