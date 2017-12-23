import sqlite3

class Database:
    """Define the actions necessary to interact with a database"""
    
    # right here we have the constructor, which will create an object instance of this class when called
    # this function alone is executed when an instance of this class is created. 
    # the other methods must be called by name on a specific object
    def __init__(self):
        self.conn = sqlite3.connect("films.db")
        # we need to create an attribute cur (the cursor for the database connection) 
        # so that it can be used in this object methods. It is no longer a variable, it is an attribute of the class 'Database'
        # this is the line below, self.cur
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, title text, director text, year integer, length integer)")
        self.conn.commit()

    def insert(self,title,director,year,length):
        self.cur.execute("INSERT INTO movie VALUES (NULL,?,?,?,?)",(title,director,year,length))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM movie")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="",director="",year="",length=""):
        self.cur.execute("SELECT * FROM movie WHERE title=? OR director=? OR year=? OR length=?", (title,director,year,length))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM movie WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,title,director,year,length):
        self.cur.execute("UPDATE movie SET title=?, director=?, year=?, length=? WHERE id=?",(title,director,year,length,id))
        self.conn.commit()
        
    def close_connection(self):
        self.conn.close()
        
    # another special method for an object class, like __init__
    # but basically does the opposite. It is a destructor
    # this method is called on an object instance when the file that created the object is closed
    def __del__(self):
        self.conn.close()