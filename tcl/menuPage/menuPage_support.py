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

def startEntryPage():
    sys.stdout.flush()
    sys.path.append('..\entryPage')
    import entryPage
    entryPage.create_Toplevel1(root, 'Hello', top_level)

def startInstPage():
    sys.stdout.flush()
    sys.path.append('..\instPage')
    import instPage
    instPage.create_Toplevel1(root, 'Hello', top_level)

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
    import openPage
    openPage.vp_start_gui()




