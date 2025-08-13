#Create 3x3 matrix and calculate the sum of the diagonal elements.

import numpy as np
def mat(rows,cols):
    matrix=[]
    for i in range(rows):
        a=[]
        for j in range(cols):
            val=int(input("Enter the element:"))
            a.append(val)
            matrix.append(a)
            array=np.array(matrix)
            return array
def sum_diagonal(A):
    sum=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i==j:
                sum=sum+A[i][j]
        return sum

rows=int(input("Enter number of rows:"))
cols=int(input("Enter number of columns:"))

print("Enter the matrix:\n")
A=mat(rows,cols)
print(A)
print("The sum of diagonal matrix=",sum_diagonal(A))