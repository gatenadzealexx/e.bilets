CREATE SCHEMA ;

CREATE TABLE IF NOT EXISTS eventes(
    id SERIAL PRIMARY KEY,
    name_event VARCHAR(100),
    date_event DATE
);

CREATE TABLE IF NOT EXISTS bilets(
    id SERIAL PRIMARY KEY,
    bilets INT,
    type_bilets VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS events_bilets(
    id SERIAL PRIMARY KEY,
    name_event_id INT REFERENCES eventes (id) ON DELETE CASCADE,
    bilet_id INT REFERENCES bilets (id) ON DELETE CASCADE
);

