def f(n, m):
    if n % m == 0:
        return 1
    return 0


for A in range(1, 10000 + 1):
    b = 1
    for x in range(1, 1000):
        F = (f(x, 15) and (not(f(x, 21)))) <= ((not(f(x, A))) or (not(f(x, 15))))
        if F == 0:
            b = 0

            break

    if b:
        print(A)
        break