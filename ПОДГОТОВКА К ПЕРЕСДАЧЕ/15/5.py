def d(n, m):
    if n % m == 0:
        return 1
    return 0


for A in range(1, 10000):
    b = 1
    for x in range(1, 5000):
        F = d(A, 7) and (d(240, x) <= ((not(d(A, x))) <= (not(d(780, x)))))
        if F == 0:
            b = 0
            break
    if b:
        print(A)
        break