import sys
import sqlite3
from tkinter import *
import clientBL

def fe_login_res(status_code, status_txt):
    global w
    print('loginRes')
    sys.stdout.flush()
    src = w.Label_error
    src.configure(text=status_txt + " (" + status_code + ")")
    """
    sys.path.append('..\\forgotPage')
    import forgotPage
    forgotPage.create_Toplevel1(root, 'Hello', top_level)"""

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
    password1 = to.get()
    print(username1+" "+password1)
    clientBL.login(fe_login_res, username1, password1)

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





