f = open('9.txt')
f = [str(i).strip() for i in f]

k = 0
for i in f:
    if i.count('S') == i.count('X'):
        k += 1
print(k)