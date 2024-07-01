def f(n, m):
    if n % m == 0:
        return 1
    return 0

for A in range(1, 1000):
    b = True
    for x in range(1, 1000):
        F = (((f(72, x)) <= (not(f(90, x)))) or ((A - x) > 80))
        if F == 0:
            b = False
    if b:
        print(A)
        break