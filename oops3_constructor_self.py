# __init__ is a constructor.


class Computer1:
    pass


c1 = Computer1()
c2 = Computer1()

print(id(c1))
print(id(c2))

# every object has their own memory location.
# size of object in memory depends upon  no. of variables.
# CONSTRUCTOR is responsible to allocate or decide object size (no. of variables).

class Computer:
    def __init__(self):
        self.name = "sneha"
        self.age = 20

    def update(self):
        self.age = 40


obj1 = Computer()
obj2 = Computer()

print(obj1.name)
print(obj2.age)

obj1.name = 'neha'
obj2.age =23
print(obj1.name)  # modified outside the class
print(obj2.age)  # modified outside the class
print(obj2.name)
print(obj1.age)


obj2.name = 'rashi'
obj2.age = 34
print(obj2.name,obj2.age)

obj2.update()

print(obj2.name,obj2.age)
