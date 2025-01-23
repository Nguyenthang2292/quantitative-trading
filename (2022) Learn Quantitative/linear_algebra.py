from sympy import * 

M = Matrix([[1, 1, -2, -2], [0, 1, 3, 7], [1, 0, -1, -1]])
print("Matrix : {} ".format(M))
   
# Use sympy.rref() method 
M_rref = M.rref()  
      
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))  