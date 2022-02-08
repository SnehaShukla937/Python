a = 5
b = 0

try:
    print(a/b)
except Exception:
    print("you can not divide any no. by zero")

##################################################

a = 9
b = 0

try:
    print(a/b)
except Exception as e:
    print("you can not divide any no. by zero!!!",e)

##################################################

a = 9
b = 0

try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("you can not divide any no. by zero!!!",e)
finally:
    print("resource close")

# if you don't know the error name ...simply use Exception as e and print e.
# e or Exception will give you an error name.
