import sqlite3
import sys
import clientBL

def fe_forgot_password_res(status_code, status_txt, password):
    global w
    print('forgot_password_Res')
    sys.stdout.flush()
    src = w.error_label
    if int(status_code) == 0:
        src.configure(text = "your password: " +password)
    else:
        src.configure(text="error:"+status_txt + " (" + status_code + ")")

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
    clientBL.forgot_password(fe_forgot_password_res, username1, city1, birthYear1, mothersName1)

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




