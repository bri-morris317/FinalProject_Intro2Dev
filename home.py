from tkinter import *
from tkinter import StringVar
from typing import Type

ws = Tk()

ws.geometry("500x300")



Label(ws, text="Bandera Entertainment Registration", font="arial 15 bold").grid(row=0, column=1)
sign = Label(ws, text="Ready to Sign Up? Click Below!")

sign.grid(row=1, column =1)

def nextPage():
    ws.destroy()
    import registration.py


# Submit Button
Button(text="Sign Up!" , command=nextPage,).grid(row=2, column=1)


ws.mainloop()
