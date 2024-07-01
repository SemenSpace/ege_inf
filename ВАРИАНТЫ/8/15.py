for A in range(1000):
    b = True
    for x in range(1000):
        for y in range(1000):
            F = (((y < 20) <= (x > 70)) or (not((x < A) <= (y > A))))
            if F == 0:
                b = False
    if b:
        print(A)
        break