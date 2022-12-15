CREATE TABLE "user" (
	"Id"	INTEGER PRIMARY KEY,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"gender"	TEXT,
	"login"	TEXT,
	"email"	TEXT,
	"register_date"	INTEGER,
	PRIMARY KEY("Id" AUTOINCREMENT)
);

INSERT INTO user (first_name, last_name, gender, login, email, register_date)
VALUES('Dan','Smith','Male','Tim_2984','smith_is_here@gmail.com', 2010-12-21);
INSERT INTO user (first_name, last_name, gender, login, email, register_date)
VALUES('Tim','Smith','Male','Tim_2984','smith_is_here@gmail.com', 2010-12-21);
INSERT INTO user (first_name, last_name, gender, login, email, register_date)
VALUES('Denis','Smith','Male','Tim_2984','smith_is_here@gmail.com', 2010-12-21);