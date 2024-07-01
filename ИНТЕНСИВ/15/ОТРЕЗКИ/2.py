p = [i/10 for i in range(240, 770 + 1)]
q = [i/10 for i in range(470, 920 + 1)]
r = [i/10 for i in range(820, 1160 + 1)]

A = set()
for x in range(200, 1200):
    x /= 10
    F = ( (not((x in q) <= ((x in p) or (x in r)))) ) <= ( (not(x in A)) <= (not(x in q)) )
    if F == 0:
        A.add(x)

A = sorted(A)
print(max(A), min(A))