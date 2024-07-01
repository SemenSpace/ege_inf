f = open('08.txt')
n, s = map(int, f.readline().split())
f = sorted([[int(i.split()[1]) + int(i.split()[2]) + int(i.split()[3]), int(i.split()[4]), int(i.split()[0])] for i in f], reverse=True)

prohod = 0
poly_prohod = 0

poly_prohod = f[s][0]

for i in sorted(f):
    if i[0] > poly_prohod:
        prohod = i[2]
        break

k = 0
for i in f:
    if i[0] == poly_prohod:
        k += 1
print(prohod, k)