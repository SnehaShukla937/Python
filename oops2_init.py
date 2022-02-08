"""
SPECIAL VARIABLE =  __name__
SPECIAL METHOD = __init__

"""


class Computer1:
    def __init__(self):   # dont need to call this method manually
        print("hello !! this is init method.")

    def config(self):
        print("this is config file not init")


com1 = Computer1()   # this time init will be called automatically
com1.config()


# user passing arguments.

class Computer:
    def __init__(self,cpu,ram):  # variables are defined here
        self.cpu = cpu
        self.ram = ram

    def  con(self):
        print("config is:",self.cpu,self.ram)


c1 = Computer("i5",16)   # variables are called here
c2 = Computer("i8",32)

c1.con()
c2.con()