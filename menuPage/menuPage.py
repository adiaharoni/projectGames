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

import menuPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    menuPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    menuPage_support.init(w, top, *args, **kwargs)
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
        font10 = "-family {Tw Cen MT} -size 40 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("AABox")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.open_frame = tk.Frame(top)
        self.open_frame.place(relx=0.067, rely=0.044, relheight=0.896
                , relwidth=0.872)
        self.open_frame.configure(relief='groove')
        self.open_frame.configure(borderwidth="2")
        self.open_frame.configure(relief="groove")
        self.open_frame.configure(background="#ff62b0")
        self.open_frame.configure(highlightbackground="#d9d9d9")
        self.open_frame.configure(highlightcolor="black")

        self.title_label = tk.Label(self.open_frame)
        self.title_label.place(relx=0.076, rely=0.074, height=71, width=424)
        self.title_label.configure(activebackground="#f9f9f9")
        self.title_label.configure(activeforeground="#000000")
        self.title_label.configure(background="#ff62b0")
        self.title_label.configure(disabledforeground="#a3a3a3")
        self.title_label.configure(font=font10)
        self.title_label.configure(foreground="#ffffff")
        self.title_label.configure(highlightbackground="#d9d9d9")
        self.title_label.configure(highlightcolor="black")
        self.title_label.configure(text='''Choose an option''')

        self.instr_button = tk.Button(self.open_frame)
        self.instr_button.place(relx=0.21, rely=0.323, height=94, width=311)
        self.instr_button.configure(activebackground="#ececec")
        self.instr_button.configure(activeforeground="#ffffff")
        self.instr_button.configure(background="#ffffff")
        self.instr_button.configure(command=menuPage_support.startInstPage)
        self.instr_button.configure(disabledforeground="#a3a3a3")
        self.instr_button.configure(font="-family {Tw Cen MT} -size 22 -weight bold")
        self.instr_button.configure(foreground="#ffb0d8")
        self.instr_button.configure(highlightbackground="#d9d9d9")
        self.instr_button.configure(highlightcolor="#ffffff")
        self.instr_button.configure(pady="0")
        self.instr_button.configure(text='''Instructions''')

        self.login_bottun = tk.Button(self.open_frame)
        self.login_bottun.place(relx=0.21, rely=0.62, height=94, width=307)
        self.login_bottun.configure(activebackground="#ececec")
        self.login_bottun.configure(activeforeground="#000000")
        self.login_bottun.configure(background="#ffffff")
        self.login_bottun.configure(command=menuPage_support.startEntryPage)
        self.login_bottun.configure(disabledforeground="#ffb0d8")
        self.login_bottun.configure(font="-family {Tw Cen MT} -size 22 -weight bold")
        self.login_bottun.configure(foreground="#ffb0d8")
        self.login_bottun.configure(highlightbackground="#d9d9d9")
        self.login_bottun.configure(highlightcolor="black")
        self.login_bottun.configure(pady="0")
        self.login_bottun.configure(text='''Login''')

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





