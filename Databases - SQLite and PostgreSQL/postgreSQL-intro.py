# most postgreSQL code is the same as SQLite3 code, with some slight changes
# the library we import is psycopg2 
import psycopg2

# one difference between SQLite and postgreSQL databases is that 
# the database for postgreSQL is not stored in a .db file. 
# instead, it is a database embedded in the postgreSQL installation. 
# There needs to be an already-existing database in the installation.
# (we can still create tables from a python file)
# The installation comes with a default database, 'postgres', 
# or a database can be created with the pgAdmin tool
# I've created an empty database called superheros. 

# make the connection
# all these parameters must be passed to get a secure connection to the database
cnn = psycopg2.connect("dbname = 'superheros' user = 'postgres' password = 'ethernet69' host = 'localhost' port = '5432'")

# create a cursor
csr = cnn.cursor()

# execute the command to create a table in the superheros database
csr.execute("CREATE TABLE IF NOT EXISTS supervillains (name TEXT, age INTEGER, superpower TEXT, lairLocation TEXT, lairCoords INTEGER)")

def insert_villain(name, age, power, lairLoc, lairCoords):
    # the following method of using string formatting to insert entries into the databases
    # can be prone to SQL injection attacks, and it is safest not to use this method. 
    # csr.execute("INSERT INTO supervillains (name, age, superpower, lairLocation, lairCoords) VALUES ('%s', '%s', '%s', '%s', '%s')" % (name, age, power, lairLoc, lairCoords))
    
    # the better way of doing this is this way
    csr.execute("INSERT INTO supervillains (name, age, superpower, lairLocation, lairCoords) VALUES (%s, %s, %s, %s, %s)", (name, age, power, lairLoc, lairCoords))

# insert_villain('The Joker', 40, 'Is insane', 'Clown Cave', 299)

# we can also view output from a table. Duh. 
def view_table(name):
    csr.execute("SELECT * FROM supervillains WHERE name = %s", (name,))
    the_entry = csr.fetchall()
    return the_entry

# print(view_table('The Joker'))

# and now the delete function
def delete_entry(name):
    csr.execute("DELETE FROM supervillains WHERE name = %s", (name,))
    rowcount = csr.rowcount
    return str(rowcount)

# print("The number of entries deleted was " + delete_entry("The Joker"))

def update_entry(name, superpower):
    csr.execute("UPDATE supervillains SET superpower = %s WHERE name = %s", (superpower,name))
    rowcount = csr.rowcount
    if rowcount > 0:
        return "Change successful"
    else:
        return "No change made"

# print(update_entry('The Joker', 'What a joking jokey joker'))

# commit the changes
cnn.commit()

# close the database connection
cnn.close()