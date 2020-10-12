CREATE TABLE users (
        id SERIAL PRIMARY KEY, 
        usertype INTEGER NOT NULL, 
        username TEXT UNIQUE, 
        password TEXT, 
        currentweight FLOAT, 
        targetweight FLOAT,
        height FLOAT, 
        created TIMESTAMP, 
        modified TIMESTAMP
);

CREATE TABLE weights (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        weight_now FLOAT,
        fat_now FLOAT,
        muscle_now FLOAT,
        weight_date DATE,
        created TIMESTAMP, 
        modified TIMESTAMP
);
