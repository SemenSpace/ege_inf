for A in range(10000):
    B = True
    for x in range(10000):
        if ((x & 77 != 0) <= ((x & 12 == 0) <= (x & A != 0))) != 1:
            B = False
    if B:
        print(A)
        break