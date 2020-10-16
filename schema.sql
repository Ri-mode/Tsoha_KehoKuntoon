CREATE TABLE users (
        id SERIAL PRIMARY KEY, 
        usertype INTEGER NOT NULL, 
        username TEXT UNIQUE, 
        password TEXT, 
        targetweight FLOAT,
        height FLOAT, 
        created TIMESTAMP, 
        modified TIMESTAMP,
        visible INTEGER NOT NULL
);

CREATE TABLE weights (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users,
        weight_now FLOAT,
        weight_date DATE,
        created TIMESTAMP, 
        modified TIMESTAMP,
        visible INTEGER NOT NULL
);

CREATE TABLE coaches (
        id SERIAL PRIMARY KEY,
        coach_id INTEGER REFERENCES users,
        trainer_id INTEGER REFERENCES users,
        created TIMESTAMP, 
        modified TIMESTAMP,
        visible INTEGER NOT NULL
);
