f = open("12.txt")
n = int(f.readline())
f = sorted([list(map(int, i.split())) for i in f])
raydi = [[0 for i in range(500)] for i in range(101)]

for i in range(n):
    r1, p1 = f[i]
    raydi[r1][p1] = 1

mx_rayd = []
mx_len = 0
for i in range(len(raydi)):
    k = 0
    mx = 0
    kon = raydi[i]
    for j in kon:
        if j == 1:
            k += 1
            mx = max(mx, k)
        else:
            k = 0

    mx_rayd.append([mx, i])


print(max(sorted(mx_rayd, reverse=True)), mx_len)
