PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS Cookies;

DROP TABLE IF EXISTS Users;

CREATE TABLE Users(
  id          INTEGER      PRIMARY KEY AUTOINCREMENT,
  name        TEXT         NOT NULL UNIQUE,
  created     TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Cookies(
    id      INTEGER        PRIMARY KEY AUTOINCREMENT,
    owner   INTEGER        NOT NULL,
    type    TEXT           NOT NULL DEFAULT 'Zimtstern',
    FOREIGN KEY(owner) REFERENCES Users(id) On DELETE CASCADE
);
