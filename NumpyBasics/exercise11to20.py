import numpy as np
import sys
#Solving the exercises 11 - 20:
#11. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
def comparisonEqual(x,y):
    print("The comparison between the elemets of the array {} and array {} are {}.".format(x,y,np.equal(x,y)))

def comparisonTolerance(x,y):
    print("The comparison between the elemets of the array {} and array {} are {}.".format(x,y,np.allclose(x,y)))

x=np.array([1,2,3,4,5.000001])
y=np.array([1,2,3,4,5])
#comparisonTolerance(x,y)
#comparisonEqual(x,y)

#12. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
def generateArray():
    x=np.array([1,7,13,105])
    print("The size of the array {} is {} bytes".format(x,sys.getsizeof(x)))
#generateArray()

#13. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
def generate015():
    print(np.zeros(10))
    print(np.ones(10))
    print(5*np.ones(10))
#generate015()

#14. Write a NumPy program to create an array of the integers from 30 to70.
def generate3070():
    print("Creating an array with the range 30-70",np.arange(30,71))
#generate3070()

#15. Write a NumPy program to create an array of all the even integers from 30 to 70
def generate3070even():
    print("Creating an array with the range 30-70 only even numbers",np.arange(30,71,2))
#generate3070even()

#16. Write a NumPy program to create a 3x3 identity matrix
def indentityMatrix(n):
    print("Creating a squared identity matrix of {}x{}".format(n,n))
    print(np.identity(n))
#indentityMatrix(5)

#17. Write a NumPy program to generate a random number between 0 and 1.
def randomN():
    print("Generating a random array between 0 - 1",np.random.uniform(0,1,10))
#randomN()

#18. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.
def randomArr():
    print("Generating a random array in a standard normal distribution",np.random.normal(0,1,15))
#randomArr()

#19. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
def createVec():
    x=np.arange(15,55).reshape(-1,1)
    print(x[1:-1])
#createVec()

#20. Write a NumPy program to create a 3X4 array using and iterate over it.
def createArray(n,m):
    x=np.arange(1,13).reshape((n,m))
    print(x)
#createArray(3,4)