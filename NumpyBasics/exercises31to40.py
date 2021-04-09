import numpy as np
#Solving exercises 31-40
#31. Write a NumPy program to create a 3x3x3 array filled with arbitrary values.
def create333(): 
    print(np.random.rand(3,3,3)*10)

#32. Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.
def sumAllElements():
    x=np.array([1,2,3,4,5])
    print(np.sum(x))
#sumAllElements()

#33. Write a NumPy program to compute the inner product of two given vectors.
def productInner():
    x=np.array([4,5])
    y=np.array([7,10])
    print(np.sum(x*y))
    #or
    print(np.dot(x,y))
#productInner()

#34. Write a NumPy program to add a vector to each row of a given matrix.
def addingVtoM():
    M = np.ones((3,3))
    v = np.random.rand(1,3)
    for i in range(M.shape[1]):
        M[i, :] = M[i, :] + v
    print(M)
#addingVtoM()

#35. Write a NumPy program to save a given array to a binary file. Not completed yet!
def writingFile():
    a = np.random.randint(2,10,(2,4))
    print(a)
#writingFile()

