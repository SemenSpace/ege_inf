for i in range(201, 300):
    n = "1" * i
    while "111" in n or "222" in n:
        n = n.replace("111", "22", 1)
        n = n.replace("222", "1", 1)
    if n.count('1') == 0:
        print(i, n)
