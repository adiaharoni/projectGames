import sys
import sqlite3
from tkinter import *
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

sys.path.append('..\\')
import clientBL

def fe_login_res(status_code, status_txt):
    global w
    print('loginRes')
    sys.stdout.flush()
    src = w.Label_error
    if status_code == "00":
        sys.stdout.flush()
        sys.path.append('..\\chooseGamePage')
        src.configure(text="")
        # hide this window
        root.withdraw()
        import chooseGamePage
        chooseGamePage.create_Toplevel1(root, 'Hello', top_level)
        chooseGamePage.set_close_callback(abort_user)
        #chooseGamePage.vp_start_gui()
    else:
        src.configure(text=status_txt + " (" + status_code + ")")

def abort_user():
    #show window
    root.update()
    root.deiconify()

def login(p1):
    global w
    print('entryPage_support.xxx')
    username = w.entry_username.get()
    password = w.entry_password.get()
    print(username+" "+password)
    if username == "" or password == "" or username.isspace() is True or password.isspace() is True:
        src = w.Label_error
        src.configure(text="Error: The fills cannot be empty")
    else:
        clientBL.login(fe_login_res, username, password)

def startNewRegistrationPage():
    sys.stdout.flush()
    sys.path.append('..\\newRegistrationPage')
    import newRegistrationPage
    newRegistrationPage.create_Toplevel1(root, 'Hello', top_level)

def startforgotPage():
    sys.stdout.flush()
    sys.path.append('..\\forgotPage')
    import forgotPage
    forgotPage.create_Toplevel1(root, 'Hello', top_level)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    clientBL.init()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import entryPage
    entryPage.vp_start_gui()





