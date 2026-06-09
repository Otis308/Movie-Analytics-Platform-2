CREATE TABLE countries (
    iso_3166_1 VARCHAR(10) PRIMARY KEY,
    english_name VARCHAR(255),
    native_name VARCHAR(255)
);

CREATE TABLE languages (
    iso_639_1 VARCHAR(10) PRIMARY KEY,
    english_name VARCHAR(255),
    native_name VARCHAR(255)
);

CREATE TABLE genres (
    genre_id INT PRIMARY KEY,
    genre_name VARCHAR(255)
);

CREATE TABLE genders (
    gender_id INT PRIMARY KEY,
    gender_name VARCHAR(50)
);

CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(255) UNIQUE
);

CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    department_id INT,
    job_name VARCHAR(255),

    CONSTRAINT fk_job_department
        FOREIGN KEY(department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE credit_types (
    credit_type_id SERIAL PRIMARY KEY,
    credit_type_name VARCHAR(100)
);

CREATE TABLE timezones (
    timezone_id SERIAL PRIMARY KEY,
    zone_name VARCHAR(255) UNIQUE
);

CREATE TABLE primary_translations (
    translation_code VARCHAR(20) PRIMARY KEY,
    iso_639_1 VARCHAR(10),
    iso_3166_1 VARCHAR(10),

    FOREIGN KEY (iso_639_1)
        REFERENCES languages(iso_639_1),

    FOREIGN KEY (iso_3166_1)
        REFERENCES countries(iso_3166_1)
);