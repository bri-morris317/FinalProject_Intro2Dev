from tkinter import *
from tkinter import StringVar
from typing import Type

root = Tk()

root.geometry("500x300")


def close():
    root.destroy()
    
Label(root, text="Bandera Entertainment Registration Successful!", font="arial 15 bold").grid(row=0, column=3)

Button(text="Exit" , command=close).grid(row=4, column=3)

root.mainloop()
