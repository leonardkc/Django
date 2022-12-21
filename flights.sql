CREATE TABLE flights (
    id INTEGER PRIMARY KEY,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (id, origin, destination, duration) VALUES ("1", "New York", "London", 419);
INSERT INTO flights (id, origin, destination, duration) VALUES ("2", "Istanbul", "Tokyo", 459);
INSERT INTO flights (id, origin, destination, duration) VALUES ("3", "Nigeria", "Paris", 245);
INSERT INTO flights (id, origin, destination, duration) VALUES ("7", "Shanghai", "France", 700);
INSERT INTO flights (id, origin, destination, duration) VALUES ("8", "Lima", "New York", 419);
INSERT INTO flights (id, origin, destination, duration) VALUES ("9","Spain", "Morroco", 419);
SELECT * FROM flights;