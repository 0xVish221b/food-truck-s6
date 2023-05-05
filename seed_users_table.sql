DROP TABLE IF EXISTS users;

CREATE TABLE users(id SERIAL PRIMARY KEY, email TEXT NOT NULL, name TEXT NOT NULL, password_hash TEXT NOT NULL);

INSERT INTO users(email, name, password_hash) VALUES
    ('foo@gmail.com', 'foo bar', '$2b$12$l4i64Xk9Iy7kZktddKlqHOoq4U80lphevF5IPsGcI3eFmZz55GGTe'),
    ('bar@hotmail.com', 'bar baz', '$2b$12$l4i64Xk9Iy7kZktddKlqHO05wtZUyMhEO1z3OiVOd9/Tb5oBTkW3S');
