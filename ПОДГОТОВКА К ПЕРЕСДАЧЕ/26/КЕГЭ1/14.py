f = open('14.txt')
n, k = map(int, f.readline().split())
f = sorted([[int(i.split()[1])//int(i.split()[0]), int(i.split()[1]), int(i.split()[0])]for i in f])

k2 = []
kon = [[] for i in range(10**7)]
for i in f:
    kon[i[0]].append([i[1], i[2]])
mass = 0
mx = 0
for i in kon:
    if k > 0:
        for x in sorted(i, reverse=True):
            if k > 0:
                if x != []:
                    k -= 1
                    mass += x[1]
                    mx = max(mx, x[1])
                    k2.append(x)

    else:
        break

price = 0
for x in k2:
    if str(x[1]) == str(mx):
        print(x)
        price = max(price, x[0])
print(mass, price)
