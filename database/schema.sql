CREATE TABLE stops(
	id INTEGER PRIMARY_KEY,
	on_street VARCHAR(20),
	cross_street VARCHAR(20),
	extra_info VARCHAR(30),
	latitude REAL,
	longitude REAL
);

CREATE TABLE boardings(
	id INTEGER PRIMARY_KEY,
	stop_id INTEGER,
	boardings REAL,
	alightings REAL,
	FOREIGN KEY(stop_id) REFERENCES stops(id)
);

CREATE TABLE stop_routes (
	id INTEGER PRIMARY_KEY,
	stop_id INTEGER,
	route CHAR(5),
	FOREIGN KEY(stop_id) REFERENCES stops(id)
);