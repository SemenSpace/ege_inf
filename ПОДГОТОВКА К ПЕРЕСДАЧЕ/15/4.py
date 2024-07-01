def mod(m, n):
    return m % n


for A in range(1, 10000):
    b = 1
    for x in range(10000):
        F = ((mod(x, 4) != 3) or (mod(x, 6) != 1)) <= (mod(x, 36) != A)
        if F == 0:
            b = 0
            break
    if b:
        print(A)
        break