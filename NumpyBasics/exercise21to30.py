import numpy as np
#Solving the exercises 21 - 30:
#21 Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
def vec5to50():
    x = np.linspace(5,50,10)
    print(x)
    y=np.arange(5,51,5)
    print(y)
#vec5to50()

#22. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15
def changeSign():
    x = np.arange(0,20,dtype=int)
    x[(x>=9)&(x<=15)]*=-1
    print(x.reshape((2,-1)))
#changeSign()

#23. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
def arbVector():
    print(np.random.randint(0,10,5))
#arbVector()

#24. Write a NumPy program to multiply the values of two given vectors.
def multVec():
    x=np.array([1,1,1,1,1])
    y=np.array([2,3,4,5,1])
    print(x*y)
#multVec()

#25. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
def matrixC():
    print(np.arange(10,22).reshape((3,4)))
#matrixC()

#26. Write a NumPy program to find the number of rows and columns of a given matrix
def shapeMatrix():
    x=np.ones(4)
    y=np.ones((3,3))
    print("The shape of the matrix {} is {}".format(x,x.shape))
    print("The shape of the matrix {} is {}".format(y,y.shape))
#shapeMatrix()

#27.Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
def identityMatrix():
    n = int(input("Enter the size of your squared matrix: "))
    x = np.identity(n)
    print("Your matrix identity is \n{}".format(x))
#identityMatrix()
    
#28. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
def borders1():
    x = np.zeros((10,10))
    for i in range(len(x)):
        for j in range(len(x)):
            if i == 0 or j == 0 or i == len(x)-1 or j ==len(x)-1:
                x[i,j]=1
    print(x)
    #or
    y = np.ones((10,10))
    y[1:-1,1:-1] = 0
    print(y)
#borders1()

#29. Write a NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5
def diagonalM():
    x = np.zeros((5,5))
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                x[i,j]=i+1
    print(x)
    #or
    y = np.identity(5)
    for i in range(len(y)):
        for j in range(len(y)):
            y[i,j]*=i+1
    print(y)
    #or
    z = np.diag((1,2,3,4,5))
    print(z)

#diagonalM()

#30. Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal
def diagonal0():
    x = np.ones((4,4))
    for i in range(len(x)):
        for j in range(len(x)):
            if i == j:
                x[i,j]=0
    print(x)
    #or
    x = np.zeros((4, 4))
    x[::2, 1::2] = 1
    x[1::2, ::2] = 1
    print(x)
diagonal0()

