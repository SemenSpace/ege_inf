for A in range(1, 1000):
    k = 0
    for x in range(1000):
        if (not((x % A) == 0)) <= (((x % 14) == 0) <= (not((x % 4) == 0))):
            k += 1
    if k >= 1000:
        print(A)