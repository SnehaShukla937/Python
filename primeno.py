num = int(input("enter no. to check:\t"))
for i in range(2,num):
    if num%i == 0:
        print("no. is not prime")
        break
else:
    print("no. is prime")