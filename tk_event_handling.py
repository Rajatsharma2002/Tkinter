from tkinter import *
def func1(event):
    print(f"Your cursor is on {event.x},{event.y}")

screen=Tk()
screen.title("Event handling")

screen.geometry("700x600")

obj=Button(screen,text="click")
obj.pack()

obj.bind("<Button-1>",func1)
obj.bind("<Double-3>",quit)
screen.mainloop()