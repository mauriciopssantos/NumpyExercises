import numpy as np
import matplotlib.pyplot as plt
import math
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

#35. Write a NumPy program to save a given array to a binary file. 
def writingFile():
    a = np.random.randint(2,10,(2,4))
    with open('C:\\Users\\mauri\\NumpyExercises\\NumpyBasics\\exercise35.npy', 'wb') as fileN:
        np.save(fileN, a)
#writingFile()

#36. Write a NumPy program to save two given arrays into a single file in compressed format (.npz format) and load it.
def writingFileC():
    a =np.random.randint(2,10,(2,4))
    b = np.random.randint(2,10,(4,2))
    with open('C:\\Users\\mauri\\NumpyExercises\\NumpyBasics\\exercise36.npz', 'wb') as fileN:
        np.savez(fileN,a,b)
    
    with open('C:\\Users\\mauri\\NumpyExercises\\NumpyBasics\\exercise36.npz', 'rb') as fileN:
        npz_files = np.load(fileN)
        print(npz_files.files)
        print("The arrays saved in the file are: \n{}\n and\n {}".format(npz_files['arr_0'],npz_files['arr_1']))
#writingFileC()

#37. Write a NumPy program to save a given array to a text file and load it.
def writingFileTxt():
    a =np.random.randint(2,10,(2,4))
    with open('C:\\Users\\mauri\\NumpyExercises\\NumpyBasics\\exercise37.gz', 'wb') as fileN:
        np.savetxt(fileN,X=a)
    with open('C:\\Users\\mauri\\NumpyExercises\\NumpyBasics\\exercise37.gz', 'rb') as fileN:
        txt_file = np.loadtxt(fileN)
        print(txt_file)
#writingFileTxt()

#38. Write a NumPy program to convert a given array into bytes, and load it as array.
def writingBytes():
    a =np.random.randint(2,10,(2,4))
    A = a.tobytes("C")
    arrA = np.frombuffer(A,dtype=a.dtype)
    print(A,arrA)
#writingBytes()

#39. Write a NumPy program to convert a given list into an array, then again convert it into a list. 
# Check initial list and final list are equal or not.
def listToArray():
    a = [1,2,3,4,5,6,7,8,9]
    arrA = np.array(a)
    listA = list(arrA)
    print(a,arrA,listA)
    if a == listA:
        print("They are equal")
    else: 
        print("They are not equal")
#listToArray()

#40. Write a NumPy program to compute the x and y coordinates for points on a sine curve and plot the points using matplotlib
def sineCurve():
    x=np.arange(0,3*np.pi,0.1)
    y = np.sin(x)

    print("values of x: ",x,"values of y: ",y)
    plt.plot(x,y)
    plt.show()
#sineCurve()


        


