f = open("26_3.txt")
s, n = list(map(int, f.readline().split()))
f = sorted([int(i) for i in f])

count = 0
last = []
ost = s
for i in range(n):
    if s - f[i] > 0:
        count += 1
        last.append(f[i])
        s -= f[i]
    else:
        print(last)
        print(s)
        print(f)
        break


print(count, ost)