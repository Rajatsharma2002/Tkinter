from tkinter import *
import os
from PIL import Image,ImageTk

screen=Tk()
screen.geometry("800x700")

path="C:\\Users\\HP\\Pictures\\wallpaper"
os.chdir(path)
files=os.listdir(os.getcwd())
print(files)
imgfiles=[]
for i in files:
    if '.png' in i or '.jpg' in i:
        imgfiles.append(i)
print(imgfiles)

# for file in files:
#     if file.endswith(".jpg"):
#         image = Image.open(file)
#         photo = ImageTk.PhotoImage(image)
#         add_img = Label(image=photo)
#         add_img.pack()
#     else:
#         photo=PhotoImage(file=file)

for i in imgfiles:
    if '.jpg' in i:
        image = Image.open(i)
        image = image.resize((300, 150), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image)
        label2 = Label(image=photo2)
        label2.pack(side=RIGHT)
    else:
        photo = PhotoImage(file=i)
        label = Label(image=photo)
        label.pack(side=LEFT)
screen.mainloop()