# Component Documentation

This document explains the architecture and usage of the Extract and Transform components in the ELT pipeline.

## Extract Component

### Overview

The Extract component (`src/extract/`) is currently a proof-of-concept Python package that demonstrates environment-aware execution. It reads environment variables to allow the same extraction logic to run in different environments (local development vs GitHub Actions).

**Current Status**: The extract component is a minimal implementation that validates the environment setup but does not perform actual data extraction yet.

**Future Goal**: This package will extract data from external systems and save it as parquet files to Azure Blob Storage, which will then be consumed by the Transform component.

### Architecture

```
src/extract/
├── src/extract/
│   ├── __init__.py
│   └── main.py              # Entry point with environment detection
├── tests/
│   ├── __init__.py
│   └── test_main.py         # Basic tests
├── pyproject.toml           # Dependencies and configuration
└── uv.lock                  # Locked dependencies
```

### Key Files

- **`main.py`**: Contains the `main()` function that reads the `ENVIRONMENT` variable and demonstrates environment-aware execution
- **`pyproject.toml`**: Defines the package metadata, dependencies (pandas), and the `extract-pipeline` console script

### Configuration

The extract component uses environment variables for configuration:

```python
env = os.getenv("ENVIRONMENT", "default")
print(f"Starting extraction in environment: {env}")
```

**Environment Values**:

- `development` - Local development (set by mise.toml)
- `production` - GitHub Actions environment
- `default` - Fallback when no environment is specified

### Running the Extract Component

```bash
cd src/extract

# Install dependencies
uv sync --locked --dev

# Run the extraction pipeline
uv run extract-pipeline

# Run tests
uv run pytest tests/
```

## Transform Component

### Overview

The Transform component (`src/transform/`) is a dbt project that processes raw data into analytics-ready tables. It follows a two-layer architecture with staging models for data cleaning and marts models for business logic.

**Data Source**: The dbt source tables reference parquet files stored on Azure Blob Storage that are created by the Extract component.

### Architecture

```
src/transform/
├── models/
│   ├── staging/            # Raw data cleaning layer
│   │   ├── dimensions/     # Dimension table staging
│   │   └── system1/        # System1 source staging
│   └── marts/              # Business logic layer
│       └── tableau/        # Analytics-ready outputs
├── dbt_project.yml         # Project configuration
├── profiles.yml            # Database connections
└── database/               # Local DuckDB storage
    └── dwh_local.duckdb
```

### Data Models

#### Staging Models

Staging models clean and standardize raw data from source systems:

- **`stg_system1__activity`**: Processes activity data from system1
- **`stg_dimensions__system1`**: Maps system1 dimension data  
- **`stg_dimensions__master`**: Master dimension mappings

#### Marts Models

Marts models implement business logic and create analytics-ready tables:

- **`activity`**: Combines activity data with project dimensions for Tableau reporting

### Configuration

#### Database Connections (`profiles.yml`)

```yaml
transform:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: "database/dwh_local.duckdb"
    prod:
      type: duckdb
      # Production configuration with Azure Blob Storage
```

#### Project Settings (`dbt_project.yml`)

```yaml
name: "transform"
model-paths: ["models"]
# All models default to view materialization
models:
  transform:
    +materialized: view
```

### Adding a New Staging Model

To add a new staging model for a new data source, follow these steps:

#### 1. Create the Source Configuration

Add your source definition in the appropriate `_sources.yml` file. For example, to add a new system2 source:

```yaml
# models/staging/system2/_system2__sources.yml
sources:
  - name: system2
    tables:
      - name: customers
        external:
          location: "abfs://raw/system2/customers.parquet"
      - name: orders
        external:
          location: "abfs://raw/system2/orders.parquet"
```

#### 2. Create the Staging Model

Create the SQL file for your staging model:

```sql
-- models/staging/system2/stg_system2__customers.sql
with

source as (
    select * from {{ source('system2', 'customers') }}
)

select * from source
```

#### 3. Add Model Documentation

Document your new model:

```yaml
# models/staging/system2/_system2__models.yml
models:
  - name: stg_system2__customers
    description: "Staging model for system2 customer data"
    columns:
      - name: customer_id
        description: "Unique customer identifier"
        data_tests:
          - unique
          - not_null
```

#### 4. Follow Naming Conventions

- **Directory**: `models/staging/{source_system}/`
- **Model file**: `stg_{source_system}__{table_name}.sql`
- **Documentation**: `_{source_system}__models.yml` and `_{source_system}__sources.yml`
- **Blob Storage Path**: `abfs://raw/{source_system}/{table_name}.parquet`

**Example**: For a new "system2" with a "customers" table:

- Directory: `models/staging/system2/`
- Model: `stg_system2__customers.sql`
- Source location: `abfs://raw/system2/customers.parquet`
- Files: `_system2__sources.yml`, `_system2__models.yml`

### Running the Transform Component

```bash
cd src/transform

# Install dependencies
uv sync --locked

# Run all models
dbt run --target dev

# Run specific model
dbt run --select stg_system1__activity

# Test models
dbt test

# Generate documentation
dbt docs generate
dbt docs serve
```

### Environment-Specific Behavior

The transform component supports different materializations based on environment:

```sql
{{
    config(
      materialized='external', 
      location='abfs://analytics/activity.parquet' if env_var('ENVIRONMENT') == 'prod' else 'view'
    )
}}
```

- **Development**: Models materialized as views in local DuckDB
- **Production**: Models materialized as external tables in Azure Blob Storage

### Testing

dbt provides several testing mechanisms:

```yaml
# In _models.yml files
models:
  - name: stg_system1__activity
    columns:
      - name: id
        data_tests:
          - unique
          - not_null
```

Run tests with:

```bash
dbt test                    # All tests
dbt test --select stg_*     # Staging model tests only
```

