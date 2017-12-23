# SQLite and PostgreSQL are different
# SQLite is not a client-server database, it is instead embedded into the actual application
# SQLite data is stored in a file associated with the program
# postgreSQL needs to be installed. It is more useful in a web application.
# python would be the program that grabs the data from the postgreSQL

# need two libraries to interact with these two databases
# for SQLite it's:
import sqlite3

# and for postgreSQL it's:
import psycopg2

# there are 5 basic steps when working with a database:
# 1. Connect to the databases
# 2. Create a cursor object to work with the database. With this cursor you can access table rows
# 3. Write the database query (Create, Read, Update, Delete)
# 4. Commit the changes to the database
# 5. Close the connection

