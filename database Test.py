import sqlite3

conn = sqlite3.connect('SQLDatabase.db')

print(conn.execute("SELECT * FROM STATES").fetchall())