f = open("7.txt")
n, k, m = map(int, f.readline().split())
f = sorted([int(i) for i in f], reverse=True)

sale_20 = []
sale_10 = []

sale_remove_20 = []
sale_remove_10 = []

for i in range(k):
    sale_20.append(f[i] * 0.2)
    sale_remove_20.append(f[i])

for i in sale_remove_20:
    f.remove(i)

for i in range(m):
    sale_10.append(f[i] * 0.1)
    sale_remove_10.append(f[i])
for i in sale_remove_10:
    f.remove(i)


mx_without_sale = max(f)
print(mx_without_sale, sum(sale_20) + sum(sale_10))
