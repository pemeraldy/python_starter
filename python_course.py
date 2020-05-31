import sqlite3 as lite

# functionality goes here
class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect('course.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT AVAILABLE course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Bad Connection")
    
    #TODO: create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data
                )
        except Exception:
            return False

    #TODO: read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False
            

    #TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
        except Exception:
            return False 

# TODO: Provide UI to users