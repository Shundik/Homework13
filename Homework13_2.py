import sqlite3 as sl

connection = sl.connect('auditorium5')
with connection:
    connection.execute("""
        CREATE TABLE  auditorium5 (
            age INTEGER,
            auditorium INTEGER
        );
""")

sql = 'INSERT INTO auditorium5 (age,auditorium) values(?,?)'
data = [
    (30, 315),
    (40, 415)
]

with connection:
    connection.executemany(sql, data)
