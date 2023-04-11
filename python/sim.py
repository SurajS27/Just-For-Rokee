from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("654x420")

f1 = Frame(root, background="white", borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT,pady=0, fill=Y)

f2 = Frame(root, bg="red" , borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP, padx=150, pady=0, fill=X)

f3 = Frame(root,background="white", borderwidth=5, relief=SUNKEN)
f3.pack(side=RIGHT)

image = Image.open("logo.png")
reimg = image.resize((90,60))
logo = ImageTk.PhotoImage(reimg)
logo_label = Label(f1,image=logo)
logo_label.image = logo
logo_label.pack()

welcome = Label(f2,text="WELCOME TO JUST FOR ROOKIES")
welcome.pack()


s=Label(root, text="Simplex Method")
t=Label(root, text="Max")
z1 = Label(root, text="x =" )
z2 = Label(root, text="y =" )
u=Label(root, text="Subject to")
x1 = Label(root, text="x1 =" )
y1 = Label(root, text="+ y1 =" )
c1 = Label(root, text="<=  c1=" )
x2 = Label(root, text="x2 =" )
y2 = Label(root, text="+ y2 =" )
c2 = Label(root, text="<=  c2 =" )

s.grid(row=0, column=5)
t.grid(row=1,column=0)
u.grid(row=3,column=0)


z1.grid(row=1,column=2)
z2.grid(row=1,column=5)
x1.grid(row=3,column=2)
y1.grid(row=3,column=4)
c1.grid(row=3,column=6)
x2.grid(row=4,column=2)
y2.grid(row=4,column=4)
c2.grid(row=4,column=6)

z1value = IntVar()
z2value = IntVar()
x1value = IntVar()
y1value = IntVar()
c1value = IntVar()
x2value = IntVar()
y2value = IntVar()
c2value = IntVar()

z1entry = Entry(f3,root,textvariable=z1value)
z2entry = Entry(f3,root,textvariable=z2value)
x1entry = Entry(f3,root,textvariable=x1value)
y1entry = Entry(f3,root,textvariable=y1value)
c1entry = Entry(f3,root,textvariable=c1value)
x2entry = Entry(f3,root,textvariable=x2value)
y2entry = Entry(f3,root,textvariable=y2value)
c2entry = Entry(f3,root,textvariable=c2value)

z1entry.grid(row=1, column=3)
z2entry.grid(row=1, column=6)
x1entry.grid(row=3, column=3)
y1entry.grid(row=3, column=5)
c1entry.grid(row=3, column=7)
x2entry.grid(row=4, column=3)
y2entry.grid(row=4, column=5)
z2entry.grid(row=4, column=7)

Button(text="calculate",command="simplex")




root.mainloop()