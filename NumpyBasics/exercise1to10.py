import numpy as np
#Solving the first 10 exercises:
#1.Write a NumPy program to get the numpy version and show numpy build configuration:
def exercise1():
  npVersion = np.__version__
  print("The numpy version is",npVersion)

#2. Write a NumPy program to  get help on the add function
def exercise2():  
  getHelpAddFunc = np.info(np.add)
  print(getHelpAddFunc)

#3. Write a NumPy program to test whether none of the elements of a given array is zero.
#Give the np.array X:
#You can make a simple for to check each element or just call the np built in function np.all(X)
def exercise3():
  X = np.array([[1,2,3],[4,5,6]])
  for i in X:
    if i == 0:
      return False
  return True

def exercise3_1():
  X = np.array([[1,2,3],[4,5,0]])
  print(np.all(X))

#4. Write a NumPy program to test whether any of the elements of a given array is non-zero.
#Give the np.array X:
#You can make a simple for to check each element or just call the np built in function np.any(X)
def exercise4():
  X = np.array([[1,2,3],[4,5,6]])
  for i in X:
    if i != 0:
      return True
  return False

def exercise4_1():
  X = np.array([[1,2,3],[4,5,0]])
  print(np.any(X))

  
#5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
#You can define a number infinite using np.inf, and not a number using np.nan.
def exercise5():
  X = np.array([1,np.nan,np.inf])
  Y = np.array([1,2,3])
  
  print("The array element-wise for finiteness in array X?",np.isfinite(X))
  print("The array element-wise for finiteness in array Y?",np.isfinite(Y))
  
#6. Write a NumPy program to test element-wise for positive or negative infinity.
def exercise6():
  X = np.array([1,np.nan,np.inf])
  Y = np.array([1,2,3])
  
  print("The array element-wise for positive or negative infinity in array X?",np.isinf(X))
  print("The array element-wise for positive or negative infinity in array Y?",np.isinf(Y))
  
  
#7. Write a NumPy program to test element-wise for NaN of a given array.
def exercise7():
  X = np.array([1,np.nan,2])
  Y = np.array([1,2,3])
  
  print("The array element-wise for NaN in array X?",np.isnan(X))
  print("The array element-wise for NaN in array Y?",np.isnan(Y))
  
#8. Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not
def exercise8():
  X = np.array([1,1+2j,2])
  Y = np.array([1])
  
  print("The array element-wise for complex number in array X?",np.iscomplex(X))
  print("The array element-wise is a scalar type or not in array Y?",np.isscalar(Y))
  
#9. Write a NumPy program to test whether two arrays are element-wise equal within a tolerance.
#To better understand what is the tolerance range, read the documentation.
#You can use np.info(np.allclose) to check the documentation here.
#I'll give the same examples given in the documentation...
def exercise9():
  print(np.allclose([1e10,1e-7], [1.00001e10,1e-8]))
  print(np.allclose([1e10,1e-8], [1.00001e10,1e-9]))
  print(np.allclose([1e10,1e-8], [1.0001e10,1e-9]))
  print(np.allclose([1.0, np.nan], [1.0, np.nan]))
  print(np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True))
  
#10. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
#You can only compare if the arrays has the same size.
def exercise10():
  X = np.array([1,2,3]).reshape((1,-1))
  Y = np.array([2,2,3]).reshape((1,-1))
  if X.size == Y.size:
    print("Greater:",np.greater(X,Y))
    print("Greater or equal:",np.greater_equal(X,Y))
    print("Less:",np.less(X,Y))
    print("Less equal",np.less_equal(X,Y))
  else:
    raise Exception("Arrays with different sizes")
        
    
  
  
  
