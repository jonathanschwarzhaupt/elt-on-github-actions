{{
  config(
    materialized='external' if env_var('ENVIRONMENT') == 'prod' else 'view',
    location='abfs://analytics/activity.parquet' if env_var('ENVIRONMENT') == 'prod' else none,
  )
}}

with
activites as (
    select * from {{ ref('stg_system1__activity') }}
)

, projects as (
    select * from {{ ref('stg_dimensions__system1') }}
)

, project_names as (
    select * from {{ ref('stg_dimensions__master') }}
)

, activities_with_ids as (
    select
        t1.*
        , t2.project_id
    from activites t1
    left join projects t2
    on t1.mandanten_id = t2.mandanten_id
)

, activities_with_ids_and_names as (
    select
        t1.*
        , t2.project_name
    from activities_with_ids t1
    left join project_names t2
    on t1.project_id = t2.project_id
)

, selected as (
    select
        id
        , activity_type
        , job_title
        , request_date
        , mandanten_name
        , project_id
        , project_name
    from activities_with_ids_and_names
)

select * from selected
