# README Template – `update-readme-repo`

GitHub Actions template to automatically generate a clean `README.md` with a dynamic table of your GitHub repositories.

## Goal

This template runs an `update-readme-repo` workflow that:
- fetches repositories from a GitHub account,
- sorts them by stars,
- automatically updates a section of the README,
- commits/pushes changes when needed.

## Structure

```text
.github/workflows/update-readme-repo.yml
scripts/update-readme-repo.py
README.md
EXAMPLE.md
```

## Prerequisites

- A GitHub repository with Actions enabled
- Python 3.x
- A `README.md` with the following markers:

```md
<!-- REPO_TABLE:START -->
<!-- REPO_TABLE:END -->
```

If the markers are not present, the script adds a new section automatically.

## Local usage

```bash
python scripts/update-readme-repo.py --readme README.md --username "your-username"
```

Optional to avoid API rate limits:

```bash
export GITHUB_TOKEN="ghp_xxx"
python scripts/update-readme-repo.py --readme README.md --username "your-username"
```

## Workflow GitHub Actions

The `update-readme-repo` workflow is defined in:

- `.github/workflows/update-readme-repo.yml`

Triggers:
- manual (`workflow_dispatch`)
- weekly (Monday at 06:00 UTC)

Command used in the workflow:

```bash
python scripts/update-readme-repo.py --readme README.md --username "${{ github.repository_owner }}"
```

## Quick customization

- Edit the `cron` in `.github/workflows/update-readme-repo.yml`
- Adjust the text around the table in your `README.md`
- Use `EXAMPLE.md` as a visual base

## Example

A complete rendering example is available in [EXAMPLE.md](EXAMPLE.md)