count = 0
for A in range(1000):
    b = True
    for x in range(200):
        for y in range(200):
            F = ((x < 5) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 5))
            if F == 0:
                b = False
    if b:
        count += 1

print(count)