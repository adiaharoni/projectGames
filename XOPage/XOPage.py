import sys
from tkinter import messagebox

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

import XOPage_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_close)
    top = Toplevel1 (root)
    XOPage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    XOPage_support.init(w, top, *args, **kwargs)
    w.protocol("WM_DELETE_WINDOW", on_close)
    return (w, top)

def set_close_callback(abort_game):
    XOPage_support.set_close_callback(abort_game)

def on_close():
    print ("XO closing")
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        XOPage_support.on_close()
        w.destroy()


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

        top.geometry("600x451+882+239")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("XO")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.1, rely=0.067, relheight=0.896, relwidth=0.872)
        self.Frame1.configure(relief='flat')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#408080")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.518, rely=0.173, relheight=0.817)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(self.Frame1)
        self.TSeparator2.place(relx=0.751, rely=0.198, relheight=0.792)
        self.TSeparator2.configure(orient="vertical")

        self.TSeparator3 = ttk.Separator(self.Frame1)
        self.TSeparator3.place(relx=0.287, rely=0.446, relwidth=0.688)

        self.TSeparator3_1 = ttk.Separator(self.Frame1)
        self.TSeparator3_1.place(relx=0.287, rely=0.718, relwidth=0.688)

        self.XO_Label = ttk.Label(self.Frame1)
        self.XO_Label.place(relx=0.402, rely=0.025, height=69, width=245)
        self.XO_Label.configure(background="#408080")
        self.XO_Label.configure(foreground="#ffffff")
        self.XO_Label.configure(font="-family {Tw Cen MT} -size 40 -weight bold")
        self.XO_Label.configure(relief="flat")
        self.XO_Label.configure(text='''X/O play!''')

        self.Button0 = tk.Button(self.Frame1)
        self.Button0.place(relx=0.302, rely=0.198, height=94, width=107)
        self.Button0.configure(activebackground="#408080")
        self.Button0.configure(activeforeground="white")
        self.Button0.configure(activeforeground="black")
        self.Button0.configure(background="#408080")
        self.Button0.configure(command=lambda: XOPage_support.button_click(0, self.Button0))
        self.Button0.configure(disabledforeground="#ffffff")
        self.Button0.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button0.configure(foreground="#ffffff")
        self.Button0.configure(highlightbackground="#d9d9d9")
        self.Button0.configure(highlightcolor="black")
        self.Button0.configure(pady="0")
        self.Button0.configure(relief="groove")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.535, rely=0.198, height=94, width=107)
        self.Button1.configure(activebackground="#408080")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#408080")
        self.Button1.configure(command=lambda: XOPage_support.button_click(1, self.Button1))
        self.Button1.configure(disabledforeground="#ffffff")
        self.Button1.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#c0c0c0")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.765, rely=0.198, height=94, width=107)
        self.Button2.configure(activebackground="#408080")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#408080")
        self.Button2.configure(command=lambda: XOPage_support.button_click(2, self.Button2))
        self.Button2.configure(disabledforeground="#ffffff")
        self.Button2.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="groove")

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.302, rely=0.47, height=94, width=107)
        self.Button3.configure(activebackground="#408080")
        self.Button3.configure(activeforeground="white")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#408080")
        self.Button3.configure(command=lambda: XOPage_support.button_click(3, self.Button3))
        self.Button3.configure(disabledforeground="#ffffff")
        self.Button3.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(relief="groove")

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.535, rely=0.47, height=94, width=107)
        self.Button4.configure(activebackground="#408080")
        self.Button4.configure(activeforeground="white")
        self.Button4.configure(activeforeground="black")
        self.Button4.configure(command=lambda: XOPage_support.button_click(4, self.Button4))
        self.Button4.configure(background="#408080")
        self.Button4.configure(disabledforeground="#ffffff")
        self.Button4.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button4.configure(foreground="#ffffff")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(relief="groove")

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.765, rely=0.47, height=94, width=107)
        self.Button5.configure(activebackground="#408080")
        self.Button5.configure(activeforeground="white")
        self.Button5.configure(activeforeground="black")
        self.Button5.configure(command=lambda: XOPage_support.button_click(5, self.Button5))
        self.Button5.configure(background="#408080")
        self.Button5.configure(cursor="fleur")
        self.Button5.configure(disabledforeground="#ffffff")
        self.Button5.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button5.configure(foreground="#ffffff")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(relief="groove")

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.306, rely=0.743, height=94, width=107)
        self.Button6.configure(activebackground="#408080")
        self.Button6.configure(activeforeground="white")
        self.Button6.configure(activeforeground="black")
        self.Button6.configure(background="#408080")
        self.Button6.configure(command=lambda: XOPage_support.button_click(6, self.Button6))
        self.Button6.configure(disabledforeground="#ffffff")
        self.Button6.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button6.configure(foreground="#ffffff")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(relief="groove")

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.535, rely=0.743, height=94, width=107)
        self.Button7.configure(activebackground="#408080")
        self.Button7.configure(activeforeground="white")
        self.Button7.configure(activeforeground="black")
        self.Button7.configure(background="#408080")
        self.Button7.configure(command=lambda: XOPage_support.button_click(7, self.Button7))
        self.Button7.configure(disabledforeground="#ffffff")
        self.Button7.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button7.configure(foreground="#ffffff")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(relief="groove")

        self.Button8 = tk.Button(self.Frame1)
        self.Button8.place(relx=0.765, rely=0.743, height=94, width=107)
        self.Button8.configure(activebackground="#408080")
        self.Button8.configure(activeforeground="white")
        self.Button8.configure(activeforeground="black")
        self.Button8.configure(command=lambda: XOPage_support.button_click(8, self.Button8))
        self.Button8.configure(background="#408080")
        self.Button8.configure(cursor="fleur")
        self.Button8.configure(disabledforeground="#ffffff")
        self.Button8.configure(font="-family {Tw Cen MT} -size 72 -weight bold")
        self.Button8.configure(foreground="#ffffff")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(relief="groove")

        self.opponentName_Label = tk.Label(self.Frame1)
        self.opponentName_Label.place(relx=0.019, rely=0.473, height=25
                , width=134)
        self.opponentName_Label.configure(activebackground="#f9f9f9")
        self.opponentName_Label.configure(activeforeground="#408080")
        self.opponentName_Label.configure(anchor='w')
        self.opponentName_Label.configure(background="#408080")
        self.opponentName_Label.configure(disabledforeground="#a3a3a3")
        self.opponentName_Label.configure(font="-family {Tw Cen MT} -size 11 -weight bold")
        self.opponentName_Label.configure(foreground="#000000")
        self.opponentName_Label.configure(highlightbackground="#d9d9d9")
        self.opponentName_Label.configure(highlightcolor="black")

        self.opponentScore_Label = tk.Label(self.Frame1)
        self.opponentScore_Label.place(relx=0.019, rely=0.573, height=25
                , width=134)
        self.opponentScore_Label.configure(activebackground="#f9f9f9")
        self.opponentScore_Label.configure(activeforeground="#408080")
        self.opponentScore_Label.configure(anchor='w')
        self.opponentScore_Label.configure(background="#408080")
        self.opponentScore_Label.configure(cursor="fleur")
        self.opponentScore_Label.configure(disabledforeground="#a3a3a3")
        self.opponentScore_Label.configure(font="-family {Tw Cen MT} -size 11 -weight bold")
        self.opponentScore_Label.configure(foreground="#000000")
        self.opponentScore_Label.configure(highlightbackground="#d9d9d9")
        self.opponentScore_Label.configure(highlightcolor="black")
        self.opponentScore_Label.configure(justify='left')
        self.opponentScore_Label.configure(pady="0")

        self.userScore_Label = tk.Label(self.Frame1)
        self.userScore_Label.place(relx=0.019, rely=0.373, height=25, width=134)
        self.userScore_Label.configure(activebackground="#f9f9f9")
        self.userScore_Label.configure(activeforeground="#408080")
        self.userScore_Label.configure(anchor='w')
        self.userScore_Label.configure(background="#408080")
        self.userScore_Label.configure(cursor="fleur")
        self.userScore_Label.configure(disabledforeground="#a3a3a3")
        self.userScore_Label.configure(font="-family {Tw Cen MT} -size 11 -weight bold")
        self.userScore_Label.configure(foreground="#000000")
        self.userScore_Label.configure(highlightbackground="#d9d9d9")
        self.userScore_Label.configure(highlightcolor="black")

        self.symbol_Label = tk.Label(self.Frame1)
        self.symbol_Label.place(relx=0.019, rely=0.273, height=25, width=134)
        self.symbol_Label.configure(activebackground="#f9f9f9")
        self.symbol_Label.configure(activeforeground="black")
        self.symbol_Label.configure(anchor='w')
        self.symbol_Label.configure(background="#408080")
        self.symbol_Label.configure(disabledforeground="#a3a3a3")
        self.symbol_Label.configure(font="-family {Tw Cen MT} -size 11 -weight bold")
        self.symbol_Label.configure(foreground="#000000")
        self.symbol_Label.configure(highlightbackground="#d9d9d9")
        self.symbol_Label.configure(highlightcolor="black")

        self.turn_Label = tk.Label(self.Frame1)
        self.turn_Label.place(relx=0.019, rely=0.673, height=25, width=134)
        self.turn_Label.configure(activebackground="#f9f9f9")
        self.turn_Label.configure(activeforeground="black")
        self.turn_Label.configure(anchor='w')
        self.turn_Label.configure(background="#408080")
        self.turn_Label.configure(disabledforeground="#a3a3a3")
        self.turn_Label.configure(font="-family {Tw Cen MT} -size 11 -weight bold")
        self.turn_Label.configure(foreground="#000000")
        self.turn_Label.configure(highlightbackground="#d9d9d9")
        self.turn_Label.configure(highlightcolor="black")

if __name__ == '__main__':
    vp_start_gui()





