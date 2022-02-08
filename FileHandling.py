filename = 'MyData.txt'

f = open(filename,'r')      # will open file {open(filename,mode of operation)}
print(f.read())             # will read data from file.
print(f.readline())         # will read only one line.
print(f.readline())         # will read 2nd line.
print(f.readline(10))       # will read only first 10 char.
f.close()

f = open(filename,'r')  # will open file in read mode (if there is no such file then error)
f1 = open('abc','w') # will open file in write mode (if there is no such file then it will be created automatically in write mode)
f1.write("automatically generated file")
f1.write("\nhello world")

for data in f:  # copying data from f to f1
    f1.write(data)
f1.close()
f.close()

f2 = open('img.jpg','rb') # open image file in read-binary mode
for i in f2:
    print(i)

f3 = open('img2.jpg','wb')
for i in f2:
    f3.write(i)
f2.close()
f3.close()

