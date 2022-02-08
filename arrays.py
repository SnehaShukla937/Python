from array import *

x = array('i', [1, -2, 3, 4, 5, 8, 9, 5])
print(x)
print(x.buffer_info())  # will give address and size of array.
print(x.typecode)  # type of an array
print(x[2])

y = array('u', ['a', 'b', 'p'])
print(y)
print(y[0])

# print each element of array
newarr = array('i', [1, 2, 3, 4, 5])
print(newarr)
for i in newarr:
    print(i)

# arrays in sorted form
p = array('i', [2, 1, 0, 5, 3, 9, 4])
print(p)
q = list(p)
print(q)
print(type(q))
sorted_val = sorted(q)
print('sorted_val:',sorted_val)

# user input in an array
arr = array('i',[])
a = int(input("enter the length:\t"))
for i in range(a):
    x = int(input("enter val:"))
    arr.append(x)
print(arr)

l = int(input("enter value to search:\t"))
for i in arr:
    if l == i:
        pos = arr.index(l)
        print("value found in "+str(pos)+" position.")
        break
else:
    print("value not found")