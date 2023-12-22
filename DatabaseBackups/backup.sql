PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR, 
	password VARCHAR, 
	email VARCHAR, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
CREATE TABLE storage_places (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	description TEXT, 
	image VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO storage_places VALUES(1,'sp2','nowhere','some_image_name');
INSERT INTO storage_places VALUES(2,'sp3','nowhere','some_image_name');
INSERT INTO storage_places VALUES(3,'tst','desc','pth');
CREATE TABLE storage_grids (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	description TEXT, 
	row_count INTEGER NOT NULL, 
	column_count INTEGER NOT NULL, 
	image VARCHAR, 
	storage_place_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(storage_place_id) REFERENCES storage_places (id)
);
INSERT INTO storage_grids VALUES(1,'left wall','Its just there on the left',2,3,'image of a wall i guess',1);
INSERT INTO storage_grids VALUES(2,'right wall','Its just there on the right',1,1,'image of a wall i guess',1);
INSERT INTO storage_grids VALUES(3,'right wall','Its just there on the right',2,1,'image of a wall i guess',2);
INSERT INTO storage_grids VALUES(4,'tes','desctst',5,3,'fsdfds',3);
CREATE TABLE storage_units (
	id INTEGER NOT NULL, 
	name VARCHAR NOT NULL, 
	description TEXT, 
	image VARCHAR, 
	storage_place_id INTEGER, 
	storage_grid_id INTEGER, 
	storage_grid_row INTEGER NOT NULL, 
	storage_grid_column INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(storage_place_id) REFERENCES storage_places (id), 
	FOREIGN KEY(storage_grid_id) REFERENCES storage_grids (id)
);
INSERT INTO storage_units VALUES(1,'Box 123','Small storage box','/path/to/box_image.jpg',1,1,2,3);
INSERT INTO storage_units VALUES(2,'Box 009','Small storage box','/path/to/box__image.jpg',1,2,2,3);
INSERT INTO storage_units VALUES(3,'Box 009','Small storage box','/path/to/box__image.jpg',2,3,1,1);
INSERT INTO storage_units VALUES(4,'Duck','A very special duck','DobaldDuck.png',3,4,2,2);
COMMIT;
