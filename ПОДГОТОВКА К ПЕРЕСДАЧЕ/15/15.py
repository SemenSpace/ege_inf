A = set()
for P in range(69, 91 + 1):
    for Q in range(77, 114 + 1):
        if P == Q:
            A.add(P)
            A.add(Q)

print(A)