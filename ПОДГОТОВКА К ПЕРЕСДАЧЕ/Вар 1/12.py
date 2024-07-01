mx = 0
for x in range(200):
    for y in range(200):
        for z in range(200):
            A = '0' + '1' * x + '2' * y + '3' * z + '0'
            if len(A) == 200:
                while '00' not in A:
                    A = A.replace('011', '201', 1)
                    A = A.replace('03', '220', 1)
                    A = A.replace('02', '210', 1)
                    A = A.replace('012', '2101', 1)
                    A = A.replace('013', '12101', 1)
                    A = A.replace('010', '1100', 1)
                if A.count('1') == 220 and A.count('2') == 197:
                    mx = max(mx, (x + y * 2 + z * 3))

print(mx)
