CREATE TABLE movie_genres (
    movie_id INT,
    genre_id INT,

    PRIMARY KEY(movie_id, genre_id),

    FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id),

    FOREIGN KEY(genre_id)
        REFERENCES genres(genre_id)
);

CREATE TABLE tv_genres (
    tv_show_id INT,
    genre_id INT,

    PRIMARY KEY(tv_show_id, genre_id),

    FOREIGN KEY(tv_show_id)
        REFERENCES tv_shows(tv_show_id),

    FOREIGN KEY(genre_id)
        REFERENCES genres(genre_id)
);

CREATE TABLE movie_languages (
    movie_id INT,
    iso_639_1 VARCHAR(10),

    PRIMARY KEY(movie_id, iso_639_1),

    FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id),

    FOREIGN KEY(iso_639_1)
        REFERENCES languages(iso_639_1)
);

CREATE TABLE tv_show_languages (
    tv_show_id INT,
    iso_639_1 VARCHAR(10),

    PRIMARY KEY(tv_show_id, iso_639_1),

    FOREIGN KEY(tv_show_id)
        REFERENCES tv_shows(tv_show_id),

    FOREIGN KEY(iso_639_1)
        REFERENCES languages(iso_639_1)
);

CREATE TABLE movie_countries (
    movie_id INT,
    iso_3166_1 VARCHAR(10),

    PRIMARY KEY(movie_id, iso_3166_1),

    FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id),

    FOREIGN KEY(iso_3166_1)
        REFERENCES countries(iso_3166_1)
);

CREATE TABLE tv_show_countries (
    tv_show_id INT,
    iso_3166_1 VARCHAR(10),

    PRIMARY KEY(tv_show_id, iso_3166_1),

    FOREIGN KEY(tv_show_id)
        REFERENCES tv_shows(tv_show_id),

    FOREIGN KEY(iso_3166_1)
        REFERENCES countries(iso_3166_1)
);

CREATE TABLE country_timezones (
    iso_3166_1 VARCHAR(10),
    timezone_id INT,

    PRIMARY KEY(
        iso_3166_1,
        timezone_id
    ),

    FOREIGN KEY(iso_3166_1)
        REFERENCES countries(iso_3166_1),

    FOREIGN KEY(timezone_id)
        REFERENCES timezones(timezone_id)
);