for i in range(0, 10):
    if i == 5:
        break  # will stop execution in the loop at i =5 and jump out of the loop
    print(i)

print('1st loop sneha')

for i in range(0, 10):
    if i == 5:
        continue  # will skip execution in the loop for i = 5 and continue for next iteration in loop
    print(i)

print('2nd loop sneha')

for i in range(0, 10):
    if i == 5:
        pass  # will just ignore the condition and continue in loop
    print(i)

print('3rd loop sneha')
