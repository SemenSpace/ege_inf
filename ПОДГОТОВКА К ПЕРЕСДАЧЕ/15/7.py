for A in range(2, 1000):
    b = 1
    for x in range(0, 10000):
        F = (( (x & 13 != 0) or (x & A != 0) ) <= (x & 13 != 0) ) or ((x & A != 0) and (x & 39 == 0))
        if F == 0:
            b = 0
            break
    if b:
        print(A)