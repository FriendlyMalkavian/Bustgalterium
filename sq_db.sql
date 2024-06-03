PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT, 
title text NOT NULL, 
url text NOT NULL
);

CREATE TABLE IF NOT EXISTS pages (
id integer PRIMARY KEY AUTOINCREMENT, 
title text NOT NULL, 
url text NOT NULL,
menuId integer,
FOREIGN KEY (menuId) REFERENCES mainmenu(id) 
);