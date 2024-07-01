def f(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return f(n - 1) + 2*n - 1
    if n % 2 == 0:
        return 4 * f(n / 2)


for a in range(1000):
    for b in range(1000):
        if (f(a) - f(b)) == 1001:
            print(a - b)