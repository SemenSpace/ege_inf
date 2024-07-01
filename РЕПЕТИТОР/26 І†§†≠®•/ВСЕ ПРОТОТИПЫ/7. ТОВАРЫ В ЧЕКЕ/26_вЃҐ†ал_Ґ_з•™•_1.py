file = open('26_ТОВАРЫ_В_ЧЕКЕ.txt')
n = int(file.readline())
f = [int(i) for i in file]
f.sort(reverse=True)
all_sum = sum(f)

sale_sum = 0
for i in range(2, n, 3):
    sale_sum += f[i]

print(all_sum - sale_sum)