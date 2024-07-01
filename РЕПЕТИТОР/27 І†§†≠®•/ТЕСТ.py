a = [21, 13, 9, 19, 17, 26, 95]
mx = 10**10
n = 7

for i in range(n - 1):
    for j in range(i + 1, n):
        s = a[i:j]
        if sum(s) % 43 == 0:
            mx = min(len(s), mx)

print(mx)
