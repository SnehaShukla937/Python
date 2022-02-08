def greet():
    print("hello")


greet()


def add(x,y):
    z = x+y
    z1 = x - y
    return z,z1


print(add(2,3))

# there is no concept of pass by value or pass by reference in python.

# actual argument = position, keyword, default, variable length


def person(name, age):  # position
    return name,age


print(person('sneha',25))


def person(name, age):  # keyword
    return name,age


print(person(age = 27, name = 'neha'))


def person(name, age = 15):  # default
    return name,age


print(person('golu'))
print(person('golu',30))  # age 30 (actual arg) will override on 15 (formal arg).


def person(name, *age):  # variable length  [type of variable arg = tuple]
    return name,age


print(person('sneha',22,26,25))


def sum(a,*b):  # variable length
    c = a
    for i in b:
        c = c+i
    return c,type(a),type(b)


print(sum(3,4,5,6,7))  # b can be of any length tuple.


# KEYWORD VARIABLE LENGTH ARGUMENT    [type of variable arg = dict]

def person(name,*data):  # variable length
    return name,data,type(name),type(data)


print(person('sneha','female',26,'mumbai'))


def person1(name,**data):  # keyword variable length
    return name,data,type(name),type(data)


print(person1('sneha',gender = 'female',age = 26,city = 'mumbai'))


def person2(name,**data):  # keyword variable length
    print(name)
    for i ,j in data.items():
        print(i,j)


print(person2('sneha',gender = 'female',age = 26,city = 'mumbai'))

#  PASS LIST INSIDE A FUNC
lst = [2,3,4,5,6]  # count even odd


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 is 0:even += 1
        else:odd += 1
    return even,odd


even,odd = count(lst)
print("even counts:{} and odd counts:{}".format(even,odd))