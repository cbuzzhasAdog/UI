import tkinter as tk
from tkinter import *


def save():
    print('saved')
def clearData():
    print('Cleared Data')
def new():
    print('New')
def getPos(val):
    v = w.get()
    c.config(to=photoNum+v)


def doNothing():
    print(" ")


# Vars

r = Tk()
scale1 = 0
photoNum = 20
r.title('Structure from Motion Control Panel')

menu = Menu(r)
r.config(menu=menu)
r.geometry("1200x900")

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="New...", command=new)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=r.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Clear Data", command=clearData)

# ***** The Toolbar *****

toolbar = Frame(r, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)



# ***** Status Bar *****

status = Label(r, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

w = Scale(r, from_=0, to=42, command=getPos)
w.pack()

c = Scale(r, from_=0, to=photoNum, orient=HORIZONTAL)
c.pack(side=BOTTOM, fill=X)

mainloop()

