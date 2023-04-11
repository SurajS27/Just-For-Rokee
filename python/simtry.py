from tkinter import *
import numpy as np  

from fractions import Fraction

root = Tk()

class PrintLogger(object):  # create file like object

    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.configure(state="normal")  # make field editable
        self.textbox.insert("end", text)  # write text to textbox
        self.textbox.see("end")  # scroll to end
        self.textbox.configure(state="disabled")  # make field readonly

    def flush(self):  # needed for file like object
        pass

def simplex():
    z1=z1value.get()
    z2=6
    x1=x1value.get()
    y1=y1value.get()
    c1=c1value.get()
    x2=x2value.get()
    y2=y2value.get()
    c2=c2value.get()


    A = np.array([[x1, y1, 0, 1], [x2, y2, 1, 0]]) 
    # b will contain the amount of resources  

    b = np.array([c1, c2])            
    # c will contain coefficients of objective function Z       

    c = np.array([z1, z2, 0, 0])              

    
    # B will contain the basic variables that make identity matrix 

    cb = np.array(c[3]) 

    B = np.array([[3], [2]])           

     # cb contains their corresponding coefficients in Z    

    cb = np.vstack((cb, c[2]))         

    xb = np.transpose([b])                  
    # combine matrices B and cb 

    table = np.hstack((B, cb))              

    table = np.hstack((table, xb))          
    # combine matrices B, cb and xb 
    # finally combine matrix A to form the complete simplex table 

    table = np.hstack((table, A))          
    # change the type of table to float 

    table = np.array(table, dtype ='float')  
    # inputs end 

    
    # if min problem, make this var 1 

    MIN = 0

    

    label1=Label(root,text="Table at itr = 0") 
    label1.grid(row=11,column=3)

    label2=Label(root,"B \tCB \tXB \ty1 \ty2 \ty3 \ty4") 
    label2.grid()

    for row in table: 

        for el in row: 

                    # limit the denominator under 100 

            label3=Label(root, text=Fraction(str(el)).limit_denominator(100), end ='\t')  
            label3.grid()

        label9=Label(root, text="") 
        label9.grid()

    label10 = Label(root, text="")
    label10.grid() 

    label4 = Label(root,text="Simplex Working....") 
    label4.grid()
    
    # when optimality reached it will be made 1 

    reached = 0     

    itr = 1

    unbounded = 0

    alternate = 0

    

    while reached == 0: 

    

        label5=Label(root,text="Iteration: ", end =' ') 
        label5.grid()

        label6=Label(root, text=itr) 
        label6.grid()

        label7 = Label(root, text="B \tCB \tXB \ty1 \ty2 \ty3 \ty4") 
        label7.grid()

        for row in table: 

            for el in row: 

                lable8 = Label(root,text=Fraction(str(el)).limit_denominator(100), end ='\t') 
                lable8.grid()

            label11 = Label(root,text="")
            label11.grid() 

    

        # calculate Relative profits-> cj - zj for non-basics 

        i = 0

        rel_prof = [] 

        while i<len(A[0]): 

            rel_prof.append(c[i] - np.sum(table[:, 1]*table[:, 3 + i])) 

            i = i + 1

    

        label12 = Label(root,text="rel profit: ", end =" ") 

        for profit in rel_prof: 

            label13 = Label(root,text=Fraction(str(profit)).limit_denominator(100), end =", ") 

        label14 = Label(root,text="") 

        i = 0



        b_var = table[:, 0] 

        # checking for alternate solution 

        while i<len(A[0]): 

            j = 0

            present = 0

            while j<len(b_var): 

                if int(b_var[j]) == i: 

                    present = 1

                    break; 

                j+= 1

            if present == 0: 

                if rel_prof[i] == 0: 

                    alternate = 1

                    label15 = Label(root,text="Case of Alternate found") 

                    # print(i, end =" ") 

            i+= 1

        label16 = Label(root,text="") 

        flag = 0

        for profit in rel_prof: 

            if profit>0: 

                flag = 1

                break

            # if all relative profits <= 0 

        if flag == 0: 

            label17 = Label(root, text="All profits are <= 0, optimality reached") 

            reached = 1

            break

        

        # kth var will enter the basis 

        k = rel_prof.index(max(rel_prof)) 

        min = 99999

        i = 0; 

        r = -1

        # min ratio test (only positive values) 

        while i<len(table): 

            if (table[:, 2][i]>0 and table[:, 3 + k][i]>0):  

                val = table[:, 2][i]/table[:, 3 + k][i] 

                if val<min: 

                    min = val 

                    r = i     # leaving variable 

            i+= 1

    

            # if no min ratio test was performed 

        if r ==-1: 

            unbounded = 1

            label18 = Label(root,text="Case of Unbounded") 

            break

        

        label19 = Label(root,text="pivot element index:", end =' ') 

        label20 = Label(root,text=np.array([r, 3 + k])) 

    

        pivot = table[r][3 + k] 

        label21=Label(root,text="pivot element: ", end =" ") 

        label22=Label(root,text=Fraction(pivot).limit_denominator(100)) 



            # perform row operations 

        # divide the pivot row with the pivot element 

        table[r, 2:len(table[0])] = table[ 

                r, 2:len(table[0])] / pivot 



        # do row operation on other rows 

        i = 0

        while i<len(table): 

            if i != r: 

                table[i, 2:len(table[0])] = table[i, 2:len(table[0])] - table[i][3 + k] * table[r, 2:len(table[0])]





            i += 1

    



        # assign the new basic variable 

        table[r][0] = k 

        table[r][1] = c[k] 



        label23 = Label(root,text="")  

        label24 = Label(root,text="")  


        itr+= 1



    

    label25 = Label(root,text="")  


    

    label26 = Label(root,text="***************************************************************") 

    if unbounded == 1: 

        label27=Label(root, text="UNBOUNDED LPP") 

        exit() 

    if alternate == 1: 

        label28=Label(root,text="ALTERNATE Solution") 

    

    label29=Label(root,text="optimal table:") 

    label30=Label(root,text="B \tCB \tXB \ty1 \ty2 \ty3 \ty4") 

    for row in table: 

        for el in row: 

            label31=Label(root,text=Fraction(str(el)).limit_denominator(100), end ='\t') 

        label32 = Label(root,text="")  


    label33 = Label(root,text="")  


    label34=Label(root,text="value of Z at optimality: ", end =" ") 

    

    basis = [] 

    i = 0

    sum = 0

    while i<len(table): 

        sum += c[int(table[i][0])]*table[i][2] 

        temp = "x"+str(int(table[i][0])+1) 

        basis.append(temp) 

        i+= 1
    # if MIN problem make z negative 

    if MIN == 1: 

        label35=Label(root,text=-Fraction(str(sum)).limit_denominator(100)) 

    else: 

        label36=Label(root,text=Fraction(str(sum)).limit_denominator(100)) 

    label37=Label(root,text="Final Basis: ", end =" ") 

    label38=Label(root,text=basis) 

    

    label39=Label(root,text="Simplex Finished...") 

    label40 = Label(root,text="") 

    label12.grid()
    label13.grid()
    label14.grid()
    label15.grid()
    label16.grid()
    label17.grid()
    label18.grid()
    label19.grid()
    label20.grid()
    label21.grid()
    label22.grid()
    label23.grid()
    label24.grid()
    label25.grid()
    label26.grid()

    label28.grid()
    label29.grid()
    label30.grid()
    label31.grid()
    label32.grid()
    label33.grid()
    label34.grid()
    label35.grid()
    label36.grid()
    label37.grid()
    label38.grid()
    label39.grid()
    label40.grid()





Label(root, text="Simplex Method").grid(row=0, column=5)
Label(root, text="Max").grid(row=1,column=0)
z11 = Label(root, text="x =" )
z21 = Label(root, text="y =" )
Label(root, text="Subject to").grid(row=3,column=0)
x11 = Label(root, text="x1 =" )
y11 = Label(root, text="+ y1 =" )
c11 = Label(root, text="<=  c1=" )
x21 = Label(root, text="x2 =" )
y21 = Label(root, text="+ y2 =" )
c21 = Label(root, text="<=  c2 =" )

z11.grid(row=1,column=2)
z21.grid(row=1,column=4)
x11.grid(row=3,column=2)
y11.grid(row=3,column=4)
c11.grid(row=3,column=6)
x21.grid(row=4,column=2)
y21.grid(row=4,column=4)
c21.grid(row=4,column=6)

z1value = IntVar()
z2value = IntVar()
x1value = IntVar()
y1value = IntVar()
c1value = IntVar()
x2value = IntVar()
y2value = IntVar()
c2value = IntVar()

z1entry = Entry(root,textvariable=z1value)
z2entry = Entry(root,textvariable=z2value)
x1entry = Entry(root,textvariable=x1value)
y1entry = Entry(root,textvariable=y1value)
c1entry = Entry(root,textvariable=c1value)
x2entry = Entry(root,textvariable=x2value)
y2entry = Entry(root,textvariable=y2value)
c2entry = Entry(root,textvariable=c2value)

z1entry.grid(row=1, column=3)
z2entry.grid(row=1, column=5)
x1entry.grid(row=3, column=3)
y1entry.grid(row=3, column=5)
c1entry.grid(row=3, column=7)
x2entry.grid(row=4, column=3)
y2entry.grid(row=4, column=5)
z2entry.grid(row=4, column=7)

Button(text="calculate",command="simplex").grid(row=6,column=5)






root.mainloop()