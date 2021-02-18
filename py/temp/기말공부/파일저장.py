from tkinter import filedialog
from tkinter import *
win = Tk()
win.filename=filedialog.asksaveasfilename(initialdir="/",title="Select file",\
                                          filetypes = (("txt files","*.txt"),
                                                       ("jpeg files","*.jpg"),
                                                       ("all files","*.*")))
print (win.filename)
