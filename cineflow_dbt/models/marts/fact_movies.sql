-- Gọi các bảng staging đã được dbt xử lý thông qua hàm ref()
WITH movies AS (
    SELECT * FROM {{ ref('stg_tmdb_movies') }}
),

genres AS (
    SELECT * FROM {{ ref('stg_movie_genres') }}
),

-- Gom nhóm các ID thể loại lại thành một chuỗi cho mỗi bộ phim
movie_genres_agg AS (
    SELECT
        movie_dlt_id,
        STRING_AGG(CAST(genre_id AS VARCHAR), ', ') AS genre_ids_list
    FROM genres
    GROUP BY movie_dlt_id
)

-- Ghép nối dữ liệu phim với chuỗi thể loại vừa gom
SELECT
    m.movie_id,
    m.title,
    m.release_date,
    m.popularity,
    m.vote_average,
    m.vote_count,
    m.original_language,
    m.is_adult_movie,
    g.genre_ids_list,
    m.raw_loaded_at
FROM movies m
LEFT JOIN movie_genres_agg g
    ON m.movie_dlt_id = g.movie_dlt_id