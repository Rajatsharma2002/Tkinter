from tkinter import *

screen=Tk()
screen.geometry("555x444")
screen.title("Basic Functions")


screen.wm_iconbitmap("1.ico")

width = screen.winfo_screenwidth()
height = screen.winfo_screenheight()
print(f"{width}x{height}")

Button(text="Close",command=screen.destroy).pack()
screen.config(background="orange")
screen.mainloop()