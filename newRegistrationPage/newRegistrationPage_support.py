import sqlite3
import sys
import clientBL

def fe_register_res(status_code, status_txt):
    global w
    print('registerRes')
    sys.stdout.flush()
    src = w.error_label
    src.configure(text=status_txt + " (" + status_code + ")")
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def backEntryPage():
    sys.stdout.flush()
    destroy_window()

def register(p1):
    global w
    print('newRegistrationPage_support.xxx')
    username = w.username_entry.get()
    password = w.password_entry.get()
    city = w.city_entry.get()
    birthYear = w.birthYear_entry.get()
    mothersName = w.motherName_entry.get()
    print(username+" "+password+" "+city+" "+birthYear+" "+mothersName)
    if len(password) < 4:
        src = w.error_label
        src.configure(text="Error: password length <4")
    elif not birthYear.isdigit():
        src = w.error_label
        src.configure(text="Error: Year must be a number between 1900 and 2020")
    elif int(birthYear)< 1900 or int(birthYear)> 2020 : #the year should be between 1900-2020
        src = w.error_label
        src.configure(text="Error: Year must be a number between 1900 and 2020")
    elif username == "" or password == "" or city == "" or birthYear == "" or mothersName == "" or username.isspace() == True or password.isspace() == True or city.isspace() == True or birthYear.isspace() == True or mothersName.isspace() == True:
        src = w.error_label
        src.configure(text="Error: The details cannot be empty")
    else:
        clientBL.register(fe_register_res, username, password, city, birthYear, mothersName)

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
    import newRegistrationPage
    newRegistrationPage.vp_start_gui()




