f = open('27_test.txt')
n = int(f.readline())
f = [int(i) for i in f]

# n - index + nach_pynkt

pynkti = []
for i in range(n):
    nach_pynkt = f[i]
    a = {}
    for j in range(n//2 + 1):
        a[j] = 0

    pynkti.append(a)


print(pynkti)