class A:
    def __init__(self):
        print("init A")

    def fet1(self):
        print("fet1 work")


class B(A):
    def __init__(self):
        super().__init__()   # will call the init method of super class A.
        print("init B")

    def fet2(self):
        print("fet2 work")


a = A()  # will call init A
a.fet1()

a1 = B()    # will first call init of B(if present) otherwise call init A
a1.fet1()
a1.fet2()

# 1. a child class object  will first call init of child(if present) otherwise call init of parent.
# 2. super() is used to call any method of super class
# super().methodname()
