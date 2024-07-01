P = [i/10 for i in range(30, 381)]
Q = [i/10 for i in range(210, 571)]

A = set()
for x in range(0, 600):
    x /= 10
    F = (((x in Q) <= (x in P))) <= (x in A)
    if F == 0:
        A.add(x)

print(A)
print(min(A), max(A), (max(A) - min(A)))
