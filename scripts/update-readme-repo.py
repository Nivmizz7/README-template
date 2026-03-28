#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

START_MARKER = "<!-- REPO_TABLE:START -->"
END_MARKER = "<!-- REPO_TABLE:END -->"


def repository_status(repo: dict) -> str:
    if repo.get("archived", False):
        return "Archive"
    if repo.get("fork", False):
        return "Fork"
    if repo.get("is_template", False):
        return "Template"
    return "—"


def gh_request(url: str, token: str | None) -> dict | list:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )

    try:
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"GitHub API error ({error.code}) for {url}: {body}") from error


def escape_md(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def fetch_repositories(username: str, token: str | None) -> list[dict]:
    repos: list[dict] = []
    page = 1

    while True:
        query = urllib.parse.urlencode(
            {
                "per_page": 100,
                "page": page,
                "sort": "updated",
                "direction": "desc",
                "type": "all",
            }
        )
        url = f"https://api.github.com/users/{urllib.parse.quote(username)}/repos?{query}"
        batch = gh_request(url, token)

        if not isinstance(batch, list):
            raise SystemExit("Unexpected response for repositories list")

        if not batch:
            break

        repos.extend(batch)
        page += 1

    repos.sort(key=lambda repo: (-repo.get("stargazers_count", 0), repo.get("name", "").lower()))
    return repos


def build_table(repos: list[dict]) -> str:
    header = "| Repository | Stars | Description | Status |\n|---|---:|---|---|"
    lines = [header]

    for repo in repos:
        name = repo.get("name", "unknown")
        html_url = repo.get("html_url", "")
        stars = repo.get("stargazers_count", 0)
        description = repo.get("description") or "—"
        status = repository_status(repo)

        repo_cell = f"[{escape_md(name)}]({html_url})" if html_url else escape_md(name)
        lines.append(f"| {repo_cell} | {stars} | {escape_md(description)} | {status} |")

    if len(lines) == 1:
        lines.append("| — | 0 | No repositories found. | — |")

    return "\n".join(lines)


def replace_section(readme: str, section_content: str) -> str:
    block = f"{START_MARKER}\n{section_content}\n{END_MARKER}"

    if START_MARKER in readme and END_MARKER in readme:
        start_index = readme.index(START_MARKER)
        end_index = readme.index(END_MARKER) + len(END_MARKER)
        return f"{readme[:start_index]}{block}{readme[end_index:]}"

    if not readme.endswith("\n"):
        readme += "\n"

    return f"{readme}\n## Dynamic Repositories Table\n\n{block}\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="update-readme-repo: update README repositories table")
    parser.add_argument("--readme", default="README.md", help="Path to README file")
    parser.add_argument("--username", default=os.getenv("GITHUB_USERNAME", "Nivmizz7"), help="GitHub username")
    args = parser.parse_args()

    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN")

    repos = fetch_repositories(args.username, token)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    table = build_table(repos)
    section = f"_Last update: {timestamp}_\n\n{table}"

    with open(args.readme, "r", encoding="utf-8") as file:
        content = file.read()

    updated = replace_section(content, section)

    with open(args.readme, "w", encoding="utf-8") as file:
        file.write(updated)


if __name__ == "__main__":
    main()
