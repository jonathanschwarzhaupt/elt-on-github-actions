with

source as (
    select * from {{ source('dimensions', 'dim_system1') }}
)

select * from source
