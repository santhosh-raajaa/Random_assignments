import tkinter as tk
from PIL import ImageTk,Image
import os
win=tk.Tk()
win.title('tkinter tutorial')
img=ImageTk.PhotoImage(Image.open("ironman.jpg"))
w=tk.Label(win,text='hello').pack()
panel=tk.Label(win,image=img)
panel.pack()
win.mainloop()
