for A in range(1, 1000):
    b = 1
    for x in range(1000):
        for y in range(1000):
            F = (x + y <= 30) or (y <= x + 2) or (y >= A)
            if F == 0:
                b = 0

    if b:
        print(A)