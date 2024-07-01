for n in range(1, 1000):
    nn = bin(n)[2:]
    nn = nn + str(sum([int(i) for i in nn]) % 2)
    nn = nn + str(sum([int(i) for i in nn]) % 2)
    if int(nn, 2) > 55:
        print(int(nn, 2))
