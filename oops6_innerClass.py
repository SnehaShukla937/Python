class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop('HP','i3',32)      # defining object of inner class lap.

    def show(self):
       print(self.name,self.roll)
       print(self.lap.show())           # calling method of inner class.

    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            return self.brand,self.cpu,self.ram


obj1 = Student('SNEHA',1)
obj2 = Student('Neha',2)

obj1.show()
obj2.show()

