def f(n):
    if n == 2:
        return 1
    if n > 2:
        return 4 * f(n - 1) + 2 * g(n - 1) - n * 3 + 8


def g(n):
    if n == 2:
        return 1
    if n > 2:
        return 3 * f(n - 1) + 3 * g(n - 1) + n


print(f(16) + g(16))

