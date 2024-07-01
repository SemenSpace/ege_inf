def s(n):
    summa = 0
    for i in n:
        summa += int(i)
    if summa % 2 == 0:
        return 1
    else:
        return 2

kon = []
for N in range(1, 100):
    R = bin(N)[2:]
    if s(R) == 1:
        R = R + "0"
        R1 = "1" + R[2:]
    if s(R) == 2:
        R += "1"
        R1 = "11" + R[2:]

    R = int(R1, 2)
    print(N, R)
    if R > 49:
        kon.append([R, N])

print(sorted(kon))