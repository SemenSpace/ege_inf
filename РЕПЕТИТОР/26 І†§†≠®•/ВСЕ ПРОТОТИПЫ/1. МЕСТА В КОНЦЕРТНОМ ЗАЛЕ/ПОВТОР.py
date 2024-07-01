f = open('26_1.txt')
N = int(f.readline())
f = sorted([list(map(int, i.split())) for i in f])

last = 0
kaif = [f[0]]

for i in range(1, N):
    if f[i][0] == f[i - 1][0] and f[i][1] - f[i - 1][1] == 3:
        kaif.append([f[i - 1], f[i]])

print(kaif)
print(8631, 7311)
