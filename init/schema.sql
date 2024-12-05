CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    created_at TEXT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (name, username, password)
VALUES
    ('John Doe', 'johndoe', '123456'),
    ('Jane Doe', 'janedoe', '123456');

INSERT INTO requests (description, created_at, user_id)
VALUES
    ('Request 1', '2021-01-01 00:00:00', 1),
    ('Request 2', '2021-01-02 00:00:00', 1),
    ('Request 3', '2021-01-03 00:00:00', 2),
    ('Request 4', '2021-01-04 00:00:00', 2);
