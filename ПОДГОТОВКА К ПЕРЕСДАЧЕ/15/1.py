def f(n, m):
    if n % m == 0:
        return 1
    return 0

for A in range(1, 1000):
    b = 1
    for x in range(1, 1000):
        F = (f(x, A) and f(x, 24) and (not(f(x, 16)))) <= (not(x, A))
        if F == 0:
            b = 0
    if b:
        print(A)