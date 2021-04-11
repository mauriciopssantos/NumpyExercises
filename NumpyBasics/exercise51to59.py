import numpy as np
#51. Write a NumPy program to create a new array of given shape (5,6) and type, filled with zeros.
def q51():
    print(np.zeros((5,6)))

#q51()

#52. Write a NumPy program to sort a given array by row and column in ascending order.
def q52():
    a=np.random.randint(0,101,20)
    print(np.sort(a))
#q52()

#53. Write a NumPy program to extract all numbers from a given array which are less and greater than a specified number
def q53():
    a=np.random.randint(0,101,20)
    print(np.sort(a[a<50]))
    print(np.sort(a[a>50]))
#q53()

#54. Write a NumPy program to replace all numbers in a given array which is equal, less and greater to a given number.
def q54():
    a=np.random.randint(0,101,20)
    b = np.ones(a[a<50].shape)
    a[a<50] = b
    print(np.sort(a))
    #or 
    c=np.random.randint(0,101,20)
    print(np.where(c<=50,10,c-c))
#q54()

#55. Write a NumPy program to create an array of equal shape and data type of a given array. 
def q55():
    a=np.random.rand(4,4)
    b=np.copy(a)
    print(a,"\n",b)
#q55()

#56. Write a NumPy program to create a three-dimension array with shape (3,5,4) and set to a variable.
def q56():
    a=np.random.randint(0,101,(3,5,4))
    print(a)
#q56()

#57. Write a NumPy program to create a 4x4 array, now create a new array from the said array swapping first and last, second and third columns
def q57():
    a=np.array([1,2,3,4,1,2,3,4,1,2,3,4,0,0,0,0]).reshape((4,4))
    print("Original array",a)
    b = np.flip(a,axis=1)
    c = a[:: -1,:]
    print("Shuffled array",b)
    print(c)
#q57()

#58. Write a NumPy program to swap rows and columns of a given array in reverse order.
def q58():
    a=np.array([1,2,3,4,1,2,3,4,1,2,3,4,0,0,0,0]).reshape((4,4))
    b=a[:: -1,:: -1]
    print(a)
    print(b)
#q58()

#59. Write a NumPy program to multiply two give arrays of same size element-by-element.
def q59():
    pass     
    