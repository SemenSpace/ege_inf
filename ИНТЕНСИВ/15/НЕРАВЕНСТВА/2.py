for A in range(1000):
    b = True
    for x in range(100):
        for y in range(100):
            F = ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9))
            if F == 0:
                b = False
    if b:
        print(A)