
for A in range(0, 10001):
    k = 0
    for x in range(0, 10001):
        if ((x % 2 == 0) <= (x % 3 != 0)) or ((x + A) >= 100):
            k += 1
    if k >= 10000:
        print(A)
        break