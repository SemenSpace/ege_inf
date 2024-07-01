f = open('26.txt')
n = int(f.readline())
f = [int(i) for i in f]

f.sort(reverse=True)

ln = [f[0]]
for i in range(1, n):
    if ln[-1] - f[i] >= 4:
        ln.append(f[i])

print(len(ln), ln[-1])