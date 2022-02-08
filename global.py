a = 10   # global variable
def hello():
    a = 15  # local variable
    return a

print(hello())
print(a)

print("after removing local variable")
a = 10   # global variable
def hello():
    #a = 15  # local variable
    return a

print(hello())
print(a)

print("making local variable to global ")
a = 10   # global variable
def hello():
    global a
    a = 15  # local variable
    return a

print(hello())
print(a)


print("access all global variable in function")
a = 10   # global variable
b = 20    # global variable
print(id(a))
def hello():
    a = 15  # local variable
    b = 32 # local variable
    x = globals()['a']
    y = globals()['b']
    globals()['a'] = 90   # change global variable inside the function
    return a,b,x,y,id(x)

print(hello())
print(a)
