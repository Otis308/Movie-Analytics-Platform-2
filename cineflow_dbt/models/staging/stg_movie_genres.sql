WITH raw_genres AS (
    SELECT * FROM {{ source('raw_tmdb', 'tmdb_discover_movies__genre_ids') }}
)

SELECT
    CAST(_dlt_parent_id AS VARCHAR(50)) AS movie_dlt_id,
    
    CAST(value AS INTEGER) AS genre_id

FROM raw_genres