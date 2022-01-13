from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("677x456")
        self.title("Classes and objects")
    def status(self):
        self.status_bar=StringVar()
        self.status_bar.set("Ready")
        Label(self,textvar=self.status_bar,relief=SUNKEN,anchor="w").pack(fill=X,side=BOTTOM)

    def func(self):
        print("This function is a print function")

    def button(self,txt):
        Button(self,text=txt,command=self.func).pack()

if __name__ == '__main__':
    screen=GUI()
    screen.status()
    screen.button("Print")
    screen.mainloop()