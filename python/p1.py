from cProfile import label
import re
from tkinter import *
from turtle import bgcolor
from PIL import Image, ImageTk

root = Tk()
f1 = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT, padx=0 , pady=0)

f2 = Frame(root, bg="grey" , borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP, padx=150, pady=0)
image = Image.open("logo.png")
logo = ImageTk.PhotoImage(image)
logo_label = Label(f1,image=logo)
logo_label.image = logo
logo_label.pack()

welcome = Label(f2,text="WELCOME TO JUST FOR ROOKIES")
welcome.pack()
root.mainloop()