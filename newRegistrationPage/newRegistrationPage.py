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

import newRegistrationPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    newRegistrationPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    newRegistrationPage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x434+535+232")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.067, rely=0.044, relheight=0.896, relwidth=0.872)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#efb7fb")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.new_label = tk.Label(self.Frame1)
        self.new_label.place(relx=0.134, rely=0.051, height=51, width=344)
        self.new_label.configure(activebackground="#f9f9f9")
        self.new_label.configure(activeforeground="black")
        self.new_label.configure(background="#efb7fb")
        self.new_label.configure(disabledforeground="#a3a3a3")
        self.new_label.configure(font="-family {Tw Cen MT} -size 30 -weight bold")
        self.new_label.configure(foreground="#ffffff")
        self.new_label.configure(highlightbackground="#d9d9d9")
        self.new_label.configure(highlightcolor="black")
        self.new_label.configure(text='''New Registration''')

        self.error_label = tk.Label(self.Frame1)
        self.error_label.place(relx=0.0, rely=0.75, height=30, width=500)
        self.error_label.configure(activebackground="#f9f9f9")
        self.error_label.configure(activeforeground="black")
        self.error_label.configure(background="#efb7fb")
        self.error_label.configure(disabledforeground="#a3a3a3")
        self.error_label.configure(font="-family {Tw Cen MT} -size 12 -weight bold")
        self.error_label.configure(foreground="red")
        self.error_label.configure(highlightbackground="#d9d9d9")
        self.error_label.configure(highlightcolor="black")
        self.error_label.configure(text="")

        self.password_entry = tk.Entry(self.Frame1)
        self.password_entry.place(relx=0.325, rely=0.396, height=20, relwidth=0.409)
        self.password_entry.configure(background="white")
        self.password_entry.configure(disabledforeground="#a3a3a3")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(foreground="#000000")
        self.password_entry.configure(highlightbackground="#d9d9d9")
        self.password_entry.configure(highlightcolor="black")
        self.password_entry.configure(insertbackground="black")
        self.password_entry.configure(selectbackground="#c4c4c4")
        self.password_entry.configure(selectforeground="black")

        self.city_entry = tk.Entry(self.Frame1)
        self.city_entry.place(relx=0.325, rely=0.488,height=20, relwidth=0.409)
        self.city_entry.configure(background="white")
        self.city_entry.configure(disabledforeground="#a3a3a3")
        self.city_entry.configure(font="TkFixedFont")
        self.city_entry.configure(foreground="#000000")
        self.city_entry.configure(highlightbackground="#d9d9d9")
        self.city_entry.configure(highlightcolor="black")
        self.city_entry.configure(insertbackground="black")
        self.city_entry.configure(selectbackground="#c4c4c4")
        self.city_entry.configure(selectforeground="black")

        self.birthYear_entry = tk.Entry(self.Frame1)
        self.birthYear_entry.place(relx=0.325, rely=0.591, height=20, relwidth=0.409)
        self.birthYear_entry.configure(background="white")
        self.birthYear_entry.configure(disabledforeground="#a3a3a3")
        self.birthYear_entry.configure(font="TkFixedFont")
        self.birthYear_entry.configure(foreground="#000000")
        self.birthYear_entry.configure(highlightbackground="#d9d9d9")
        self.birthYear_entry.configure(highlightcolor="black")
        self.birthYear_entry.configure(insertbackground="black")
        self.birthYear_entry.configure(selectbackground="#c4c4c4")
        self.birthYear_entry.configure(selectforeground="black")

        self.motherName_entry = tk.Entry(self.Frame1)
        self.motherName_entry.place(relx=0.325, rely=0.694, height=20, relwidth=0.409)
        self.motherName_entry.configure(background="white")
        self.motherName_entry.configure(disabledforeground="#a3a3a3")
        self.motherName_entry.configure(font="TkFixedFont")
        self.motherName_entry.configure(foreground="#000000")
        self.motherName_entry.configure(highlightbackground="#d9d9d9")
        self.motherName_entry.configure(highlightcolor="black")
        self.motherName_entry.configure(insertbackground="black")
        self.motherName_entry.configure(selectbackground="#c4c4c4")
        self.motherName_entry.configure(selectforeground="black")

        self.inst_label = tk.Label(self.Frame1)
        self.inst_label.place(relx=0.038, rely=0.18, height=41, width=214)
        self.inst_label.configure(activebackground="#f9f9f9")
        self.inst_label.configure(activeforeground="black")
        self.inst_label.configure(background="#efb7fb")
        self.inst_label.configure(disabledforeground="#a3a3a3")
        self.inst_label.configure(font="-family {Tw Cen MT} -size 17 -weight bold")
        self.inst_label.configure(foreground="#ffffff")
        self.inst_label.configure(highlightbackground="#d9d9d9")
        self.inst_label.configure(highlightcolor="black")
        self.inst_label.configure(text='''fill in your details:''')

        self.username_entry = tk.Entry(self.Frame1)
        self.username_entry.place(relx=0.325, rely=0.308, height=20, relwidth=0.409)
        self.username_entry.configure(background="white")
        self.username_entry.configure(disabledforeground="#a3a3a3")
        self.username_entry.configure(font="TkFixedFont")
        self.username_entry.configure(foreground="#000000")
        self.username_entry.configure(highlightbackground="#d9d9d9")
        self.username_entry.configure(highlightcolor="black")
        self.username_entry.configure(insertbackground="black")
        self.username_entry.configure(selectbackground="#c4c4c4")
        self.username_entry.configure(selectforeground="black")

        self.username_label = tk.Label(self.Frame1)
        self.username_label.place(relx=0.076, rely=0.308, height=21, width=94)
        self.username_label.configure(activebackground="#f9f9f9")
        self.username_label.configure(activeforeground="black")
        self.username_label.configure(background="#efb7fb")
        self.username_label.configure(disabledforeground="#a3a3a3")
        self.username_label.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.username_label.configure(foreground="#ffffff")
        self.username_label.configure(highlightbackground="#d9d9d9")
        self.username_label.configure(highlightcolor="black")
        self.username_label.configure(text='''username''')

        self.password_label = tk.Label(self.Frame1)
        self.password_label.place(relx=0.076, rely=0.393, height=21, width=94)
        self.password_label.configure(activebackground="#f9f9f9")
        self.password_label.configure(activeforeground="black")
        self.password_label.configure(background="#efb7fb")
        self.password_label.configure(disabledforeground="#a3a3a3")
        self.password_label.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.password_label.configure(foreground="#ffffff")
        self.password_label.configure(highlightbackground="#d9d9d9")
        self.password_label.configure(highlightcolor="black")
        self.password_label.configure(text='''password''')

        self.city_label = tk.Label(self.Frame1)
        self.city_label.place(relx=0.076, rely=0.481, height=21, width=94)
        self.city_label.configure(activebackground="#f9f9f9")
        self.city_label.configure(activeforeground="black")
        self.city_label.configure(background="#efb7fb")
        self.city_label.configure(disabledforeground="#a3a3a3")
        self.city_label.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.city_label.configure(foreground="#ffffff")
        self.city_label.configure(highlightbackground="#d9d9d9")
        self.city_label.configure(highlightcolor="black")
        self.city_label.configure(text='''city''')

        self.birthYear_label = tk.Label(self.Frame1)
        self.birthYear_label.place(relx=0.076, rely=0.581, height=21, width=94)
        self.birthYear_label.configure(activebackground="#f9f9f9")
        self.birthYear_label.configure(activeforeground="black")
        self.birthYear_label.configure(background="#efb7fb")
        self.birthYear_label.configure(disabledforeground="#a3a3a3")
        self.birthYear_label.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.birthYear_label.configure(foreground="#ffffff")
        self.birthYear_label.configure(highlightbackground="#d9d9d9")
        self.birthYear_label.configure(highlightcolor="black")
        self.birthYear_label.configure(text='''birth year''')

        self.motherName_label = tk.Label(self.Frame1)
        self.motherName_label.place(relx=0.057, rely=0.668, height=21, width=124)
        self.motherName_label.configure(activebackground="#f9f9f9")
        self.motherName_label.configure(activeforeground="black")
        self.motherName_label.configure(background="#efb7fb")
        self.motherName_label.configure(disabledforeground="#a3a3a3")
        self.motherName_label.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.motherName_label.configure(foreground="#ffffff")
        self.motherName_label.configure(highlightbackground="#d9d9d9")
        self.motherName_label.configure(highlightcolor="black")
        self.motherName_label.configure(text='''mother's name''')

        self.return_button = tk.Button(self.Frame1)
        self.return_button.place(relx=0.057, rely=0.88, height=44, width=87)
        self.return_button.configure(activebackground="#ececec")
        self.return_button.configure(activeforeground="#000000")
        self.return_button.configure(background="#ffffff")
        self.return_button.configure(command=newRegistrationPage_support.backEntryPage)
        self.return_button.configure(disabledforeground="#a3a3a3")
        self.return_button.configure(font="-family {Tw Cen MT} -size 16 -weight bold")
        self.return_button.configure(foreground="#efb7fb")
        self.return_button.configure(highlightbackground="#d9d9d9")
        self.return_button.configure(highlightcolor="black")
        self.return_button.configure(pady="0")
        self.return_button.configure(text='''return''')

        self.finish_button = tk.Button(self.Frame1)
        self.finish_button.place(relx=0.784, rely=0.88, height=44, width=87)
        self.finish_button.configure(activebackground="#ececec")
        self.finish_button.configure(activeforeground="#000000")
        self.finish_button.configure(background="#ffffff")
        self.finish_button.configure(disabledforeground="#a3a3a3")
        self.finish_button.configure(font="-family {Tw Cen MT} -size 16 -weight bold")
        self.finish_button.configure(foreground="#efb7fb")
        self.finish_button.configure(highlightbackground="#d9d9d9")
        self.finish_button.configure(highlightcolor="black")
        self.finish_button.configure(pady="0")
        self.finish_button.configure(text='''finish''')
        self.finish_button.bind('<Button-1>', lambda e: newRegistrationPage_support.register(e))

if __name__ == '__main__':
    vp_start_gui()





