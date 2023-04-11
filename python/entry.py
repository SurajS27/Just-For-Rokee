import imp
from tkinter import *
root = Tk()

user = Label(root, text="username")
user.grid()

uservalue = IntVar()
userentry = Entry(root, textvariable= uservalue)

userentry.grid(row=0, column=1)

root.mainloop()