CREATE DATABASE IF NOT EXISTS mydb;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;

\c mydb

CREATE TABLE estate (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255)
);

CREATE TABLE image (
    id SERIAL PRIMARY KEY,
    link VARCHAR(255),
    estate_id INTEGER REFERENCES estate(id)
);