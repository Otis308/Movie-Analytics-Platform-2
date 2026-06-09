CREATE TABLE system_configurations (
    config_id INT PRIMARY KEY DEFAULT 1,

    base_url VARCHAR(500),
    secure_base_url VARCHAR(500),

    backdrop_sizes TEXT[],
    logo_sizes TEXT[],
    poster_sizes TEXT[],
    profile_sizes TEXT[],
    still_sizes TEXT[],

    change_keys TEXT[]
);