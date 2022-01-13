from tkinter import *

def func1():
    pass

screen=Tk()
screen.title("Menus and Submenus")
screen.geometry("500x400")

# single_menu=Menu(screen)
# single_menu.add_command(label="File",command=func1)
# single_menu.add_command(label="Exit",command=quit)
# screen.config(menu=single_menu)

drop_down_menu=Menu(screen)
sub_menu=Menu(drop_down_menu,tearoff=0)
sub_menu.add_command(label="Rename",command=func1)
sub_menu.add_command(label="Save all",command=func1)
sub_menu.add_separator()
sub_menu.add_command(label="Save As",command=func1)
sub_menu.add_command(label="Print",command=func1)
sub_menu.add_command(label="Settings",command=func1)

screen.config(menu=drop_down_menu)
drop_down_menu.add_cascade(label="File",menu=sub_menu)

sub_menu=Menu(drop_down_menu,tearoff=0)
sub_menu.add_command(label="Undo",command=func1)
sub_menu.add_command(label="Cut",command=func1)
sub_menu.add_separator()
sub_menu.add_command(label="Copy",command=func1)
sub_menu.add_command(label="Paste",command=func1)
sub_menu.add_command(label="Find",command=func1)

screen.config(menu=drop_down_menu)
drop_down_menu.add_cascade(label="Edit",menu=sub_menu)


screen.mainloop()