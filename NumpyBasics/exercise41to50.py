import numpy as np
#41. Write a NumPy program to convert numpy dtypes to native python types.
def convertDtypes():
    a = np.ones(1)
    print("The type of a is: ",a.dtype)
    if a.size == 1: 
        aPython = a.item()
        print(type(aPython))
    else:
        raise Exception("You can only convert number using this method")
#convertDtypes()

#42. Write a NumPy program to add elements in a matrix. 
#If an element in the matrix is 0, we will not add the element below this element.
def addToMatrix():
    a = np.array([[1,2,3],[2,0,0],[1,5,1]]) 
    counter = 0  
    for i in range(len(a)):  
        for j in range(len(a)):  
            if a[i,j] == 0 and i < len(a)-1: 
                a[i+1][j] = 0  
            counter += a[i][j]  
    print(a,"The sum of the items in the matrix is: ",counter)
    return counter
#addToMatrix()

#43. Write a NumPy program to find the missing data in a given array.
def missingN():
    a = np.arange(10)
    missing = a % 2 == 0 #pretend that even elements are missing
    print("Is the element missing?",missing)
    #or
    b = np.ma.masked_array(np.arange(10))
    b[b<2] = np.ma.masked
    print(b)
    #or
    c=np.array([[1,2,np.nan],[4,np.nan,6]])
    print("missing number?\n ",np.isnan(c))
#missingN()

#44. Write a NumPy program to check whether two arrays are equal (element wise) or not.
def equals():
    zeros= np.zeros((2,2))
    ones= np.ones((2,2))
    equal = np.equal(zeros,ones)
    print("Are the elemets equal?",equal)
#equals()

#45. Write a NumPy program to create one-dimensional array of single, two and three digit numbers.
def create1D():
    x = np.arange(0,10,1)
    y = np.arange(10,100,10)
    z = np.arange(100,1000,100)
    print(x,y,z)
#create1D()

#46. Write a NumPy program to create a two-dimensional array of specified format.
def create2D(x,y):
    a = np.random.randint(0,10,(x,y))
    print(a)
#create2D(4,4)

#47. Write a NumPy program to create a one dimensional array of forty pseudo-randomly generated values.
#  Select random numbers from a uniform distribution between 0 and 1    
def arrayG():
    a=np.random.uniform(0,1,40)
    print(a)
#arrayG()

#48.Write a NumPy program to create a two-dimensional array with shape (8,5) of random numbers.
#  Select random numbers from a normal distribution (200,7).
def q48():
    a = np.random.normal(200,7,(8,5))
    print(a)
#q48()

#49. Write a NumPy program to generate a uniform, non-uniform random sample from a given 1-D array with and without replacement
def q49():
    a = np.random.uniform(1,10,(10))
    b = np.random.choice(a,a.shape)
    c = np.random.choice(a,a.shape,replace=False)
    print(a,"\n",b,"\n",c)
#q49()

#50. Write a NumPy program to create a 4x4 array with random values, now create a new array from the said array swapping first and last rows.
def q50():
    a = np.random.randint(0,20,(4,4))
    b = np.random.randint(0,20,(4,4))
    #print(a)
    b[0,:] = a[0,:]
    b[3,:] = a[3,:]
    a[3,:] = b[0,:]
    a[0,:] = b[3,:]
    #print(a)
    #or
    x = np.random.randint(0,20,(4,4))
    y = np.copy(x)
    first_row = y[0,:]
    last_row = y[3,:]
    print(x)
    x[0] = last_row
    x[3] = first_row
    print(x)
#q50()


