# README Template – `update-readme-repo`

GitHub Actions template to automatically generate a clean `README.md` with a dynamic table of your GitHub repositories.

[![Setup](https://img.shields.io/badge/Setup-Run%20Workflow-blue?style=for-the-badge)](../../actions/workflows/setup-readme.yml)

Use **Setup**, click **Run workflow**, and GitHub opens the run page where execution is shown live. The workflow will:
- copy `EXAMPLE.md` to `README.md`,
- delete `EXAMPLE.md`,
- commit and push the final `README.md`.

## Goal

This template runs an `update-readme-repo` workflow that:
- fetches repositories from a GitHub account,
- sorts them by stars,
- automatically updates a section of the README,
- commits/pushes changes when needed.

## Structure

```text
.github/workflows/update-readme-repo.yml
.github/workflows/setup-readme.yml
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
_Last update: 2026-04-20 07:55 UTC_

| Repository | Language | Stars | Description | Status |
|---|---|---:|---|---|
| [TarkovTracker-Archive](https://github.com/tarkovtracker-org/TarkovTracker-Archive) | TypeScript | 22 | TarkovTracker - Web App for tracking & planning your progression in the game Escape From Tarkov. | Archive |
| [docs](https://github.com/Nivmizz7/docs) | — | 1 | — | — |
| [RatScanner](https://github.com/tarkovtracker-org/RatScanner) | C# | 1 | Rat Scanner a helpful tool for Escape from Tarkov. | Fork |
| [TrackerBot](https://github.com/tarkovtracker-org/TrackerBot) | JavaScript | 1 | Discord Bot of TarkovTracker.org Discord server. | — |
| [annual-update-license-year](https://github.com/Nivmizz7/annual-update-license-year) | Shell | 0 | GitHub Action for update the year in the license. | — |
| [api](https://github.com/Nivmizz7/api) | JavaScript | 0 | API for TarkovData | Archive |
| [api-docs](https://github.com/Nivmizz7/api-docs) | JavaScript | 0 | Documentation for Nivmizz7/api | Archive |
| [azerothcore-boss](https://github.com/Nivmizz7/azerothcore-boss) | Lua | 0 | Addon for AzerothCore (WotLK 3.3.5) | — |
| [azerothcore-db](https://github.com/Nivmizz7/azerothcore-db) | JavaScript | 0 | — | — |
| [azerothcore-timer](https://github.com/Nivmizz7/azerothcore-timer) | Lua | 0 | Addon for AzerothCore (WotLK 3.3.5) | — |
| [boss_spawns](https://github.com/Nivmizz7/boss_spawns) | — | 0 | — | Fork |
| [cultist-circle](https://github.com/Nivmizz7/cultist-circle) | TypeScript | 0 | — | Fork |
| [fibonacci](https://github.com/Nivmizz7/fibonacci) | C | 0 | My work on the Fibonacci sequence. | Archive |
| [gh-pages](https://github.com/Nivmizz7/gh-pages) | HTML | 0 | — | — |
| [gh-runner-manager](https://github.com/Nivmizz7/gh-runner-manager) | Shell | 0 | GitHub runner manager for self-hosted runners. | — |
| [gm_chip8](https://github.com/Nivmizz7/gm_chip8) | — | 0 | GM Chip-8 is a Chip-8 emulator made under Game Maker 7.0 by Monokeros in January 2025. It features all of the opcodes and runs most of the games. This piece of software comes with no warranty and is property of Monokeros | — |
| [graph-template](https://github.com/Nivmizz7/graph-template) | JavaScript | 0 | Template for draw.io diagram. | Template |
| [guild-manager](https://github.com/Nivmizz7/guild-manager) | Vue | 0 | — | — |
| [hello_100](https://github.com/Nivmizz7/hello_100) | Solidity | 0 | "Hello, I am Niv." in 100 programming language. | — |
| [Jarvis](https://github.com/Nivmizz7/Jarvis) | — | 0 | Jarvis desktop assistant project | Fork |
| [kantine](https://github.com/Nivmizz7/kantine) | JavaScript | 0 | — | — |
| [kolotun](https://github.com/Nivmizz7/kolotun) | JavaScript | 0 | Shema of Kolotun Tarkov quest 2025 | Archive |
| [learning-markdown](https://github.com/Nivmizz7/learning-markdown) | — | 0 | Learning #1 - Markdown | Archive |
| [learning-review-pr](https://github.com/Nivmizz7/learning-review-pr) | HTML | 0 | Exercise: Review pull requests | Archive |
| [manager](https://github.com/Nivmizz7/manager) | HTML | 0 | — | — |
| [nginx_script](https://github.com/Nivmizz7/nginx_script) | Shell | 0 | — | — |
| [Nivmizz7](https://github.com/Nivmizz7/Nivmizz7) | Python | 0 | README for public profile. | — |
| [overlay-monitor](https://github.com/Nivmizz7/overlay-monitor) | JavaScript | 0 | — | Archive |
| [peninsula-client](https://github.com/Nivmizz7/peninsula-client) | C++ | 0 | — | — |
| [peninsula-server](https://github.com/Nivmizz7/peninsula-server) | JavaScript | 0 | — | — |
| [RatScanner-fork](https://github.com/Nivmizz7/RatScanner-fork) | C# | 0 | Rat Scanner a helpful tool for Escape from Tarkov. | Fork |
| [README-template](https://github.com/Nivmizz7/README-template) | Python | 0 | Template for README profile. | Template |
| [stash-fork](https://github.com/Nivmizz7/stash-fork) | JavaScript | 0 | The Tarkov.dev's Escape from Tarkov Discord bot | Fork |
| [tarkov-api](https://github.com/Nivmizz7/tarkov-api) | JavaScript | 0 | Tarkov.dev's API fork. | Archive |
| [tarkov-data-manager](https://github.com/Nivmizz7/tarkov-data-manager) | JavaScript | 0 | The Tarkov Data manager web app to manage the sql database | Fork |
| [tarkov-data-overlay](https://github.com/Nivmizz7/tarkov-data-overlay) | TypeScript | 0 | Data overlay for Tarkov.dev API data. | Fork |
| [tarkov-dev](https://github.com/Nivmizz7/tarkov-dev) | JavaScript | 0 | The official site for tarkov.dev - A web app to track item prices, view trader barters, quests, maps, and much more! | Fork |
| [tarkov-monitor-website](https://github.com/Nivmizz7/tarkov-monitor-website) | JavaScript | 0 | — | Archive |
| [tarkov-raid-planner](https://github.com/Nivmizz7/tarkov-raid-planner) | JavaScript | 0 | — | — |
| [tarkovdata](https://github.com/Nivmizz7/tarkovdata) | TypeScript | 0 | Escape From Tarkov game data, maintained by Niv. | Archive |
| [TarkovMonitor-fork](https://github.com/Nivmizz7/TarkovMonitor-fork) | C# | 0 | Monitor Tarkov log files to help track progress, queues, and groups | Fork |
| [TarkovTracker-fork](https://github.com/Nivmizz7/TarkovTracker-fork) | TypeScript | 0 | TarkovTracker - Web App for tracking & planning your progression in the game Escape From Tarkov. | Archive |
| [TarkovTrackerNuxt-fork](https://github.com/Nivmizz7/TarkovTrackerNuxt-fork) | TypeScript | 0 | Rewrite of TarkovTracker.org in Nuxt. | Fork |
| [template](https://github.com/Nivmizz7/template) | — | 0 | My template for my repository. | Template |
| [VSMU](https://github.com/Nivmizz7/VSMU) | JavaScript | 0 | Vintage Story Mods Updater | — |
| [web](https://github.com/Nivmizz7/web) | HTML | 0 | Webpage : nivmizz7.fr | — |
| [web-pickle](https://github.com/Nivmizz7/web-pickle) | CSS | 0 | Website for Pickle Team | — |
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