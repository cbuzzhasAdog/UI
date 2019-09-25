import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def save():
    print('saved')
def clearData():
    print('Cleared Data')
def new():
    print('New')
def openRunFile():
    print ("open")
def searchDialogue():
    searchBox = Tk()
    date = LabelFrame(searchBox,text="Date:", padx=5, pady=5)
    date.grid(row=0, column=0,padx=1, pady=10)
    dateEntry = Entry(date)
    dateEntry.pack()
    imageNum = LabelFrame(searchBox, text="Image Number:", padx=5, pady=5)
    imageNum.grid(row=0, column=2, padx=1, pady=10)
    imageNumEntry = Entry(imageNum)
    imageNumEntry.pack()
    runNumber = LabelFrame(searchBox, text="Run Number:", padx=5, pady=5)
    runNumber.grid(row=0, column=3, padx=1, pady=10)
    runNumberEntry = Entry(runNumber)
    runNumberEntry.pack()
    searchButton = Button(searchBox, text="Search", command=search.quit)
    searchButton.grid(row=1,column=3)
    searchBox.mainloop()
def search():
    return
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

# **** Dropdown menu *******
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
search = Button(toolbar, text="Search", command=searchDialogue)
search.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****
status = Label(r, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
w = Scale(r, from_=0, to=42, command=getPos)
w.pack()
c = Scale(r, from_=0, to=photoNum, orient=HORIZONTAL)
c.set(10)
c.pack(side=BOTTOM, fill=X)

# Display Image
load = Image.open("2.png")
render = ImageTk.PhotoImage(load)

# labels can be text or images
img = Label(r, image=render)
img.image = render

img.pack()

mainloop()

