# Language Word-of-the-Day Sync Tool

A CLI tool to fetch and aggregate word-of-the-day entries from multiple language-learning apps (e.g., Duolingo, Memrise, Anki) into a single calendar or feed.

## Features
- Fetch word-of-the-day from multiple sources.
- Aggregate into a single feed or calendar.
- Support for offline caching.
- Modular design for easy API integration.

## Technical Architecture
- **Core Logic**: `core/sync.py` (separate from CLI for testability).
- **CLI**: `cli.py` (uses `typer` for modern CLI development).
- **API Clients**: `clients/` (modular clients for each language-learning app).
- **Tests**: `tests/` (unit tests for core logic and API clients).

## Dependencies
- `typer` (CLI)
- `requests` (HTTP requests)
- `icalendar` (calendar export)
- `pytest` (testing)

## License
MIT# Note

This repository is published under `fairyfemirins` due to GitHub namespace restrictions. A transfer to `femirins` is pending.

## Transfer Instructions

To request a transfer:
1. Open an issue in this repository.
2. Contact `@femirins` on GitHub.

### Manual Transfer Process
1. Navigate to: [https://github.com/fairyfemirins/language-word-sync/settings](https://github.com/fairyfemirins/language-word-sync/settings)
2. Under "Danger Zone", select "Transfer ownership".
3. Enter the target namespace (`femirins`) and confirm.