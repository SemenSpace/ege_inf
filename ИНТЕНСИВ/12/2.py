def f(n):
    k = 0
    for i in str(n)[:-1]:
        k += int(i)
    for i in range(2, k//2):
        if k % i == 0:
            return 0
    return 1


for n in range(100):
    s = '>' + '0' * 39 + '1' * n + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    if f(s):
        print(n)
        break