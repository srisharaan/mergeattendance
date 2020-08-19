from tkinter import *
#import openpyxl as xl
import vaandru
from vaandru import paavam
import chardet
import pandas as pd
#from pandas import *
import openpyxl as xl


def getdet():
    global ws1
    global wb1
    root = Tk()
    root.title("MMM")
    def button2_click():
        root.destroy()
    def button1_click():
        #e1.delete(0,END)
        #e1.insert("saved")
        id=e1.get()
        paavam(id)
        mylabel=Label(root,text="saved")
        mylabel.grid(row=9,column=0,columnspan=3,padx=10,pady=10)

    e1 = Entry(root, width=35, borderwidth=5)
    e1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    button_1 = Button(root, text="enter", padx=20, pady=10, command=button1_click)
    button_1.grid(row=10, column=1)
    mylabel1=Label(root,text="File name with path")
    mylabel1.grid(row=1,column=0,columnspan=3,padx=10,pady=10)


    button_2 = Button(root, text="exit", padx=20, pady=10, command=button2_click)
    button_2.grid(row=10, column=2)

    root.mainloop()

getdet()
