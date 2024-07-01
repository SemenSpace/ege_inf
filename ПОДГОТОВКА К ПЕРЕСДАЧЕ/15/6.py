for A in range(1, 1000):
    b = 1
    for x in range(1, 100000):
        F = ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & A != 0))
        if F == 0:
            b = 0
            break
    if b:
        print(A)
        break