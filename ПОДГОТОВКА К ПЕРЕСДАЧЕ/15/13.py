for A in range(1000):
    b = 1
    for x in range(1000):
        for y in range(1000):
            F = (x**2 - 10*x + 16 > 0) or (y**2 - 10*y + 21 > 0) or (x*y < 2 * A)
            if F == 0:
                b = 0
                break
    if b:
        print(A)
        break
