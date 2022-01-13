from tkinter import *
import tkinter.messagebox as tmsg

screen=Tk()
screen.title("Slider")
screen.geometry("622x555")

def likes():
    tmsg.showinfo("Likes",f"You got {slider.get()} likes")

Label(screen,text="How many likes do you want?").pack()
slider=Scale(screen,to=200,orient=HORIZONTAL,tickinterval=100)
slider.set(50)
slider.pack()

Button(screen,text="Get likes",command=likes).pack()

screen.mainloop()