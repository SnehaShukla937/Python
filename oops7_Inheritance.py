# 1. SINGLE LEVEL INHERITANCE


class A:        # Parent/super class
    def fet1(self):
        print("fet1 working")

    def fet2(self):
        print("fet2 working")


class B(A):         # child/sub class: inherit all the features of class A.
    def fet3(self):
        print("fet3 working")

    def fet4(self):
        print("fet4 working")

a1 = A()
b1 = B()

a1.fet1()
a1.fet2()
b1.fet1()
b1.fet2()
b1.fet3()
b1.fet4()

# 2. MULTI LEVEL INHERITANCE


class A:        # Parent/super class
    def fet1(self):
        print("fet1 working")

    def fet2(self):
        print("fet2 working")


class B(A):         # child/sub class OF A: inherit all the features of class A.
    def fet3(self):
        print("fet3 working")

    def fet4(self):
        print("fet4 working")


class C(B):         # child/sub class OF B: inherit all the features of class B and A.
    def fet5(self):
        print("fet5 working")


a1 = A()
b1 = B()
c1 = C()

a1.fet1()
a1.fet2()
b1.fet1()
b1.fet2()
b1.fet3()
b1.fet4()
c1.fet1()
c1.fet2()
c1.fet3()
c1.fet4()
c1.fet5()

# 3.MULTIPLE INHERITANCE


class A:        # Parent/super class
    def fet1(self):
        print("fet1 working")

    def fet2(self):
        print("fet2 working")


class B:         # 2ND PARENT CLASS
    def fet3(self):
        print("fet3 working")

    def fet4(self):
        print("fet4 working")


class C(A,B):         # child/sub class OF A and B: inherit all the features of class B and A.
    def fet5(self):
        print("fet5 working")

        
a1 = A()
b1 = B()
c1 = C()

a1.fet1()
a1.fet2()
b1.fet3()
b1.fet4()
c1.fet1()
c1.fet2()
c1.fet3()
c1.fet4()
c1.fet5()
