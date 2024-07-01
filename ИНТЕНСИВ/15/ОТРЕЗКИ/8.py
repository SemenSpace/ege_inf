for x in [k for k in range(-10000,10000)]:
    P = 3 <=x<= 13
    Q = 12 <=x<= 22
    A = 1
    f = ((A<=P) or Q)
    if f != 0:
        print(x)