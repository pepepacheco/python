DROP TABLE IF EXISTS persona;

CREATE TABLE persona (
        id INTEGER PRIMARY KEY,
        firstName TEXT,
        lastName  TEXT,
        email     TEXT,
        gender    TEXT,
        date      DATETIME
);
