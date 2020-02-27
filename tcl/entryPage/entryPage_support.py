import sys
import sqlite3
from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def xxx(p1):
    global w
    print('entryPage_support.xxx')
    src = w.entry_username
    username1 = src.get()
    to = w.entry_password
    password1= to.get()
    print(username1+" "+password1)
    conn = sqlite3.connect('user3.db')
    cursor = conn.execute(
    "SELECT * from users where username= '"+username1+ "' and password= '"+password1+"'")
    rows = cursor.fetchall()  
    if len(rows) == 0:
        print("not in db!")
        cursor = conn.execute("INSERT INTO USERS (username,password) \
                                  VALUES ('" + username1 + "', '" + password1 + "' )")
        conn.commit()
        conn.close()
    else:
       print ("is in db!")
    sys.stdout.flush()
    
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
    import entryPage
    entryPage.vp_start_gui()





