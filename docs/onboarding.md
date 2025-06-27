# Developer Onboarding Guide

Welcome to the ELT pipeline project! This guide will help you get set up for development and understand the codebase.

## Project Overview

This is an ELT (Extract, Load, Transform) pipeline project with two main components:

- **Extract Component** (`src/extract/`): Python package that extracts data from external systems
- **Transform Component** (`src/transform/`): dbt project that transforms raw data into analytics-ready tables

**Technology Stack:**

- Python 3.13 with uv package manager
- dbt with DuckDB adapter for transformations
- DuckDB as the local database
- Azure Blob Storage for production data
- GitHub Actions for CI/CD

## Development Environment Setup

### Option 1: Local Development

**Prerequisites:**

- Python 3.13 installed
- [uv package manager](https://docs.astral.sh/uv/getting-started/installation/) installed
- Git installed

**Setup Steps:**

```bash
# Clone the repository
git clone <repo-url>
cd elt-on-github-actions

# Set up extract component
cd src/extract
uv sync --locked --dev

# Set up transform component
cd ../transform
uv sync --locked

# Install pre-commit hooks (required for local development)
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg

# Install commitizen for interactive commit messages (recommended)
pip install --user pipx
pipx install commitizen
```

### Option 2: GitHub Codespaces (Recommended)

- Click "Code" → "Create codespace" in the GitHub repository
- The environment is automatically configured with all dependencies
- Pre-commit hooks are automatically installed
- Start developing immediately

**Verify Your Setup:**

```bash
# Test extract component
cd src/extract
uv run extract-pipeline

# Test transform component
cd ../transform
dbt run --target dev
dbt test
```

## Understanding the Codebase

### Project Structure

```
elt-on-github-actions/
├── src/
│   ├── extract/                    # Python extraction package
│   │   ├── src/extract/main.py     # Main extraction logic
│   │   ├── tests/                  # Extract tests
│   │   └── pyproject.toml          # Python dependencies
│   └── transform/                  # dbt transformation project
│       ├── models/                 # dbt models
│       │   ├── staging/            # Raw data cleaning
│       │   └── marts/              # Business logic models
│       ├── dbt_project.yml         # dbt configuration
│       └── profiles.yml            # Database connections
├── .github/workflows/              # CI/CD pipelines
└── docs/                           # Documentation
```

### Key Files

- **`mise.toml`**: Tool version management (used in codespaces)
- **`CLAUDE.md`**: Development guidance for AI assistants
- **`release-please-config.json`**: Automated release configuration
- **`.pre-commit-config.yaml`**: Code quality hooks

### Data Flow

1. **Extract**: `src/extract/main.py` pulls data from external systems
2. **Load**: Data is stored in DuckDB database (`src/transform/database/dwh_local.duckdb`)
3. **Transform**: dbt models process raw data into clean, analytics-ready tables
4. **Output**: Final data models available for reporting and analysis

## Development Workflow

### Git Workflow

Follow this simple workflow for making changes:

```bash
# Start with latest changes
git pull origin main

# Create a new branch using conventional commit prefixes
git switch -c feat/my-new-feature
# or
git switch -c fix/bug-description
# or  
git switch -c docs/update-readme

# Make your changes...

# Stage and commit with conventional commit message
git add .
git commit -m "feat: add new data extraction endpoint"

# Push your branch
git push -u origin feat/my-new-feature
```

### Conventional Commits

Use these prefixes for branch names and commit messages:

- **`feat/`** or **`feat:`** - New features
- **`fix/`** or **`fix:`** - Bug fixes
- **`docs/`** or **`docs:`** - Documentation changes
- **`refactor/`** or **`refactor:`** - Code refactoring
- **`test/`** or **`test:`** - Adding tests
- **`chore/`** or **`chore:`** - Maintenance tasks

**Recommended: Use commitizen for interactive commits:**

```bash
# Instead of manually typing commit messages
cz commit
# This will guide you through creating properly formatted commit messages
```

**Manual commit examples:**

```bash
git commit -m "feat: add customer data extraction"
git commit -m "fix: handle missing data in transform"
git commit -m "docs: update setup instructions"
```

### Pre-commit Hooks

The project automatically runs these checks before each commit:

- **Commitizen**: Validates commit message format
- **Ruff**: Formats and lints Python code

If pre-commit hooks fail, fix the issues and commit again.

### Pull Request Process

1. Create your branch and make changes
2. Test locally (see Testing section below)
3. Push your branch to GitHub
4. Open a Pull Request with:
   - Clear description of changes
   - Reference any related issues
   - Ensure CI checks pass

## Testing & Quality

### Extract Component Testing

```bash
cd src/extract

# Run all tests
uv run pytest tests/

# Run tests with coverage
uv run pytest tests/ --cov=src/extract --cov-report=xml --cov-fail-under=80

# Lint code
uv run ruff check src tests
uv run ruff format src tests
```

### Transform Component Testing

```bash
cd src/transform

# Run dbt models
dbt run --target dev

# Run dbt tests
dbt test

# Generate and view documentation
dbt docs generate
dbt docs serve
```

### Code Quality Requirements

- **Test Coverage**: Minimum 80% for extract component
- **Linting**: All code must pass ruff checks
- **Formatting**: Code is automatically formatted by ruff
- **Commit Messages**: Must follow conventional commit format

## Your First Contribution

Ready to make your first contribution? Here's a suggested workflow:

1. **Find a small task**: Look for issues labeled "good first issue" or make a small documentation improvement

2. **Create your branch**:

   ```bash
   git pull origin main
   git switch -c docs/improve-readme
   ```

3. **Make your change**: Edit files using your preferred editor

4. **Test locally**:

   ```bash
   # Test extract if you changed extract code
   cd src/extract
   uv run pytest tests/

   # Test transform if you changed dbt models
   cd src/transform
   dbt run --target dev
   dbt test
   ```

5. **Commit and push**:

   ```bash
   git add .
   # Use commitizen for guided commit message creation (recommended)
   cz commit
   # OR manually create commit message
   # git commit -m "docs: improve setup instructions"
   git push -u origin docs/improve-readme
   ```

6. **Open a Pull Request**: Go to GitHub and create a PR from your branch

The CI pipeline will automatically run tests and checks. Once approved, your changes will be merged and may trigger an automated release if you used `feat:` or `fix:` commits.

Welcome to the team! 🎉

