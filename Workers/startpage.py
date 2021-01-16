import numpy as np
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk
import time
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import Font
import tkinter
import page_support


#LOader
def loading():
    try:
        downloaded.set(next(files))  # update the progress bar
        root.after(1, loading)  # call this function again in 1 millisecond
    except StopIteration:
        # the files iterator is exhausted
        root.destroy()
        import mainfile


#StartGUI
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    page_support.init(root, top)

    progress = ttk.Progressbar(root,
                               orient='horizontal',
                               maximum=3000,
                               variable=downloaded,
                               mode='determinate')
    progress.pack(fill=BOTH, side=BOTTOM)
    loading()
    my_font = Font(family="Times New Roman", size=35, weight="bold")
    Label(root,
          foreground="#adbad8",
          background="#1e2c63",
          text="Design And Analysis Of Alogorithm",
          font=my_font).pack()
    Label(root,
          foreground="#adbad8",
          background="#1e2c63",
          text="Dynamic Programming Algorithms Implementation",
          font=("Helvetica", 35)).pack()
    Label(root,
          foreground="#adbad8",
          background="#1e2c63",
          text="Group Members:",
          font=("Helvetica", 30)).pack()
    Label(root,
          foreground="#adbad8",
          background="#1e2c63",
          text="Owais Sultan          18K-0303",
          font=("Helvetica", 25)).pack()
    Label(root,
          foreground="#adbad8",
          background="#1e2c63",
          text="Kanwal Gul             18K-0250",
          font=("Helvetica", 25)).pack()
    Label(root, foreground="#adbad8", background="#1e2c63",
          font=my_font).pack()
    Label(root, foreground="#adbad8", background="#1e2c63",
          font=my_font).pack()
    Label(root,
          foreground="#adbad8",
          background="#1e2c63",
          text="Please Wait While Loading ...",
          font=my_font).pack()

    root.mainloop()


w = None
w_win = None
rt = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    page_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1(Frame):
    def __init__(self, top=None):
        Frame.__init__(self)
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        # width = top.winfo_screenwidth()
        # height = top.winfo_screenheight()
        top.attributes("-fullscreen", True)
        top.title("New Toplevel")
        top.configure(relief="groove")
        top.configure(cursor="arrow")
        top.configure()

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


root = tk.Tk()
top = Toplevel1(root)
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file="graph.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
files = iter(np.arange(1, 3000))
downloaded = IntVar()
if __name__ == '__main__':
    vp_start_gui()