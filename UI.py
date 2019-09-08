import tkinter as tk
from tkinter import *


def save():
    print('saved')


def clearData():
    print('Cleared Data')


def new():
    print('New')


def getPos(val):
    scale1 = val
    print(scale1)

# Vars

r = Tk()
scale1 =
photoNum = 20
r.title('Structure from Motion Control Panel')

menu = Menu(r)
r.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="New...", command=new)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=r.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Clear Data", command=clearData)


w = Scale(r, from_=0, to=42, command=getPos)
w.pack()

w = Scale(r, from_=0, to=photoNum+scale1, orient=HORIZONTAL)
w.pack()
print(scale1)
mainloop()

