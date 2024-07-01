f = open('10.txt')
f = [str(i).strip() for i in f]
k = 0
for i in f:
    B = i.count('B')
    A = i.count('A')
    if B / A >= 1.05:
        k += 1
print(k)