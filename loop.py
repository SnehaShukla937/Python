# simple while loop
i = 1
while i <= 100:
    if i % 3 == 0 or i % 5 == 0:
       pass
    else:
        print(i)
    i += 1

# pattern print
i = 1
while i<=5:
    j = 1
    while j<=5:
        print("#",end="")
        j += 1
    print()
    i += 1

# for loop with string
x = 'sneha'
for i in x:
    print(i)

# for loop with list
for x in ['a','b','c']:
    print(x)

# for loop with tuple
for x in ('a','b','c'):
    print(x)

# for loop with range
for i in range(0,5):
    print(i)

# print all perfect square bet 1 tp 500
for i in range(1,int(500**0.5)+1):
    z = i**2
    print(z)

# pattern print using for loop
for i in range(4):
    for j in range(4):
        print("#",end = "")
    print()

for i in range(5):
    for j in range(i):
        print("#", end="")
    print()
print('nxt')
for i in range(5):
    for j in range(5-i):
        print("#", end="")
        j -= 1
    print()
print('nxt')
for i in range(1,5):
    for j in range(5-i):
        print(j+i, end="")
    print()

### for-else ####

for i in range(1,10):
    if i % 2 == 0:
        print(i)
        break  # imp
else:
    print("no action")