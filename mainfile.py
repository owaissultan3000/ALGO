from tkinter import *
from tkinter import ttk
import time
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import Font
import tkinter
from tkinter import filedialog
import tkinter.font as font
from tkinter.filedialog import askopenfile

# def UploadAction(event=None):
#     filename = filedialog.askopenfilename()
#     print('Selected:', filename)

lines = []


def open_file():
    fileopen = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
    if fileopen is not None:
        data = fileopen.readline()


OptionList = [
    "Longest Common Subsequence", "Shortest Common Supersequence",
    "Levenshtein Distance (edit-distance)", "Longest Increasing Subsequence",
    "Matrix Chain Multiplication (Order finding /paranthesization)",
    "0-1-knapsack-problem", "Partition-problem", "Rod Cutting Problem",
    "Coin-change-making-problem", "Word Break Problem"
]
FileList = [
    "File-01",
    "File-02",
    "File-03",
    "File-04",
    "File-05",
    "File-06",
    "File-07",
    "File-08",
    "File-09",
    "File-10",
]

app = tk.Tk()
simg = ImageTk.PhotoImage(Image.open("2112.jpg"))

my = Label(app, image=simg)

my.image = simg

my.place(x=0, y=0)

Frame(app, height=516, width=5, bg='black')

# width = app.winfo_screenwidth()
# height = app.winfo_screenheight()
# app.geometry("800x600")
app.attributes("-fullscreen", True)

app.title("Main Window")

my_font = Font(family="Times New Roman", size=35, weight="bold")

x1 = tk.Label(app,
              foreground="#66FF00",
              background="#808080",
              text="\nSelect The Algorithm 👇",
              font=my_font)
x1.pack(fill=tk.X, pady=9, padx=10)

variable = tk.StringVar(app)
variable.set("Algorithm's List ")

x1 = tk.OptionMenu(app, variable, *OptionList)
x1.config(width=90, font=('Helvetica', 20), bg="GRAY")
x1.pack(fill=tk.X, padx=10)
x1['menu'].config(bg="#7BCAB6")

x2 = tk.Label(app,
              foreground="#66FF00",
              background="#808080",
              text="\nSelect The File 👇",
              font=my_font)
x2.pack(fill=tk.X, pady=9, padx=10)
variable2 = tk.StringVar(app)
variable2.set("Files List")

x2 = tk.OptionMenu(app, variable2, *FileList)
x2.config(width=90, font=('Helvetica', 20), bg="GRAY")
x2.pack(fill=tk.X, padx=10)
x2['menu'].config(bg="#7BCAB6")
myFont = font.Font(size=12)

#run button

button1 = tk.Button(
    app,
    text='Run',
    width="10",
    height="2",
    bg="GRAY",
)
button1['font'] = myFont
button1.pack(pady=70, padx=90)

#Exit Button
button2 = tk.Button(app,
                    text='Exit',
                    width="10",
                    height="2",
                    bg="GRAY",
                    command=app.quit)
button2['font'] = myFont
button2.pack(pady=70, padx=90)

# btn1.grid(row=0, column=0, sticky=W)
# c.grid(row=0, column=1, sticky=W)
# def callback(*args):
#     labelTest.configure(text="\nThe Selected Algorithm Is {}".format(
#         variable.get()),
#                         foreground="BLACK",
#                         background="GRAY")

# variable.trace("w", callback)

app.mainloop()