from tkinter import *

screen=Tk()
screen.title("Canvas")

canvas_width=700
canvas_height=600

screen.geometry(f"{canvas_width}x{canvas_height}")

canvas_widget=Canvas(screen,width=canvas_width,height=canvas_height)
canvas_widget.pack()

# craeting a line
canvas_widget.create_line(0,0,350,300)
canvas_widget.create_line(0,300,350,0)

# creating a rectangle
canvas_widget.create_rectangle(100,100,650,500)

# creating an oval we have to give coordinates of a rectangle to make oval
canvas_widget.create_oval(350,300,700,600)

#creating text using canvas
canvas_widget.create_text(350,300,text="hello")


screen.mainloop()