for N in range(1000):
    n2 = str(bin(N)[2:])
    s = sum([int(i) for i in n2])
    n2 = n2 + str(s % 2)
    s = sum([int(i) for i in n2])
    n2 = n2 + str(s % 2)
    R = int(n2, 2)
    if R > 85:
        print(R, N)
