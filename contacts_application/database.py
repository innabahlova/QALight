import sqlite3


def create(first_name, second_name, phone):
    connection = sqlite3.connect("phone_book.sqlite")
    cursor = connection.cursor()

    cursor.execute(
        "insert into phone_book(first_name,second_name,phone) values(?,?,?)",
        (first_name, second_name, phone)
    )

    cursor.close()
    connection.commit()
    connection.close()
