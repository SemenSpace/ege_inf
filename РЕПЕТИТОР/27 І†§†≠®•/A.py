f = open('test.txt')
n = int(f.readline())
a = [int(i) for i in f]

res = 0
kon = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if a[i] > a[j] and a[k] > a[j]:
                res = max(res, a[i] + a[k] - 2*a[j])
                print(a[i], a[j], a[k])

print(res)