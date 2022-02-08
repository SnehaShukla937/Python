x = int(input("enter x:\t"))
if x>0:
    print("no. is +ve")
elif x==0:
    print("no. is 0")
else:
    print("no. is -ve")

y = int(input("enter y:\t"))
z = int(input("enter z:\t"))
if x>y:
    if x>z:
        print("x is greater")
    else:
        print("z is greater")
else:
    if y > z:
        print("y is greater")
    else:
        print("z is greater")