import tkinter as tk
import tkinter.filedialog as fd

readFile = fd.askopenfilename()
#파일경로

if(readFile != None):
    infile = open(readFile, "r")
    
for line in infile.readlines():
    line = line.strip()
    print(line)
    
infile.close()
