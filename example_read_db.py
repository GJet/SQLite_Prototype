import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()


# Never do this -- insecure!
#symbol = 'RHAT'
#c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
#t = ('RHAT',)
#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
#print(c.fetchone())

for row in c.execute('SELECT * FROM variables ORDER BY var_name'):
        print(str(row[0]) + " = " + str(row[3]))
print("Done")
conn.close()