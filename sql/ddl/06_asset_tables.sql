CREATE TABLE movie_images (
    movie_img_id SERIAL PRIMARY KEY,

    movie_id INT,

    img_type VARCHAR(50),

    file_path VARCHAR(500),

    aspect_ratio NUMERIC(8,4),

    width INT,
    height INT,

    iso_639_1 VARCHAR(10),

    vote_average NUMERIC(4,2),
    vote_count INT,

    FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id)
);

CREATE TABLE tv_show_images (
    tv_show_img_id SERIAL PRIMARY KEY,

    tv_show_id INT,

    img_type VARCHAR(50),

    file_path VARCHAR(500),

    aspect_ratio NUMERIC(8,4),

    width INT,
    height INT,

    iso_639_1 VARCHAR(10),

    vote_average NUMERIC(4,2),
    vote_count INT,

    FOREIGN KEY(tv_show_id)
        REFERENCES tv_shows(tv_show_id)
);