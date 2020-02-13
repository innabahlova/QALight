import sqlite3

conn = sqlite3.connect('library_app.sqlite')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE User (
        id INTEGER PRIMARY KEY NOT NULL,
        first_name CHAR(50) NOT NULL,
        last_name CHAR(50) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE Book (
        id INTEGER PRIMARY KEY NOT NULL,
        title CHAR(100) NOT NULL,
        author CHAR(50) NOT NULL,
        year INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE BookRecord (
        id INTEGER PRIMARY KEY NOT NULL,
        user_id INTEGER NOT NULL
            CONSTRAINT fk_user_id REFERENCES User(id),
        book_id INTEGER NOT NULL
            CONSTRAINT fk_book_id REFERENCES Book(id)        
    )
""")

cursor.execute("INSERT INTO User(id,first_name,last_name) VALUES(0,'Lena','Smith')")
cursor.execute("INSERT INTO User(id,first_name,last_name) VALUES(1,'Nicol','Green')")
cursor.execute("INSERT INTO User(id,first_name,last_name) VALUES(2,'Tom','Taylor')")
cursor.execute("INSERT INTO User(id,first_name,last_name) VALUES(3,'Paul','Miller')")

cursor.execute("INSERT INTO Book(id,title,author,year) VALUES(0,'Harry Poter','Rowling I.K.',2017)")
cursor.execute("INSERT INTO Book(id,title,author,year) VALUES(1,'Alchemist','Paulo Coelho',2008)")
cursor.execute("INSERT INTO Book(id,title,author,year) VALUES(2,'The Little Pince','Exupery',2009)")
cursor.execute("INSERT INTO Book(id,title,author,year) VALUES(3,'Sherlock Holmes','A.Conan Doyle',2015)")

cursor.execute("INSERT INTO BookRecord(id,user_id,book_id) VALUES(0,2,1)")
cursor.execute("INSERT INTO BookRecord(id,user_id,book_id) VALUES(1,0,3)")
cursor.execute("INSERT INTO BookRecord(id,user_id,book_id) VALUES(2,1,0)")
cursor.execute("INSERT INTO BookRecord(id,user_id,book_id) VALUES(3,3,2)")

conn.commit()
conn.close()