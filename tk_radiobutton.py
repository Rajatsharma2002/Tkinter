from tkinter import *
import tkinter.messagebox as tmsg

screen=Tk()
screen.title("Radio Button")
screen.geometry("566x455")

def order():
    tmsg.showinfo("Order received",f"Your order containing {var.get()} has successfully recieved")

Label(screen,text="What would you like to eat?",font="Arial 20 bold").pack()

# var=IntVar()
# var.set(0)
var=StringVar()
var.set("kuch bhi")

food_items=["Pizza","Burger","Paratha","Dosa","Fries","Kathi Roll"]
# for i in food_items:
#     index=food_items.index(i)
#     Radiobutton(screen,text=i,variable=var,value=index+1).pack(anchor="w")

for i in food_items:
    Radiobutton(screen,text=i,variable=var,value=i).pack(anchor="w")

Button(screen,text="Order",command=order).pack()
screen.mainloop()