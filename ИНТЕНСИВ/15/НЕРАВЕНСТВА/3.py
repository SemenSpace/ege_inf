count = 0
for A in range(1000):
    b = True
    for x in range(1000):
        for y in range(1000):
            F = ((x < 6) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 6))
            if F == 0:
                b = False
                break
        if not(b):
            break
    if b:
        count += 1

print(count)