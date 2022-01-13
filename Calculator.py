from tkinter import *

root=Tk()
root.geometry("550x450")
root.title("Calculator")

def click(event):
    global slide
    text = event.widget.cget("text")
    if text == "=":
        if slide.get().isdigit():
            value = int(slide.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        slide.set(value)
        screen.update()

    elif text == "C":
        slide.set("")
        screen.update()

    else:
        slide.set(slide.get() + text)
        screen.update()

slide=StringVar()
slide.set("")
screen=Entry(root,textvariable=slide,font="ARIAL 20 bold")
screen.pack(fill=X,pady=10,padx=10)

f=Frame(root,bg="blue")
b=Button(f,text="9",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=11,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="8",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="7",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="*",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=11,pady=8)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="blue")
b=Button(f,text="6",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=11,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="5",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="4",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=10,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="/",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=11,pady=8)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="blue")
b=Button(f,text="3",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="2",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="1",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="+",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="blue")
b=Button(f,text="0",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9.5,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="C",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="=",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="-",font="ARIAL 30 bold")
b.pack(side=LEFT,padx=9,pady=8)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()
