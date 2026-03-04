# Repo Analyzer

A CLI tool that analyzes a public GitHub repository — fetches metadata and contributors via the GitHub REST API, clones the repo, counts lines of code per language, and shows weekly commit frequency.

---

## Project Structure

    repo_analyzer/
    │
    ├── main.py
    ├── utils.py
    └── requirements.txt

---

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run with a public repo in owner/repo format
python main.py psf/requests
```

---

## Output

```
===== Repository Analysis =====
    name => requests
    ...

Total Contributors: 42
Total Lines of Code: 18500

Lines by Language:
  py: 15000
  js: 3500

Commits per Week:
  week
  2026-01-05/2026-01-11    12
  ...
```

---

## What it does

- Fetches repo metadata (name, stars, forks, etc.) from GitHub API
- Fetches all contributors (paginated)
- Clones the repo with last 1000 commits (`--depth 1000`)
- Counts lines of code for `.py`, `.js`, `.ts`, `.java`, `.go`, `.cpp`, `.c`
- Shows commits grouped by week using `pandas`
- Cleans up the cloned repo after analysis
