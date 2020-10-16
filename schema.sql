CREATE TABLE users (
        id SERIAL PRIMARY KEY, 
        usertype INTEGER NOT NULL, 
        username TEXT UNIQUE, 
        password TEXT, 
        targetweight FLOAT,
        height FLOAT, 
        created TIMESTAMP, 
        modified TIMESTAMP
);

CREATE TABLE weights (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users,
        weight_now FLOAT,
        weight_date DATE,
        created TIMESTAMP, 
        modified TIMESTAMP
);
