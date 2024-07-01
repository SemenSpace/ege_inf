file = open('26-90.txt')
n = int(file.readline())
f = [int(i) for i in file]

f.sort()
sum_for_shop = sum([f[i] for i in range(0, n // 4)]) * 0.5 + sum([f[i] for i in range(n // 4, n)])
sum_for_consum = sum([f[i] for i in range(-2500, 0)]) * 0.5 + sum([f[i] for i in range(0, 7500)])

print(int(sum_for_consum), int(sum_for_shop))


