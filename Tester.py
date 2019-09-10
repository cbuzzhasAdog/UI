# from tkinter import *
#
# def sel(num):
#    selection = "Value = " + str(num)
#    label.config(text = selection)
#    var = num
#
#
#
# root = Tk()
# var = DoubleVar()
# scale = Scale( root, variable = var,command=sel)
# scale.pack(anchor=CENTER)
#
#
#
# label = Label(root)
# label.pack()
#
# root.mainloop()
# import tkinter as tk
# #
# # class Example(tk.Frame):
# #     def __init__(self, parent):
# #         tk.Frame.__init__(self, parent)
# #
# #         self.scale = tk.Scale(self, orient="horizontal",
# #                               from_=0, to=600,
# #                               showvalue=False,
# #                               command=self._on_scale)
# #         self.scale_label = tk.Label(self, text="")
# #         self.scale.pack(side="top", fill="x")
# #         self.scale_label.pack(side="top")
# #
# #     def _on_scale(self, value):
# #         value = int(value)
# #         minutes = value/60
# #         seconds = value%60
# #         self.scale_label.configure(text="%2.2d:%2.2d" % (minutes, seconds))
# #
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     Example(root).pack(fill="both", expand=True);
# #     root.mainloop()
# from tkinter import *
#
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# bottomframe = Frame(root)
# bottomframe.pack(side=BOTTOM)
#
#
#
#
# label_1 = Label(frame, text="Name")
# label_1.pack(side = LEFT)
# label_2 = Label(bottomframe, text="Password")
# label_2.pack(side = LEFT)
# entry_1 = Entry(frame)
# entry_1.pack(side = LEFT)
# entry_2 = Entry(bottomframe)
# entry_2.pack(side = LEFT)
#
#  # widgets centered by default, sticky option to change
# # label_1.grid(row=0, sticky=E)
# # label_2.grid(row=1, sticky=E)
# #
# # entry_1.grid(row=0, column=1)
# # entry_2.grid(row=1, column=1)
#
#  # widgets can take up more than one cell with columnspan and rowspan
# c = Checkbutton(root, text="Keep me logged in")
# c.pack()
#
# root.mainloop()
#
from tkinter import *

def donothing():
    print ('IT WORKED')
root=Tk()
root.title(string='LOGIN PAGE')

frame1=Frame(root)
frame1.pack(side=TOP,fill=X)

frame2=Frame(root)
frame2.pack(side=TOP, fill=X)

m=Menu(frame1)
root.config(menu=m)

submenu=Menu(m)
m.add_cascade(label='File',menu=submenu)
submenu.add_command(label='New File', command=donothing)
submenu.add_command(label='Open', command=donothing)
submenu.add_separator()
submenu.add_command(label='Exit', command=frame1.quit)


editmenu=Menu(m)
m.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut',command=donothing)
editmenu.add_command(label='Copy',command=donothing)
editmenu.add_command(label='Paste',command=donothing)
editmenu.add_separator()
editmenu.add_command(label='Exit', command=frame1.quit)


# **** ToolBar *******

toolbar=Frame(frame1,bg='grey')
toolbar.pack(side=TOP,fill=X)
btn1=Button(toolbar, text='Print', command=donothing)
btn2=Button(toolbar, text='Paste', command=donothing)
btn3=Button(toolbar, text='Cut', command=donothing)
btn4=Button(toolbar, text='Copy', command=donothing)
btn1.pack(side=LEFT,padx=2)
btn2.pack(side=LEFT,padx=2)
btn3.pack(side=LEFT,padx=2)
btn4.pack(side=LEFT,padx=2)

# ***** LOGIN CREDENTIALS ******
label=Label(frame2,text='WELCOME TO MY PAGE',fg='red',bg='white')
label.grid(row=3,column=1)

label1=Label(frame2,text='Name')
label2=Label(frame2,text='Password')
label1.grid(row=4,column=0,sticky=E)
label2.grid(row=5,column=0,sticky=E)

entry1=Entry(frame2)
entry2=Entry(frame2)
entry1.grid(row=4,column=1)
entry2.grid(row=5,column=1)

chk=Checkbutton(frame2,text='KEEP ME LOGGED IN')
chk.grid(row=6,column=1)

btn=Button(frame2,text='SUBMIT')
btn.grid(row=7,column=1)




# **** StatusBar ******************

status= Label(root,text='Loading',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()