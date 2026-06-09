CREATE TABLE translations (
    translation_id SERIAL PRIMARY KEY,

    movie_id INT,
    tv_show_id INT,

    iso_3166_1 VARCHAR(10),
    iso_639_1 VARCHAR(10),

    name VARCHAR(255),
    english_name VARCHAR(255),

    FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id),

    FOREIGN KEY(tv_show_id)
        REFERENCES tv_shows(tv_show_id),

    FOREIGN KEY(iso_3166_1)
        REFERENCES countries(iso_3166_1),

    FOREIGN KEY(iso_639_1)
        REFERENCES languages(iso_639_1)
);

CREATE TABLE translation_data (
    data_id SERIAL PRIMARY KEY,

    translation_id INT,

    title VARCHAR(500),

    overview TEXT,

    homepage VARCHAR(500),

    FOREIGN KEY(translation_id)
        REFERENCES translations(translation_id)
);