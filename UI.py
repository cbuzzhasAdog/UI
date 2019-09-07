import tkinter as tk
from tkinter import *
master = Tk()
r = tk.Tk()
r.title('Structure from Motion Control Panel')
r = Canvas(master, width=400, height=600)



button = tk.Button(r, text='Stop', width=25, command=r.destroy) 
button.pack()
r.pack()
r.mainloop()