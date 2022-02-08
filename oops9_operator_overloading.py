a = 5
b = 6
print(a+b)

# magic methods (operators works behind the seen)
print(int.__add__(a,b))
print(int.__mul__(a,b))
a = '5'
b = '6'
print(str.__add__(a,b))


class Student:
    def __init__(self,m1,m2):
        self.m1 =   m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        g1 = self.m1+other.m1
        g2 = self.m1+other.m2
        if g1>g2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)


s1 = Student(20,30)
s2 = Student(10,10)

s3 = s1+s2      # Student.__add__(s1,s2)

print(s3.m1,s3.m2)

if s1>s2:   # Student.__gt__(s1,s2)
    print("s1 more")
else:
    print("s2 more")

a = 8
print(a)
print(s1)       # s1.__str__(self)


# when you print an object without defining __str__(self) method ....you will get module name,class name,address of obj.
