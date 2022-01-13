from tkinter import *

def click(event):
    global slide
    text=event.widget.cget("text")
    if text=="C":
        slide.set("")
        root.update()

    elif text=="=":
        if slide.get().isdigit():
            value=int(slide.get())
        else:
            try:
                value=eval(slide.get())
            except EXCEPTION as e:
                print(e)
                value="ERROR"

            slide.set(value)
            root.update()
    else:
        slide.set(slide.get()+text)
        root.update()

def button(f,*args):
    for i in args:
        b=Button(f,text=f"{i}",font="ARIAL 30 bold")
        b.pack(side=LEFT,padx=10,pady=10)
        b.bind("<Button-1>",click)

screen=Tk()
screen.geometry("500x500")
screen.title("Calculator")
screen.config(background="black")

slide=StringVar()
slide.set("")
root=Entry(screen,textvariable=slide,font="ARIAL 30 bold")
root.pack(fill=X,pady=10,padx=10)

# f=Frame(screen,bg="grey")
# button(f,"%","00","/")
# f.pack()

f=Frame(screen,bg="black")
button(f,"9","8","7","*")
f.pack()

f=Frame(screen,bg="black")
button(f,"6","5","4","-")
f.pack()

f=Frame(screen,bg="black")
button(f,"3","2","1","+")
f.pack()

f=Frame(screen,bg="black")
button(f,"C","0",".","=")
f.pack()

screen.mainloop()