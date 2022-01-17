from tkinter import *

#creating screen
screen=Tk()
screen.title("Practice 5 - Scroll Bar")
screen.geometry("566x455")

scroll_bar=Scrollbar(screen)
scroll_bar.pack(side=RIGHT,fill=Y)

text=Text(screen,yscrollcommand=scroll_bar.set)
text.pack(fill=BOTH)
scroll_bar.config(command=text.yview)
screen.mainloop()
