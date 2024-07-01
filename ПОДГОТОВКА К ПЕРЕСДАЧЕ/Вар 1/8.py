def f(n):
    s = n
    k = ''
    while s > 0:
        k += str(s%8)
        s //= 8

    return k


count = 0
for i in range(10**7, 10**8):
    s2 = bin(i)[2:]
    s8 = f(i)
    if len(s8) == 16:
        if '111' not in str(s2):
            flag = 1
            for j in range(len(s8) - 1):
                if (int(s8[j]) + int(s8[j + 1])) % 2 == 0:
                    flag = 0
                    break

            if flag:
                count += 1

print(count)