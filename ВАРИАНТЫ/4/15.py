kon = []
for A in range(40, 100):
    s = 0
    for x in range(0, 999):
        for y in range(0, 999):
            if (x < A) or (y < A) or ((x + 2*y) > 150):
                s += 1

    if s >= 999*999:
        print(A)
        break