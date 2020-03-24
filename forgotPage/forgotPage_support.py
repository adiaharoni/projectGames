import sqlite3
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def xxx(p1):
    global w
    print('forgotPage_support.xxx')
    name = w.username_entry
    username1 = name.get()
    city = w.city_entry
    city1 = city.get()
    birthYear = w.birthYear_entry
    birthYear1 = birthYear.get()
    mothersName = w.motherName_entry
    mothersName1 = mothersName.get()
    print(username1 + " " + city1 + " " + birthYear1 + " " + mothersName1)
    sys.path.append('..\\newRegistrationPage')
    conn = sqlite3.connect('user24.db')
    cursor = conn.execute(
    "SELECT * from USERS where username= '"+username1+ "' and city= '"+city1+"' and birthYear= '"+birthYear1+"' and mothersName= '"+mothersName1+"'")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("not in db! you should re-register")
    else:
        cursor = conn.execute("SELECT * from users")
        for row in cursor:
            print("password = ", row[1], "\n")
    conn.commit()
    conn.close()
    sys.stdout.flush()

def backMenuPage():
    sys.stdout.flush()
    destroy_window()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import forgotPage
    forgotPage.vp_start_gui()




