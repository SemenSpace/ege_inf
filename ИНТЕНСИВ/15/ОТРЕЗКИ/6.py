P = [i/10 for i in range(170, 461)]
Q = [i/10 for i in range(220, 571)]


A = set()
for x in range(100, 601):
    x /= 10
    if ((not(x in A)) <= (((x in P) and (x in Q)) <= (x in A))) == 0:
        A.add(x)

print(-1 * (min(A) - max(A)))