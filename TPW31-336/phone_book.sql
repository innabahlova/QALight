create table phone_book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name CHAR(50),
    second_name CHAR(50),
    third_name CHAR(50),
    phone CHAR(20) NOT NULL,
    coment CHAR(200)
);