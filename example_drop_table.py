import sqlite3
conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("DROP TABLE variables")

conn.commit()

conn.close()