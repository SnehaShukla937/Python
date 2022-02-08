from numpy import *

# creating array using array()
arr = array([1, 2, 3, 4, 5, 6])
print(arr)
print(type(arr))  # array type
print(arr.dtype)    # array element type

arr1 = array([1, 2.0, 3.5, 4, 5, 6])
print(arr1)
print(type(arr1))
print(arr1.dtype)

arr2 = array([1, 2, 3, 4, 5], float)
print(arr2)
print(arr2.dtype)
arr3 = array([1, 2.5, 3, 8, 4., 5], int)
print(arr3)
print(arr3.dtype)

# creating array using linespace()
arrlin = linspace(0,16,8)
print(arrlin)
arrlin1 = linspace(0,20)  # arg: [start,stop,no. of parts] ...no. of parts = between start-stop....by default: no. of parts = 50
print(arrlin1)

# creating array using logspace()
arrlog = logspace(1,20 ,5) # arg: [start,stop,no. of parts] ....... no. of parts = between 10^start-10^stop
print(arrlog)

# creating array using arange()
a = arange(0,10,2)
print(a)
b = arange(5,50)   # arg: [start,stop,steps] .......by default: steps = 50
print(b)

# creating array using ones()
x = ones(5)
print(x)
x = ones(10,int)
print(x)

# creating array using zeros()
x = zeros(5)
print(x)
x = zeros(10,int)
print(x)

# operation on array
a1 = array([1,2,3,4,5])
a2 = array([6,7,8,9,0])
a3 = a1+a2
print(a3)
print(a1+2)

# some numpy functions
print(sin(a1))
print(cos(a1))
print(sqrt(a1))
print(square(a1))
print(log(a1))
print(sum(a1))
print(min(a1))
print(max(a1))
print(sort(a1))
print(concatenate([a1,a2]))

# array copy
array1 = array([1,2,3,4,5])
array2 = array1
print(array1)
print(array2)
print(id(array1))
print(id(array2))

# using view() to get same array n diff memory loc [SHALLOW COPY]
s1 = array([6,9,1,3,0,2])
s2 = s1.view()
print(s1)
print(s2)
print(id(s1))
print(id(s2))
s1[2]=5
print(s1)
print(s2)
print(id(s1))
print(id(s2))

# using copy() to get same array n diff memory loc [DEEP COPY]
s1 = array([1,2,3,4,5,6])
s2 = s1.copy()
print(s1)
print(s2)
print(id(s1))
print(id(s2))
s1[2]=5
print(s1)
print(s2)
print(id(s1))
print(id(s2))