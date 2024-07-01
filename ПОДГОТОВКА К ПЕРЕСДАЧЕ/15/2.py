def f(x, A):
    if x % A == 0:
        return 1
    return 0

for A in range(1, 5000):
    b = 1
    for x in range(1, 50000):
        F = ((not(f(x, 84))) or (not(f(x, 90)))) <= (not(f(x, A)))
        if F == 0:
            b = 0
    if b:
        print(A)
        break