f = open("13.txt")
n, s = map(int, f.readline().split())
f = sorted([list(map(int, i.split())) for i in f])

types = [s for i in range(10**8)]

k = 0
ostat = [0 for i in range(10**8)]
print(1)
for i in f:
    vid, mass = i
    if types[vid] - mass >= 0:
        k += 1
        types[vid] -= mass
    else:
        ostat[vid] += mass

mx = ostat.index(max(ostat))
print(n - k, mx)
