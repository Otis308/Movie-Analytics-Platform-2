CREATE TABLE companies (
    company_id INT PRIMARY KEY,

    name VARCHAR(255),

    description TEXT,

    headquarters VARCHAR(500),

    homepage VARCHAR(500),

    logo_path VARCHAR(500),

    origin_country VARCHAR(10),

    parent_company_id INT,

    FOREIGN KEY(parent_company_id)
        REFERENCES companies(company_id)
);

CREATE TABLE media_companies (
    media_company_id SERIAL PRIMARY KEY,

    movie_id INT,
    tv_show_id INT,

    company_id INT,

    FOREIGN KEY(movie_id)
        REFERENCES movies(movie_id),

    FOREIGN KEY(tv_show_id)
        REFERENCES tv_shows(tv_show_id),

    FOREIGN KEY(company_id)
        REFERENCES companies(company_id)
);