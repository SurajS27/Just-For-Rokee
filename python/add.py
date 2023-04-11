from tkinter import *

root = Tk()

def gadd():
    a= xvalue.get()
    b= yvalue.get()
    sum = a+b
    Add= Label(root,text=sum)
    Add.grid()

x = Label(root, text="num1")
y = Label(root, text="num2")

x.grid(row=0, column=0)
y.grid(row=1, column=0)


xvalue=IntVar()
yvalue = IntVar()

xentry = Entry(root,textvariable=xvalue)
yentry = Entry(root,textvariable=yvalue)

xentry.grid(row=0, column=1)
yentry.grid(row=1,column=1)

Button(text="add",command=gadd).grid(row=2,column=1)


root.mainloop()