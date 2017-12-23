# this file goes over some basic SQLite commands, including opening a connection,
# writing and executing SQLite3 commands, different ways of adding to a database,
# and a function to remove duplicate entries in a database

import sqlite3

# 1. Open the connection to the databases
cnn = sqlite3.connect("sqlite3_intro.db")
# if there isn't already a database of this name, one will be created. 

# 2. create a cursor object
db_cursor = cnn.cursor()
# cursor is a method of the connection object

# 3. write a SQL statement
# SQL code is passed as a string argument to the execute method of the cursor object
# first, we'll create a table to write to 
db_cursor.execute("CREATE TABLE IF NOT EXISTS superheros (name TEXT, alter_ego TEXT, age INTEGER, superpower TEXT, weight FLOAT)")
# this creates a table called 'superheros' with the columns name, alter-ego, age, superpower and weight

# we continue to work with the database, making as many changes as we like.
# we can split the SQL command and the execution into two steps
command1 = "INSERT INTO superheros (name, alter_ego, age, superpower, weight) VALUES ('Superman', 'Clark Kent', 30, 'Super strength', 80)"
db_cursor.execute(command1)

# we can use a function to generalise the process of inserting rows into the databases
def insert_data(name, alter_ego, age, power, weight):
    command2 = "INSERT INTO superheros (name, alter_ego, age, superpower, weight) VALUES (?,?,?,?,?)"
    db_cursor.execute(command2, (name, alter_ego, age, power, weight))

insert_data('Wonder Woman', 'Diana Prince', 10000, 'Womanhood', 75)

# we can view the contents of the database
def view_database():
    db_cursor.execute("SELECT * FROM superheros")
    rows = db_cursor.fetchall()
    return rows

# print(view_database())

# we can use the executemany method to power through a bunch of SQL statements
many_heros = [('The Flash', 'Barry Allen', 22, 'Very fast', 60),
              ('Batman', 'Bruce Wayne', 40, 'He is rich', 80),
              ('Spiderman', 'Peter Parker', 21, 'Spidey Senses', 68),
              ('Iron Man', 'Tony Stark', 38, 'Also rich, like Batman', 80)]

db_cursor.executemany('INSERT INTO superheros (name, alter_ego, age, superpower, weight) VALUES (?,?,?,?,?)', many_heros)

# look for duplicates, using the id column as the unique identifier
def remove_duplicates():
    # create empty lists to store one entry of each unique name,
    # and the ID of subsequent duplicate names
    name_list = []
    dup_id_list = []
    # get all the names from superhero database
    db_cursor.execute("SELECT name, id FROM superheros")
    # get all names in the datatbase
    name_list_all = db_cursor.fetchall()
    
    # print(name_list_all)
    
    for name in name_list_all:
        if name[0] not in name_list:
            name_list.append(name[0])
        else:
            dup_id_list.append(name[1])
    
    for i in range(len(dup_id_list)):
        db_cursor.execute("DELETE FROM superheros WHERE id = (?)", (dup_id_list[i],))
        # it turns out the comma there at the end of name_id riiiiiiiiiiight here ^ is very important in the above statement
        # it turns this int into a tuple of length 1.
    
remove_duplicates()

# 4. Commit the changes to the databases
cnn.commit()

# 5. Close the database connection
cnn.close()