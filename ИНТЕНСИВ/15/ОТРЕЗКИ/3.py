for A in range(1000):
    B = True
    for x in range(10000):
        if (x & 85 != 0 or (x & 54 == 0 or x & A != 0)) == 0:
            B=False
    if B:
        print(A)
        break