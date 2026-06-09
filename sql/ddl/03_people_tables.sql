CREATE TABLE people (
    person_id INT PRIMARY KEY,

    name VARCHAR(255),
    original_name VARCHAR(255),

    gender_id INT,

    popularity NUMERIC(18,4),

    known_for_department VARCHAR(255),

    profile_path VARCHAR(500),

    adult BOOLEAN,

    FOREIGN KEY(gender_id)
        REFERENCES genders(gender_id)
);

CREATE TABLE credits (
    credit_id VARCHAR(100) PRIMARY KEY,

    person_id INT,

    movie_id INT,
    tv_show_id INT,

    credit_type_id INT,
    job_id INT,

    department VARCHAR(255),
    character VARCHAR(255),

    FOREIGN KEY(person_id)
        REFERENCES people(person_id),

    FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id),

    FOREIGN KEY(tv_show_id)
        REFERENCES tv_shows(tv_show_id),

    FOREIGN KEY(job_id)
        REFERENCES jobs(job_id),

    FOREIGN KEY(credit_type_id)
        REFERENCES credit_types(credit_type_id)
);