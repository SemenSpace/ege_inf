import os
def prost(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return 0
    return 1


f = open('3.txt')
f = [int(i) for i in f]


count = 0
mx = []

max_17 = 0
for i in sorted(f, reverse=True):
    if i % 100 == 17:
        max_17 = i
        break

k = 0
for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    if (prost(s1)) + (prost(s2)) == 1:
        if (s1 + s2) % max_17 ==  0:
            mx.append(s1 * s2)
    if i % 100000 == 0:
        k += 1
        print(k)

print(len(mx), max(mx))
