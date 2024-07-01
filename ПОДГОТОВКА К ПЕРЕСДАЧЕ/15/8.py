for A in range(1, 1000):
    b = 1
    for x in range(1, 10000):
        F = (x & 107 == 0) <= ((x & 55 != 0) <= (x & A != 0))
        if F == 0:
            b = 0
            break
    if b:
        print(A)
        break