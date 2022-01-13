from tkinter import *

root=Tk()

# width and height
root.geometry("733x434")

# max value of width,height
root.maxsize(900,900)

# min value of width,height
root.minsize(300,200)

# entering text in gui
text=Label(text="Welcome to Pycharm")
text.pack()

root.mainloop()