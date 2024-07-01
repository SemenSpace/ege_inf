count = 0

for A in range(1000):
    k = 1

    for x in range(100):
        for y in range(100):
            F = (((x < 5) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 5)))
            if F == 0:
                k = 0

    if k:
        count += 1

print(count)
