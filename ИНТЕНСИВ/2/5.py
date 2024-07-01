print('w x y z  f1 f2')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f1 = int((x == y) and (w <= z))
                f2 = int((x <= y) <= (w == z))
                print(w, x, y, z, ' ', f1, f2)