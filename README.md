# ELT on GitHub Actions

A proof-of-concept demonstrating modern ELT pipeline development using open-source tools, best practices, and infrastructure-light architecture.

## Overview

This project showcases how to build a **performant, maintainable ELT pipeline** using modern Python tooling and GitHub Actions. It demonstrates proper code organization, testing, automated releases, and development workflows - all while remaining lightweight and cost-effective.

**Key Highlights:**

- 🏗️ **Monorepo Structure** - Independent Extract and Transform components
- 🔧 **Modern Python Tooling** - uv, ruff, pytest with 80% coverage requirement
- 🚀 **Automated Releases** - Semantic versioning via conventional commits
- 🎯 **Infrastructure Light** - DuckDB + Azure Blob Storage architecture
- ✅ **Production Ready** - Comprehensive testing, linting, and CI/CD

## Architecture

```
Extract (Python) → Azure Blob Storage → Transform (dbt) → Analytics Tables
```

### Components

- **Extract** (`src/extract/`): Python package for data extraction (proof-of-concept)
- **Transform** (`src/transform/`): dbt project for data transformations using DuckDB
- **Storage**: Azure Blob Storage for data lake, DuckDB for compute

### Technology Stack

- **Python 3.13** with uv package manager
- **dbt** with DuckDB adapter for transformations  
- **Azure Blob Storage** for data persistence
- **GitHub Actions** for CI/CD
- **Release Please** for automated semantic versioning

## Quick Start

### Option 1: GitHub Codespaces (Recommended)

1. Click "Code" → "Create codespace"
2. Everything is pre-configured - start developing immediately!

### Option 2: Local Development

```bash
# Prerequisites: Python 3.13, uv, git
git clone https://github.com/your-username/elt-on-github-actions
cd elt-on-github-actions

# Extract component
cd src/extract
uv sync --locked --dev
uv run extract-pipeline

# Transform component
cd ../transform
uv sync --locked
dbt run --target dev
dbt test
```

## Development Features

### Code Quality

- **Automated formatting** with ruff
- **Comprehensive testing** with pytest (80% coverage minimum)
- **Pre-commit hooks** for code quality and conventional commits
- **Path-based CI** - tests only run when relevant files change

### Release Management

- **Conventional commits** enforced via commitizen
- **Automated releases** with semantic versioning
- **Component-based versioning** (e.g., `extract-v0.2.0`)
- **Automated changelogs** generated from commit messages

### Development Workflow

```bash
# Simple, standardized workflow
git pull origin main
git switch -c feat/my-feature
# make changes...
git commit -m "feat: add new feature"
git push -u origin feat/my-feature
# Open PR - CI runs automatically
```

## Why This Approach?

This project demonstrates several key principles for modern data engineering:

1. **Infrastructure Light**: Minimal cloud resources, maximum flexibility
2. **Developer Experience**: Fast setup, clear workflows, automated quality gates
3. **Maintainability**: Clear separation of concerns, comprehensive testing
4. **Scalability**: Monorepo structure allows independent component development
5. **Cost Effective**: Open-source tools, serverless architecture patterns

## Documentation

- **[📚 Full Documentation](docs/)** - Complete guides and references
- **[⚡ Quick Start](docs/quick-start.md)** - Get running in minutes
- **[👩‍💻 Developer Onboarding](docs/onboarding.md)** - Complete setup guide
- **[🏗️ Component Architecture](docs/components.md)** - Technical deep dive

## Project Status

This is a **proof-of-concept** demonstrating:

- ✅ Environment-aware execution (local vs. GitHub Actions)
- ✅ Automated testing and quality gates
- ✅ Semantic versioning and release automation
- ✅ dbt transformations with DuckDB
- 🚧 Data extraction implementation (placeholder)
- 🚧 Azure Blob Storage integration

## Acknowledgments

The development practices demonstrated in this project - including conventional commits, automated testing, GitHub Actions workflows, and release management - were learned from **Mischa Van Den Burg** and the **KubeCraft community**. Their excellent guidance on modern development workflows and best practices made this project possible.

- [KubeCraft Community](https://www.skool.com/kubecraft)
- [Mischa Van Den Burg](https://github.com/mischavandenburg/)

