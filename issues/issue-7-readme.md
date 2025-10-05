# Issue #7: CRITICAL: Memory leak causing OOM errors in production

**Created by:** atharvaawatade
**Labels:** bug, critical, memory-leak, production-issue, python, oom, performance
**Created at:** 2025-10-05T11:43:52Z

## Error Details

- **Stack Traces:**

- **Error Messages:**
Error: Unable to allocate array
- **File Paths:**
src/main.py
src/main.py
- **Function Names:**


## Issue Body

**Severity:** CRITICAL

**Description:**
Application experiences memory leak after processing ~1000 issues, leading to Out of Memory errors.

**Environment:**
- Production server
- Python 3.11.5
- 4GB RAM allocated
- Processing rate: 100 issues/min

**Stack trace:**
```
Traceback (most recent call last):
  File "src/main.py", line 89, in main_loop
    process_issues(fetched_issues)
  File "src/main.py", line 45, in process_issues
    filtered = [i for i in issues if is_valid_issue(i)]
MemoryError: Unable to allocate array
```

**Impact:**
- Production service crashes every 2 hours
- Requires manual restart
- Affecting 50+ users

**Temporary workaround:**
Restarting service manually, but need permanent fix ASAP.

**Suspected cause:**
Not clearing processed issues from memory, accumulating over time.


---
This file is auto-generated for tracking and analysis of this issue.
