f = open("27_A.txt")
n = int(f.readline())
a = [int(f.readline())*3 for i in range(n)]
s = [0] * n
sum = 0
right, left = 0, 0

for i in range(1, n // 2):
    sum += a[i] * i + a[n - i] * i
    right += a[i]
    left += a[n - i]

sum += a[n // 2] * n // 2
s[0] = sum
for i in range(1, n):
    s[i] = s[i - 1] + left + a[i - 1] - right - a[(i + (n // 2) - 1) % n]
    right = right - a[i] + a[(i + (n // 2) - 1) % n]
    left = left - a[(i + (n // 2)) % n] + a[i - 1]
print(min(s))
