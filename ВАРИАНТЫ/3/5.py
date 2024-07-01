konnn = []

for N in range(0, 1000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-3:]
    if N % 3 != 0:
        R = R + bin((N % 3)*3)[2:]

    kon = int(R, 2)
    if kon <= 170:
        konnn.append(kon)


print(max(konnn))