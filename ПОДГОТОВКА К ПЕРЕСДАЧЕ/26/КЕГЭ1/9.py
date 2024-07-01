f = open('9.txt')
n = int(f.readline())
f = sorted([int(i) for i in f])

k = 0
mass = 0
next_m = 0
for i in range(1, len(f)):
    mass += f[i - 1]
    k += 1
    next_m = f[i]
    if (next_m - mass) <= 1:
        pass

    else:
        print(mass + 1, k)
        break