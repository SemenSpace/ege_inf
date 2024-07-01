print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = ((x or y) <= (y and z)) and ((w == x) or (w <= (not(z)) ))
                if F == 1:
                    print(w, x, y, z)
