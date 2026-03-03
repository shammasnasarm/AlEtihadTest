import shutil
import argparse

from utils import get_repo_info, get_contributors, clone_repo, count_lines_of_code, get_commits_per_week


def main():
    parser = argparse.ArgumentParser(description="Analyze a public GitHub repository")
    parser.add_argument("repo", help="Repository in format owner/repo")
    args = parser.parse_args()

    owner, repo = args.repo.split("/")

    repo_info = get_repo_info(owner, repo)

    contributors = get_contributors(owner, repo)

    repo_path = clone_repo(owner, repo)

    total_lines, language_stats = count_lines_of_code(repo_path)

    commits_per_week = get_commits_per_week(repo_path)

    shutil.rmtree(repo_path)

    print("\n===== Repository Analysis =====")
    for key, value in repo_info.items():
        if key == "owner" or key == "license":
            continue
        print(f"    {key} => {value}")

    print(f"\nTotal Contributors: {len(contributors)}")
    print(f"Total Lines of Code: {total_lines}")

    print("\nLines by Language:")
    for lang, lines in language_stats.items():
        print(f"  {lang}: {lines}")

    print("\nCommits per Week:")
    print(commits_per_week)


if __name__ == "__main__":
    main()