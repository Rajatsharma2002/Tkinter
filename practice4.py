from tkinter import *
import tkinter.messagebox as tmsg

screen=Tk()
screen.title("Customer Experience")
screen.geometry("344x278")

def rate():
    with open("rate.txt","a") as f:
        f.write(f"customer rated {slider.get()}/10\n")
    with open("rate.txt","r") as f:
        print(f.read())
    tmsg.showinfo("Rate","Thanks for rating us!")

Label(screen,text="How was your experience! please rate us").pack()
slider=Scale(screen,to=10,orient=HORIZONTAL,tickinterval=5)
slider.set(5)
slider.pack()

Button(screen,text="Rate",command=rate).pack()
screen.mainloop()