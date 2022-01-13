from tkinter import *

def new():
    global i
    lbx.insert(ACTIVE,f"line {i}")
    i+=1

i=0
screen=Tk()
screen.title("List Box")
screen.geometry("678x567")

lbx=Listbox(screen)
lbx.pack()
lbx.insert(END,"This is the end of box")

Button(screen,text="Add",command=new).pack()

screen.mainloop()