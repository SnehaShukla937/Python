import functools


def square(a):
    return a**2


print(square(2))

# anonymous func (lambda)
f = lambda a: a**2
print(f(2))

f1 = lambda b,c:b+c
print(f1(3,4))

# FILTER - MAP - REDUCE

# Filter - used to filter data from list according to lambda function
lst = [1,2,3,4,5,6,7,8,9,0]

even = list(filter(lambda n:n%2 is 0,lst))
odd = list(filter(lambda n:n%2 is not 0,lst))
print(even,odd)
valuesMulNotZero = list(filter(lambda n:n*2 is not 0,lst))
print(valuesMulNotZero)

# Map - used to map or modify the list according to the lambda function
lst1 = [1,2,3,4,5,6,7,8,9,0]

x = list(map(lambda n:n-1,lst1))
y = list(map(lambda n:n*2,lst1))
print(x,y)

