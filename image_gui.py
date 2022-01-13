from tkinter import *
from PIL import Image , ImageTk
screen =Tk()
screen.geometry("700x600")
# screen.minsize(300,200)
# screen.maxsize(900,900)

# adding a png
# photo1 = PhotoImage(file="1.png")

txt=Label(text="landscape")
txt.pack()

# adding jpg to screen
image=Image.open("img.jpg")
photo=ImageTk.PhotoImage(image)

add_img=Label(image=photo)
add_img.pack(side=RIGHT)

screen.mainloop()