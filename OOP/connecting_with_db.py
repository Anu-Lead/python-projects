import sqlite3

"""Before creating a table we need to create a cursor. A cursor is an object that is used 
to make the connection for executing SQL queries. We’ll use the cursor to create tables, 
insert data, and more. To create a cursor we only need to use the connection we’ve 
created and the .cursor method."""

# create a connection
connection = sqlite3.connect('hospitals.db')
the_cursor = connection.cursor()

the_cursor.executescript("""
DROP TABLE IF EXISTS clinics;
CREATE TABLE clinics (
            name TEXT UNIQUE,
            address TEXT,
            status TEXT
    )""")

# the_cursor.execute("INSERT INTO clinics VALUES ('Yaba General Hospital', '13, Herbert Johnson Road, Lagos', 'Government')")
#
all_clinic = [
    ('St. Mary Maternity Home', '21, Ikorodu Road, Lagos Nigeria', 'Private'),
    ('Thomas Cardiovascular Center', '45, Ikoyi, Lagos', 'Private'),
    ('University College Hospital [UCH]', 'Ibadan Nigeria', 'Government'),
]
the_cursor.executemany("INSERT INTO clinics VALUES (?,?,?)", all_clinic)

the_cursor.execute("SELECT * FROM clinics")
print(the_cursor.fetchall())


connection.commit()
connection.close()

