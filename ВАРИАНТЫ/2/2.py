for A in range(0, 1000):
    k = 0
    for x in range(0, 1000):
        if (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0)):
            k += 1
    if k == 1000:
        print(A)
        break

for A in range(0, 1000):
    k = 0
    for x in range(0, 1000):
        if (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0)):
            k += 1
    if k == 1000:
        print(A)
        break
