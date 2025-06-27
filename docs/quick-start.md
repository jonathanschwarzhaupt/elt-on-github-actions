# Quick Start Guide

Get up and running with the ELT pipeline in just a few minutes.

## Prerequisites & Setup Options

Choose one of these setup options:

### Option A: GitHub Codespaces/DevContainer (Recommended)

- Click "Code" → "Create codespace" in GitHub
- Everything is pre-configured and ready to use
- Skip to "Run Your First Pipeline" below

### Option B: Local Setup

- Python 3.13 installed
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager installed
- Git installed

## Clone the Repository

```bash
git clone <repo-url>
cd elt-on-github-actions
```

## Run Your First Pipeline

```bash
# Extract data
cd src/extract
uv sync --locked
uv run extract-pipeline

# Transform data  
cd ../transform
uv sync --locked
dbt run --target dev
```

## Verify It Works

- Check DuckDB database created at `src/transform/database/dwh_local.duckdb`
- View dbt docs: `dbt docs generate && dbt docs serve`
- Run tests: `dbt test`

## What You Just Built

You've successfully run a complete ELT pipeline:

- **Extract**: Pulled data from a fictional system
- **Load**: Stored raw data in DuckDB
- **Transform**: Created analytics-ready tables using dbt
- **Result**: Clean, tested data models ready for reporting

