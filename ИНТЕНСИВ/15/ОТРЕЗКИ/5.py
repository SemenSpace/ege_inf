for A in range(1, 10000):
    b = True
    for x in range(1000):
        if ((not((x % A) == 0)) <= ((not((x % 21) == 0)) and (not((x % 35) == 0)))) == 0:
            b = False
    if b:
        print(A)

