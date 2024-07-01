def f(n, k):
    if n == k:
        return 1
    if n > k:
        return 0
    else:
        return f(n + 1, k) + f(n * 3, k) + f(n + 2, k)

print(f(1, 10) * f(10, 12) * f(12, 15))