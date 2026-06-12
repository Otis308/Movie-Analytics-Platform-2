WITH raw_movies AS (
    SELECT * FROM {{ source('raw_tmdb', 'tmdb_discover_movies') }}
)

SELECT
    CAST(_dlt_id AS VARCHAR(50)) AS movie_dlt_id,   
    CAST(id AS BIGINT) AS movie_id,
    
    CAST(title AS VARCHAR(255)) AS title,
    CAST(original_language AS VARCHAR(10)) AS original_language,
    CAST(release_date AS DATE) AS release_date,
    
    CAST(popularity AS NUMERIC) AS popularity,
    CAST(vote_average AS NUMERIC) AS vote_average,
    CAST(vote_count AS INTEGER) AS vote_count,
    
    CAST(adult AS BOOLEAN) AS is_adult_movie,
    
    CAST(_loaded_at AS TIMESTAMP) AS raw_loaded_at

FROM raw_movies

WHERE id IS NOT NULL