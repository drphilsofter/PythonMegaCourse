# goes over deleting and updating data in a database

import sqlite3

# 1. Open the connection to the databases
cnn = sqlite3.connect("sqlite3_intro.db")

# 2. create a cursor object
db_cursor = cnn.cursor()

# 3. write a SQL statement
# this statement wont generate an error if this entry doesn't exist / was already deleted
def delete_flash(name):
    db_cursor.execute("DELETE FROM superheros WHERE name = (?)", (name,))
    
# because The Flash sucks
delete_flash('The Flash')

# update multiple values in the table at once
def update_superpower_weight(name, power, weight):
    db_cursor.execute("UPDATE superheros SET superpower = (?), weight = (?) WHERE name = (?)", (power,weight,name))

# the update function call
update_superpower_weight('Superman', 'Super strength, has weird top lip', '300')

# 4. Commit the changes to the databases
cnn.commit()

# 5. Close the database connection
cnn.close()