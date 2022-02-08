class Computer:   # class name is Computer.
    def config(self):       # self is an argument for object com1.
        print("i5,16gb,1tb")


com1 = Computer()    # com1 is an object of class Computer.
Computer.config(com1)
# com1.config()
print(type(com1))  # will print type of object com1.

com2 = Computer()
Computer.config(com2)  # or com2.config()
com2.config()


class Person:
    def info(self):
        print("Sneha Shukla")


obj1 = Person()
obj2 = Person()

obj1.info()
obj2.info()