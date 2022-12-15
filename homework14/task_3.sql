CREATE TABLE "Posts" (
	"id"	INTEGER,
	"title"	TEXT,
	"data_create"	TEXT,
	"content"	TEXT(140),
	"post_author_id"	INTEGER,
	"post_category_id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO Posts(title, data_create, content, post_author_id, post_category_id)
VALUES('What is Quantum Computing?', '2021-01-18', 'Quantum computing is a rapidly-emerging technology that harnesses the laws of quantum mechanics to solve problems too complex for classical computers',
1,1);
INSERT INTO Posts(title, data_create, content, post_author_id, post_category_id)
VALUES('What is Quantum Computing?', '2021-01-18', 'Quantum computing is a rapidly-emerging technology that harnesses the laws of quantum mechanics to solve problems too complex for classical computers',
1,1);
INSERT INTO Posts(title, data_create, content, post_author_id, post_category_id)
VALUES('What is Quantum Computing?', '2021-01-18', 'Quantum computing is a rapidly-emerging technology that harnesses the laws of quantum mechanics to solve problems too complex for classical computers',
1,1);