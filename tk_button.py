from tkinter import *

def oh():
    print("good morning")

def printt():
    print("moshi moshi!")

screen=Tk()

screen.geometry("700x600")
screen.title("Buttons")

frame=Frame(bg="yellow",borderwidth=5,relief=SUNKEN,padx=10)
frame.pack(side=LEFT,anchor="se")

b1=Button(frame,text="Greet",font="ARIAL 10 bold",command=oh)
b1.pack(side=LEFT,padx=10)

b1=Button(frame,text="print",font="ARIAL 10 bold",command=printt)
b1.pack(padx=10)

screen.mainloop()