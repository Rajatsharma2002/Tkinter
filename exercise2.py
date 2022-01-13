from tkinter import *

def func():
   screen.geometry(f"{width_val.get()}x{height_val.get()}")

screen=Tk()
screen.title("Exercise 2")

screen.geometry("300x200")

Label(screen,text="Width").grid()
Label(screen,text="Height").grid()

wid=StringVar()
hei=StringVar()

width_val=Entry(screen,textvariable=wid)
height_val=Entry(screen,textvariable=hei)
width_val.grid(row=0,column=1)
height_val.grid(row=1,column=1)

Button(screen,text="Apply",command=func).grid(column=1)

screen.mainloop()