# METHOD OVERLOADING  :  (NO. OF ARG CAN BE VARIED BUT METHOD NAME IS SAME)

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a,b):      # when no. of arg are fixed
        s = a+b
        return s

    def sum2(self,*val):        # when no. of arg are diff.(variable length arg)
        s = 0
        for i in val:
            s += i
        return s


s1 = Student(10,20)
print(s1.sum(1,1))
print(s1.sum2(2,3,4,5))

class Student2:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a = None,b = None,c = None):
        s = 0
        if a is not None and b is not None and c is not None:
            s = a+b+c
        elif a is not None and b is not None:
            s = a+b
        else: s = a
        return s



s1 = Student2(10,20)
print(s1.sum(1,1),s1.sum(3),s1.sum(1,2,3))


# METHOD OVERRIDING :


class A:
    def show(self):
        print("In A show")
class B(A):
    pass

a1 = B()
a1.show()  # when B has no method show()....it will inherit from A and print it.


class A1:
    def show(self):
        print("In A show")
class B1(A1):
    def show(self):
        print("In B show")
a1 = B1()
a1.show()   # when B has  method show()....it will print it.

### B's show() method overriding A's show() method.