d = [0 for i in range(1000)]

for N in range(1, 200):
    R = str(bin(N)[2:])
    R = R + str(bin(N % 4)[2:])
    R = int(R, 2)
    d[R] = 1

mx = -1
# d - Доступные числа
for i in range(1000- 49):
    mx = max(mx, sum(d[i:i+49]))

print(mx)