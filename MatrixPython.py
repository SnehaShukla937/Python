from numpy import *

arr1 = array([[1,2,3,4],[5,6,7,8]])
print(arr1)
print(type(arr1))
print(arr1.ndim)    # dimension of array
print(arr1.shape)  # (rows,col)
print(arr1.dtype)   # type of element
print(arr1.size)   # total no. of elements in array

arr2 = arr1.flatten()  # will convert 2-d to 1-d
print(arr2)
print(arr2.ndim)

arr3 = arr2.reshape(4,2)   # will convert 1-d to 2-d (rows,col)
print(arr3)
print(arr3.ndim)

arr4 = arr2.reshape(2,2,2)   # will convert 1-d to 3-d (2-d arr -> 2d-arr -> 2 elements each)(2*2*2 = 8)
print(arr4)
print(arr4.ndim)

# 2d to 3d conversion

x = array([[1,2,3,4,5,6,7],[8,9,0,1,2,3,4]])
print("2d array:\n",x,x.size,x.ndim)
x = x.flatten()
x = x.reshape(7, 2, 1)
print("3d array:\n",x,x.size,x.ndim)

# array to matrix form

