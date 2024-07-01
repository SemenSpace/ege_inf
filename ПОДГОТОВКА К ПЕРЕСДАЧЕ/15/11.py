for A in range(1, 1000):
    b = 1
    for x in range(1000):
        for y in range(1000):
            F = (x > 39) or (y > 26) or (2*x + 4 * y < A)
            if F == 0:
                b = 0
                break
    if b:
        print(A)
        break