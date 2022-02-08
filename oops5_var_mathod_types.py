# two types of variables: class var or static var (outside init) , Instance var (inside init)
class Clothes:
    size = 'Large'  # class var (stored in class namespace)

    def __init__(self):  # instance var (stored in instance namespace)
        self.color = 'black'
        self.no = 40


obj1 = Clothes()
obj2 = Clothes()

print(obj1.size,obj1.color,obj1.no)
obj1.color = 'red'
obj1.size = 'xl'
print(obj1.size,obj1.color,obj1.no)
print(obj2.size,obj2.color,obj2.no)

####################################################################################

# two types of methods: instance,class,static

print("\nMETHODS\n")
class Student:
    school = 'Telusko'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # instance method:  working with instance variable
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):   # getter or accessor (instance method) : only fetch values.
        return self.m1

    def set_m1(self,val):   # setter or mutator (instance method): update the values.
        self.m1 = val

    @classmethod
    def info(cls):  # class method : working with class variable
        return cls.school

    @staticmethod
    def schinfo():   # static method: not concerned with any var,no arg will pass.
        print("this is static method")



obj1 = Student(1,2,3)
obj2 = Student(5,5,5)

print(obj1.avg(),obj2.avg())    # calling instance method using object/instance.
Student.schinfo()         # calling static method using class.
Student.school = 'edureka'
print(Student.info())           # calling class method using class.
