file = open('27-B_3231.txt')
n = int(file.readline())
f = [int(i) for i in file]

nach = sum([f[i]*min(i, n-i) for i in range(n)])

kon = [f[0]]
for i in range(1, n*3):
    kon.append(kon[i - 1] + f[i % n])

mx = 10**200
index = 0
for i in range(n, n*2):
    nach = nach - kon[i + n//2] + kon[i] + kon[i] - kon[i - n//2]
    if nach < mx:
        mx = nach
        index = i
print(index)