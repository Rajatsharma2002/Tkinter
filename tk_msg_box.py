from tkinter import *
import tkinter.messagebox as tmsg

def func1():
    print("Working Correctly")

def func2():
    tmsg.askyesno("Rate","Do you want to rate us!")

def func3():
    a=tmsg.askquestion("Subscription","Would you like to subscribe?")
    if a=="yes":
        tmsg.showinfo("Subscribed","You are now a subscriber")
    else:
        tmsg.showinfo("Subs","You rejected our subscribe request")

def func4():
    tmsg.showinfo("Help!","Rajat sharma will help you ! with our fast contact service")

screen=Tk()
screen.title("Message Box")
screen.geometry("500x500")

drop_down_menu=Menu(screen)
sub_menu=Menu(drop_down_menu,tearoff=0)
sub_menu.add_command(label="Rename",command=func1)
sub_menu.add_command(label="Save all",command=func1)
sub_menu.add_separator()
sub_menu.add_command(label="Save As",command=func1)
sub_menu.add_command(label="Print",command=func1)
sub_menu.add_command(label="Settings",command=func1)

screen.config(menu=drop_down_menu)
drop_down_menu.add_cascade(label="File",menu=sub_menu)

sub_menu=Menu(drop_down_menu,tearoff=0)
sub_menu.add_command(label="Undo",command=func1)
sub_menu.add_command(label="Cut",command=func1)
sub_menu.add_separator()
sub_menu.add_command(label="Copy",command=func1)
sub_menu.add_command(label="Paste",command=func1)
sub_menu.add_command(label="Find",command=func1)

screen.config(menu=drop_down_menu)
drop_down_menu.add_cascade(label="Edit",menu=sub_menu)

sub_menu=Menu(drop_down_menu,tearoff=0)
sub_menu.add_command(label="Help",command=func4)
sub_menu.add_command(label="Rate us",command=func2)
sub_menu.add_command(label="Subscription",command=func3)

screen.config(menu=drop_down_menu)
drop_down_menu.add_cascade(label="Help",menu=sub_menu)

screen.mainloop()