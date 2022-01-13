from tkinter import *
import datetime
def val():
    with open("Entry.txt","a") as f:
        f.write(f"{datetime.datetime.now()} - Name : {fname.get()} {lname.get()}\t\tRoll Number : {rno.get()}\n\n")

    with open("Entry.txt","r") as f:
        print(f.read())

screen=Tk()
screen.title("Dance Class Form")
screen.geometry("700x600")

Label(text="First Name").grid()
Label(text="Second Name").grid()
Label(text="Roll Number").grid()

fname=StringVar()
lname=StringVar()
rno=StringVar()

fname_val=Entry(screen,textvariable=fname)
lname_val=Entry(screen,textvariable=lname)
rno_val=Entry(screen,textvariable=rno)
fname_val.grid(row=0,column=1)
lname_val.grid(row=1,column=1)
rno_val.grid(row=2,column=1)

Button(text="Submit",command=val).grid()

screen.mainloop()