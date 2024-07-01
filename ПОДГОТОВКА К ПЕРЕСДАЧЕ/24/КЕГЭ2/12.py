f = open('12.txt')
f = [str(i) for i in f]
k = 0
for i in f:
    if i.count('AOA') > i.count('OAO'):
        k += 1
print(k)