with

source as (
    select * from {{ source('system1', 'activity') }}
)

select * from source
