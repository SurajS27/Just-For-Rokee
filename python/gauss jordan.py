import numpy as np
import sys

# Reading number of unknowns
n = int(input('Enter number of variables: '))

# Making numpy array of n x n+1 size and initializing 
# to zero for storing augmented matrix
a = np.zeros((n,n+1))

# Making numpy array of n size and initializing 
# to zero for storing solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

print("\rThe augmented matrix of the above system of equations will be: \n") 

for i in range(n):
    for j in range(n+1):
        print(a[i][j], end = "  ")
    print()

# Applying Gauss Jordan Elimination
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')
        
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
                
    print("\rOur objective is to make the lower left-hand corner of the matrix filled with zeros as much as possible. For that, we will perform a sequence of operations \n")
    for i in range(n):
        for j in range(n+1):
            print(a[i][j], end = "  ")
        print()

# Obtaining Solution

for i in range(n):
    x[i] = a[i][n]/a[i][i]
print("The following result: \n")
for i in range(n):
    print(x[i], end = " " )
    print()

# Displaying solution
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
