CREATE TABLE users (id SERIAL PRIMARY KEY, usertype INTEGER NOT NULL, username TEXT UNIQUE, password TEXT, currentweight FLOAT, targetweight FLOAT);
