kol = 0

for i in range(1, 10**10):
    s = str(i)
    n1 = s.count("1")
    n2 = s.count("2")
    n3 = s.count("3")
    n4 = s.count("4")
    n5 = s.count("5")
    n6 = s.count("6")
    n7 = s.count("7")
    n8 = s.count("8")
    n9 = s.count("9")
    n0 = s.count("0")

    count = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9].count(1)
    if count == 0:
        kol += 1
    else:
        kol += count

print(kol)
