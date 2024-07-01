for A in range(1, 1000):
    b = 1
    for x in range(1000):
        for y in range(1000):
            F = (x * y > A) and (x > y) and (x < 8)
            if F == 1:
                b = 0
                break
    if b:
        print(A)
        break