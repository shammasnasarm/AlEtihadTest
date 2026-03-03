import requests
import subprocess
import tempfile
import os
import pandas as pd


GITHUB_API = "https://api.github.com"


def get_repo_info(owner, repo):
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_contributors(owner, repo):
    contributors = []
    page = 1

    while True:
        url = f"{GITHUB_API}/repos/{owner}/{repo}/contributors?page={page}&per_page=100"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        contributors.extend(data)
        page += 1

    return contributors


def clone_repo(owner, repo):
    repo_url = f"https://github.com/{owner}/{repo}.git"
    print(repo_url)
    temp_dir = tempfile.mkdtemp()
    subprocess.run(
        ["git", "clone", "--depth", "1000", repo_url, temp_dir],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )
    return temp_dir


def count_lines_of_code(repo_path):
    total_lines = 0
    language_stats = {}

    extensions = (".py", ".js", ".ts", ".java", ".go", ".cpp", ".c")

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(extensions):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = len(f.readlines())
                        total_lines += lines
                        ext = file.split(".")[-1]
                        language_stats[ext] = language_stats.get(ext, 0) + lines
                except Exception:
                    continue

    return total_lines, language_stats


def get_commits_per_week(repo_path):
    result = subprocess.run(
        ["git", "-C", repo_path, "log", "--pretty=format:%cd", "--date=short"],
        capture_output=True,
        text=True
    )

    dates = result.stdout.split("\n")
    df = pd.DataFrame(dates, columns=["date"])
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna()

    df["week"] = df["date"].dt.to_period("W")
    commits_per_week = df.groupby("week").size()

    return commits_per_week