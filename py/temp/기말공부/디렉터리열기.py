from tkinter import filedialog
from tkinter import *

win = Tk()
win.directory = filedialog.askdirectory()
print (win.directory)
