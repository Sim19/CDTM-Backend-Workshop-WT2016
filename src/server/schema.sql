PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS Lists;
CREATE TABLE Lists(
        id      INTEGER     PRIMARY KEY,
        title   TEXT        NOT NULL,
        revision INTEGER    NOT NULL DEFAULT 1,
        inbox   INTEGER     NOT NULL DEFAULT 0,
        create  TIMESTAMP   NOT NULL CURRENT_TIMESTAMP
)

DROP TABLE IF EXISTS Tasks;
CREATE TABLE Tasks(
        id      INTEGER     PRIMARy KEY,
        list    INTEGER     NOT NULL,
        title   TEXT        NOT NULL,
        status  TEXT        NOT NULL,
        description TEXT    NOT NULL,
        due     TIMESTAMP   TIMESTAMP,
        revision INTEGER    NOT NULL DEFAULT 1,
        created     TIMESTAMP   CURRENT_TIMESTAMP,
        FOREIGN KEY(list) REFERENCES Lists(id) On DELETE CASCADE
)
