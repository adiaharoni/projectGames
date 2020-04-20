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
        font10 = "-family {Tw Cen MT} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("659x450+804+312")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.046, rely=0.044, relheight=0.896
                , relwidth=0.873)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#b366ff")
        self.Frame1.configure(highlightbackground="#690f96")
        self.Frame1.configure(highlightcolor="#690f96")

        self.instruction = ttk.Label(self.Frame1)
        self.instruction.place(relx=0.07, rely=0.298, height=59, width=466)
        self.instruction.configure(background="#b366ff")
        self.instruction.configure(foreground="#ffffff")
        self.instruction.configure(font="-family {Tw Cen MT} -size 16 -weight bold")
        self.instruction.configure(relief="flat")
        self.instruction.configure(text='''Enter your username and your password:''')

        self.entry_username = tk.Entry(self.Frame1)
        self.entry_username.place(relx=0.313, rely=0.471, height=30, relwidth=0.303)
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
        self.login.place(relx=0.73, rely=0.819, height=54, width=127)
        self.login.configure(activebackground="#ececec")
        self.login.configure(activeforeground="#000000")
        self.login.configure(background="#ffffff")
        self.login.configure(disabledforeground="#a3a3a3")
        self.login.configure(font="-family {Tw Cen MT} -size 19 -weight bold")
        self.login.configure(foreground="#b366ff")
        self.login.configure(highlightbackground="#d9d9d9")
        self.login.configure(highlightcolor="black")
        self.login.configure(pady="0")
        self.login.configure(text='''login''')
        self.login.bind('<Button-1>', lambda e: entryPage_support.xxx(e))

        self.Label_username = tk.Label(self.Frame1)
        self.Label_username.place(relx=0.087, rely=0.471, height=31, width=84)
        self.Label_username.configure(activebackground="#690f96")
        self.Label_username.configure(activeforeground="white")
        self.Label_username.configure(activeforeground="#000000")
        self.Label_username.configure(background="#b366ff")
        self.Label_username.configure(disabledforeground="#a3a3a3")
        self.Label_username.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.Label_username.configure(foreground="#ffffff")
        self.Label_username.configure(highlightbackground="#d9d9d9")
        self.Label_username.configure(highlightcolor="black")
        self.Label_username.configure(text='''username''')

        self.Label_error = tk.Label(self.Frame1)
        self.Label_error.place(relx=0.087, rely=0.75, height=31, width=350)
        self.Label_error.configure(activebackground="#690f96")
        self.Label_error.configure(activeforeground="white")
        self.Label_error.configure(activeforeground="#000000")
        self.Label_error.configure(background="#b366ff")
        self.Label_error.configure(disabledforeground="#a3a3a3")
        self.Label_error.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.Label_error.configure(foreground="red")
        self.Label_error.configure(highlightbackground="#d9d9d9")
        self.Label_error.configure(highlightcolor="black")
        self.Label_error.configure(text="")

        self.entry_password = tk.Entry(self.Frame1)
        self.entry_password.place(relx=0.313, rely=0.62, height=30, relwidth=0.303)
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
        self.Label_password.place(relx=0.087, rely=0.62, height=31, width=84)
        self.Label_password.configure(activebackground="#f9f9f9")
        self.Label_password.configure(activeforeground="black")
        self.Label_password.configure(background="#b366ff")
        self.Label_password.configure(disabledforeground="#a3a3a3")
        self.Label_password.configure(font="-family {Tw Cen MT} -size 14 -weight bold")
        self.Label_password.configure(foreground="#ffffff")
        self.Label_password.configure(highlightbackground="#d9d9d9")
        self.Label_password.configure(highlightcolor="black")
        self.Label_password.configure(text='''password''')

        self.button_newRegister = tk.Button(self.Frame1)
        self.button_newRegister.place(relx=0.052, rely=0.819, height=54, width=147)
        self.button_newRegister.configure(activebackground="#ececec")
        self.button_newRegister.configure(activeforeground="#000000")
        self.button_newRegister.configure(background="#ffffff")
        self.button_newRegister.configure(command=entryPage_support.startNewRegistrationPage)
        self.button_newRegister.configure(disabledforeground="#a3a3a3")
        self.button_newRegister.configure(font="-family {Tw Cen MT} -size 19 -weight bold")
        self.button_newRegister.configure(foreground="#b366ff")
        self.button_newRegister.configure(highlightbackground="#d9d9d9")
        self.button_newRegister.configure(highlightcolor="black")
        self.button_newRegister.configure(pady="0")
        self.button_newRegister.configure(text='''new register''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.278, rely=0.124, height=61, width=274)
        self.Label1.configure(activebackground="#f0f0f0f0f0f0")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#b366ff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Tw Cen MT} -size 40 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Login''')

        self.button_forgot = tk.Button(self.Frame1)
        self.button_forgot.place(relx=0.365, rely=0.819, height=54, width=177)
        self.button_forgot.configure(activebackground="#ececec")
        self.button_forgot.configure(activeforeground="#000000")
        self.button_forgot.configure(background="#ffffff")
        self.button_forgot.configure(command=entryPage_support.startforgotPage)
        self.button_forgot.configure(disabledforeground="#a3a3a3")
        self.button_forgot.configure(font=font10)
        self.button_forgot.configure(foreground="#b366ff")
        self.button_forgot.configure(highlightbackground="#d9d9d9")
        self.button_forgot.configure(highlightcolor="#000000")
        self.button_forgot.configure(pady="0")
        self.button_forgot.configure(text='''forgot your password?''')

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="-family {Segoe UI} -size 9")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event, *args, **kwargs):
        Popupmenu2 = tk.Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#f9f9f9")
        Popupmenu2.configure(activeborderwidth="1")
        Popupmenu2.configure(activeforeground="black")
        Popupmenu2.configure(background="#c9e1e9")
        Popupmenu2.configure(borderwidth="1")
        Popupmenu2.configure(disabledforeground="#a3a3a3")
        Popupmenu2.configure(font="-family {Segoe UI} -size 9")
        Popupmenu2.configure(foreground="black")
        Popupmenu2.post(event.x_root, event.y_root)

if __name__ == '__main__':
    vp_start_gui()





