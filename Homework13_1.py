import sqlite3 as sl

connection = sl.connect('Students2')
with connection:
    connection.execute("""
        CREATE TABLE  students2 (
            name TEXT,
            surname TEXT
        );
""")

sql = 'INSERT INTO students2 (name, surname) values(?, ?)'
data = [
    ('Alice', 'Lauren'),
    ('Bob', 'Laurin')
]

with connection:
    connection.executemany(sql, data)

