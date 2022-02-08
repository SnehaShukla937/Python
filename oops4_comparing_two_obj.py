class Computer:
    def __init__(self):
        self.name = "Sneha"
        self.age = 80

    def update(self):
        self.age = 35

    def comapare(self,other):
        if self.age is other.age:
            return True
        else: return False

c1 = Computer()
c2 = Computer()

c2.update()   # this will change the age of obj2.

if c1.comapare(c2):
    print("same")
    print(c1.age,c2.age)
else:
    print("not same")
    print(c1.age, c2.age)