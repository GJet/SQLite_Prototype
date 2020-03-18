import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

while 1:
    user_command = input("Enter a command. (? to list commands)")

    if user_command == "?":
        print("    Here are the options")
        print("    list_all")
        print("    lookup <variable_name>")
        print("    find <partial_name>")
        print("    exit")

    if user_command == "list_all":
        for row in c.execute('SELECT * FROM variables ORDER BY var_name'):
            print(str(row[0]) + " = " + str(row[3]))
    if user_command == "exit":
        conn.close()
        break
