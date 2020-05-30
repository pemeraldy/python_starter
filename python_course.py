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


# TODO: Provide UI to users