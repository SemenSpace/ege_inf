f = open('17.txt').readline().replace('C', '*').replace('A', '*')

kon = [0] * len(f)
for i in range(2, len(f)):
    if f[i - 2] == '*' and f[i] == '*':
        kon[i] = kon[i - 3] + 1

print(max(kon))