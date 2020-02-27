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

import entryPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    entryPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    entryPage_support.init(w, top, *args, **kwargs)
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("659x450+591+150")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.182, rely=0.067, relheight=0.878
                , relwidth=0.751)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#b366ff")
        self.Frame1.configure(highlightbackground="#690f96")
        self.Frame1.configure(highlightcolor="#690f96")

        self.instruction = ttk.Label(self.Frame1)
        self.instruction.place(relx=0.081, rely=0.101, height=59, width=416)
        self.instruction.configure(background="#690f96")
        self.instruction.configure(foreground="#ffffff")
        self.instruction.configure(font="-family {Levenim MT} -size 13 -weight bold")
        self.instruction.configure(relief="flat")
        self.instruction.configure(text='''please enter your username and your password''')

        self.entry_username = tk.Entry(self.Frame1)
        self.entry_username.place(relx=0.323, rely=0.354, height=30
                , relwidth=0.352)
        self.entry_username.configure(background="white")
        self.entry_username.configure(disabledforeground="#a3a3a3")
        self.entry_username.configure(font="TkFixedFont")
        self.entry_username.configure(foreground="#000000")
        self.entry_username.configure(highlightbackground="#d9d9d9")
        self.entry_username.configure(highlightcolor="black")
        self.entry_username.configure(insertbackground="black")
        self.entry_username.configure(selectbackground="#c4c4c4")
        self.entry_username.configure(selectforeground="black")

        self.login = tk.Button(self.Frame1)
        self.login.place(relx=0.626, rely=0.734, height=34, width=107)
        self.login.configure(activebackground="#ececec")
        self.login.configure(activeforeground="#000000")
        self.login.configure(background="#690f96")
        self.login.configure(disabledforeground="#a3a3a3")
        self.login.configure(font="-family {Levenim MT} -size 12 -weight bold")
        self.login.configure(foreground="#ffffff")
        self.login.configure(highlightbackground="#d9d9d9")
        self.login.configure(highlightcolor="black")
        self.login.configure(pady="0")
        self.login.configure(text='''Login''')
        self.login.bind('<Button-1>',lambda e:entryPage_support.xxx(e))

        self.Label_username = tk.Label(self.Frame1)
        self.Label_username.place(relx=0.121, rely=0.354, height=31, width=84)
        self.Label_username.configure(activebackground="#690f96")
        self.Label_username.configure(activeforeground="white")
        self.Label_username.configure(activeforeground="#000000")
        self.Label_username.configure(background="#690f96")
        self.Label_username.configure(disabledforeground="#a3a3a3")
        self.Label_username.configure(font="-family {Levenim MT} -size 9 -weight bold")
        self.Label_username.configure(foreground="#ffffff")
        self.Label_username.configure(highlightbackground="#d9d9d9")
        self.Label_username.configure(highlightcolor="black")
        self.Label_username.configure(text='''username''')

        self.entry_password = tk.Entry(self.Frame1)
        self.entry_password.place(relx=0.323, rely=0.506, height=30
                , relwidth=0.352)
        self.entry_password.configure(background="white")
        self.entry_password.configure(disabledforeground="#a3a3a3")
        self.entry_password.configure(font="TkFixedFont")
        self.entry_password.configure(foreground="#000000")
        self.entry_password.configure(highlightbackground="#d9d9d9")
        self.entry_password.configure(highlightcolor="black")
        self.entry_password.configure(insertbackground="black")
        self.entry_password.configure(selectbackground="#c4c4c4")
        self.entry_password.configure(selectforeground="black")

        self.Label_password = tk.Label(self.Frame1)
        self.Label_password.place(relx=0.121, rely=0.506, height=31, width=84)
        self.Label_password.configure(activebackground="#f9f9f9")
        self.Label_password.configure(activeforeground="black")
        self.Label_password.configure(background="#690f96")
        self.Label_password.configure(disabledforeground="#a3a3a3")
        self.Label_password.configure(font="-family {Levenim MT} -size 9 -weight bold")
        self.Label_password.configure(foreground="#ffffff")
        self.Label_password.configure(highlightbackground="#d9d9d9")
        self.Label_password.configure(highlightcolor="black")
        self.Label_password.configure(text='''password''')

if __name__ == '__main__':
    vp_start_gui()





