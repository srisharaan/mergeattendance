from tkinter import *
#import openpyxl as xl
import vaandru
from vaandru import paavam
import chardet
import pandas as pd
#from pandas import *
import openpyxl as xl
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk


def getdet():
    global ws1
    global wb1
    root = Tk()
    root.geometry("300x350")
    root.title("MMM")
    def browsefunc():
    
        #filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        #(("","*.xlsx"),("all files","*.*")) )
        filez = filedialog.askopenfilenames(parent=root,title='Choose a file',multiple=True)

        var=root.tk.splitlist(filez)
        filePaths = []
        for f in var:
            filePaths.append(f)
        a=len(filePaths)
        print(a)
        i=0
        while(i<a):
            paavam(filePaths[i])
            mylabel=Label(root,text="saved")
            mylabel.grid(row=9,column=0,columnspan=3,padx=10,pady=10)
            i=i+1
        
    def button2_click():
        root.destroy()
    '''
    def button1_click():
        #e1.delete(0,END)
        #e1.insert("saved")
        id=e1.get()
        paavam(id)
        mylabel=Label(root,text="saved")
        mylabel.grid(row=9,column=0,columnspan=3,padx=10,pady=10)
    '''
    #e1 = Entry(root, width=35, borderwidth=5)
    #e1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    #button_1 = Button(root, text="enter", padx=20, pady=10, command=button1_click)
    #button_1.grid(row=10, column=1)
    mylabel1=Label(root,text="Browse the files")
    mylabel1.grid(row=1,column=0,columnspan=3,padx=10,pady=10)


    button_2 = Button(root, text="exit", padx=20, pady=10, command=button2_click)
    button_2.grid(row=10, column=2)


    browsebutton = Button(root, text="Browse",padx=20,pady=10 ,command=browsefunc)
    browsebutton.grid(row=10, column=1)



    root.mainloop()

getdet()

