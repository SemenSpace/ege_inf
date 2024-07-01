def f(n, k):
    if n == k:
        return 1
    if n > k:
        return 0
    else:
        return f(n + 1, k) + f(n + 2, k) + f(n * 2, k)

print(f(4, 11) * f(11, 13) * f(13, 15))