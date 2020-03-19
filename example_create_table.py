import sqlite3
import os

db_name = 'database.db'

if os.path.isfile(db_name):
    print("Datbase Already Exists")
else:
    conn = sqlite3.connect(db_name)

    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE variables
                 (var_name, var_description, var_type, var_value)''')

    # Insert a row of data
    #c.execute("INSERT INTO variables VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    conn.commit()
    # Larger example that inserts many records at a time
    variables = [('TEMP1', 'TEMP at location 1', 'float', 0.0),
                 ('TEMP2', 'Temperature at location 2', 'float', 0.0),
                 ('PRESS1', 'Pressure at location 1', 'float', 0.0),
                 ('PRESS2', 'Pressure at location 2', 'float', 0.0)
                ]
    c.executemany('INSERT INTO variables VALUES (?,?,?,?)', variables)

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()