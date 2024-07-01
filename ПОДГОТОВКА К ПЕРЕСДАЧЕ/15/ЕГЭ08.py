def f(n, m):
    if n % m == 0:
        return 1
    return 0

B = [i for i in range(70, 91)]


for A in range(1, 1000):
    b = 1
    for x in range(1, 1000):
        F = f(x, A) or ((x in B) <= (not(f(x, 22))))
        if F == 0:
            b = 0
            break
    if b:
        print(A)
