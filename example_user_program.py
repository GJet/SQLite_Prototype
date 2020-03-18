import sqlite3
import os


# define our clear function
#TODO: Clear() function doesn't seem to be working
def clear():
    # for windows

    if os.name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


#Start of program
conn = sqlite3.connect('database.db')
c = conn.cursor()

while 1:
    user_command = input("Enter a command. (? to list commands)")

    if user_command == "?":
        clear()
        print("Here are the options:")
        print("    list_all")
        print("    lookup <variable_name>")
        print("    find <partial_name>")
        print("    exit")
        clear()

    elif user_command == "list_all":
        clear()
        for row in c.execute('SELECT * FROM variables ORDER BY var_name'):
            print(str(row[0]) + " = " + str(row[3]))

    elif "find" in user_command:
        clear()
        split_command = user_command.split()
        if len(split_command) > 1:
            for row in c.execute('SELECT * FROM variables ORDER BY var_name'):
                if split_command[1] in row[0]:
                    print(row)
        else:
            print("find command syntax error.  Try again.")


    elif user_command == "exit":
        clear()
        conn.close()
        break

    else:
        clear()
        print("We didn't understand your request. Try again")
