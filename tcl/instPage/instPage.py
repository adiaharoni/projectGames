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

sys.path.append('..\menuPage')
import instPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    instPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    instPage_support.init(w, top, *args, **kwargs)
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
        font11 = "-family {Tw Cen MT} -size 48 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Segoe UI} -size 13 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font18 = "-family {Tw Cen MT} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("699x495+639+362")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.057, rely=0.101, relheight=0.798
                , relwidth=0.794)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ff8080")

        self.inst_label = tk.Label(self.Frame1)
        self.inst_label.place(relx=0.198, rely=0.051, height=51, width=344)
        self.inst_label.configure(activeforeground="#ffffff")
        self.inst_label.configure(background="#ff8080")
        self.inst_label.configure(disabledforeground="#a3a3a3")
        self.inst_label.configure(font=font11)
        self.inst_label.configure(foreground="#ffffff")
        self.inst_label.configure(text='''Instructions:''')

        self.inst_biglabel = ttk.Label(self.Frame1)
        self.inst_biglabel.place(relx=0.018, rely=0.253, height=239, width=556)
        self.inst_biglabel.configure(background="#ff8080")
        self.inst_biglabel.configure(foreground="#ffffff")
        self.inst_biglabel.configure(font=font16)
        self.inst_biglabel.configure(relief="flat")
        self.inst_biglabel.configure(text='''In order to start playing, you should login to your profile
with your username and password.
Then, you should choose a play-"X/O" or "four in a row" and wait
for another player. 
If after a minute nobody enters, you can switch to the second play.
In the end of the game you will score points to your profile:
If you win the game- you will score 10 points, 
If it is a tie- you will score 5 points 
and if you lose, you won't score any points.
Good luck!!''')

        self.return_button = tk.Button(self.Frame1)
        self.return_button.place(relx=0.703, rely=0.785, height=64, width=127)
        self.return_button.configure(activebackground="#ececec")
        self.return_button.configure(activeforeground="#000000")
        self.return_button.configure(background="#ff8080")
        self.return_button.configure(command=instPage_support.backMenuPage)
        self.return_button.configure(disabledforeground="#a3a3a3")
        self.return_button.configure(font=font18)
        self.return_button.configure(foreground="#ffffff")
        self.return_button.configure(highlightbackground="#ff8080")
        self.return_button.configure(highlightcolor="#ff8080")
        self.return_button.configure(pady="0")
        self.return_button.configure(text='''return''')

if __name__ == '__main__':
    vp_start_gui()





