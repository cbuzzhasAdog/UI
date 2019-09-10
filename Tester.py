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
import tkinter as tk

def startgame():

    pass

mw = tk.Tk()

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
mw.option_add("*Button.Background", "black")
mw.option_add("*Button.Foreground", "red")

mw.title('The game')
#You can set the geometry attribute to change the root windows size
mw.geometry("1000x1000") #You want the size of the app to be 500x500
mw.resizable(0, 0) #Don't allow resizing in the x or y direction

back = tk.Frame(master=mw,bg='black')
back.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
back.pack(fill=tk.BOTH, expand=1) #Expand the frame to fill the root window

#Changed variables so you don't have these set to None from .pack()
go = tk.Button(master=back, text='Start Game', command=startgame)
go.pack()
close = tk.Button(master=back, text='Quit', command=mw.destroy)
close.pack()
info = tk.Label(master=back, text='Made by me!', bg='red', fg='black')
info.pack()

mw.mainloop()