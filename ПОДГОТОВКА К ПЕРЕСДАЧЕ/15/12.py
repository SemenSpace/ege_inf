for A in range(1, 1000):
    b = 1
    for x in range(1000):
        for y in range(1000):
            F = (2 * x + y != 70) or (x < y) or (A < x)
            if F == 0:
                b = 0
                break

    if b:
        print(A)
