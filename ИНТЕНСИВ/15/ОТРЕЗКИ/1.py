for A in range(100):
    k = 0
    for x in range(1000):
        for y in range(1000):
            if ((5 * x + 3 * y) != 60) or ((A > x) and (A > y)):
                k += 1
    if k >= 1000*1000:
        print(A)
        break