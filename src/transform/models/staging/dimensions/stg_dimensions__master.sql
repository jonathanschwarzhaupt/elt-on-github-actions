with

source as (
    select * from {{ source('dimensions', 'dim_master') }}
)

select * from source
