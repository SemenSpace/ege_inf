f = open('КОНФЕРЕНЦЗАЛ.txt')
N = int(f.readline())
f = sorted([[int(i.split()[1]), int(i.split()[0])] for i in f])

print(f)
proshli = [f[0]]
for i in range(1, N):
    if f[i][1] >= proshli[-1][0]:
        proshli.append(f[i])

print(len(proshli))
print(proshli[-2])

for i in range(N):
    if f[i][1] >= 989:
        print(f[i])