def f(n, k):
    if n == k:
        return 1
    if n > k or n == 15:
        return 0
    else:
        return f(n + 1, k) + f(n + 2, k) + f(n * 3, k)


print(f(2, 11) * f(11, 16))