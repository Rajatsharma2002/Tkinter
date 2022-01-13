# from tkinter import *
# from PIL import  ImageTk, Image
#
# def every_100(text):
#     final_text = ""
#     for i in range(0, len(text)):
#         final_text +=text[i]
#         if i%100==0 and i!=0:
#             final_text += "\n"
#     return final_text
#
#
#
# root = Tk()
# root.title("Aapka Apna Akhabaar")
# root.geometry("1000x1000")
#
# texts = []
# photos = []
# for i in range(0, 3):
#     with open(f"{i+1}.txt") as f:
#         text = f.read()
#         texts.append(every_100(text))
#
#     image = Image.open(f"{i+1}.png")
#     #TODO: Resize these images
#     image = image.resize((225, 200), Image.ANTIALIAS)
#     photos.append(ImageTk.PhotoImage(image))
#
# f0 = Frame(root, width=800, height=70)
# Label(f0, text="Code With Harry News", font="lucida 33 bold").pack()
# Label(f0, text="January 19, 2050", font="lucida 13 bold").pack()
# f0.pack()
#
#
# f1 = Frame(root, width=900, height=200, pady=14)
# Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")
# Label(f1, image=photos[0], anchor="e").pack()
# f1.pack(anchor="w")
#
#
# f2 = Frame(root, width=900, height=200, pady=14, padx=22)
# Label(f2, text=texts[1], padx=22, pady=22).pack(side="right")
# Label(f2, image=photos[1], anchor="e", padx=22).pack()
# f2.pack(anchor="w")
#
#
# f3 = Frame(root, width=900, height=200, pady=34)
# Label(f3, text=texts[2], padx=22, pady=22).pack(side="left")
# Label(f3, image=photos[2], anchor="e").pack()
# f3.pack(anchor="w")
#
# root.mainloop()

# my solution
from tkinter import *
import datetime
from PIL import Image,ImageTk

screen=Tk()
screen.title("Newspaper")
screen.geometry("1200x1200")

Label(text="Times India Newspaper",bg="black",fg="white",font="ARIAL 20 bold").pack()
y=datetime.datetime.now().strftime("%Y-%m-%d")
Label(text=f"{y}",font="ARIAL 15 bold").pack()

text=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        content=f.read()
        text.append(content)

    image=Image.open(f"{i+1}.png")
    image = image.resize((225, 200), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    photos.append(photo)

f1=Frame(screen,width=1200,height=200,pady=14)
Label(f1,text=text[0],padx=44,pady=22).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack()
f1.pack(anchor="w")

f2=Frame(screen,width=1200,height=200,padx=44,pady=14)
Label(f2,text=text[1],padx=44,pady=22).pack(side="right")
Label(f2,image=photos[1],anchor="e",padx=44).pack()
f2.pack(anchor="w")

f3 = Frame(screen, width=1200, height=200, pady=34)
Label(f3, text=text[2], padx=44, pady=22).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")

screen.mainloop()

