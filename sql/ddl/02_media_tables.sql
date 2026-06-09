CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(500),
    original_title VARCHAR(500),
    original_language VARCHAR(10),
    overview TEXT,

    poster_path VARCHAR(500),
    backdrop_path VARCHAR(500),

    release_date DATE,

    popularity NUMERIC(18,4),
    vote_average NUMERIC(4,2),
    vote_count INT
);

CREATE TABLE tv_shows (
    tv_show_id INT PRIMARY KEY,

    name VARCHAR(500),
    original_name VARCHAR(500),
    original_language VARCHAR(10),

    overview TEXT,

    poster_path VARCHAR(500),
    backdrop_path VARCHAR(500),

    first_air_date DATE,

    popularity NUMERIC(18,4),
    vote_average NUMERIC(4,2),
    vote_count INT
);

CREATE TABLE seasons (
    season_id INT PRIMARY KEY,

    tv_show_id INT,

    season_number INT,
    name VARCHAR(500),

    overview TEXT,

    episode_count INT,
    air_date DATE,

    poster_path VARCHAR(500),

    FOREIGN KEY(tv_show_id)
        REFERENCES tv_shows(tv_show_id)
);

CREATE TABLE collections (
    collection_id INT PRIMARY KEY,

    name VARCHAR(500),

    overview TEXT,

    poster_path VARCHAR(500),
    backdrop_path VARCHAR(500)
);

CREATE TABLE collection_movies (
    collection_id INT,
    movie_id INT,

    PRIMARY KEY(collection_id, movie_id),

    FOREIGN KEY(collection_id)
        REFERENCES collections(collection_id),

    FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id)
);