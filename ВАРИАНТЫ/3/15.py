for A in range(1, 1001):
    flag = 0
    for x in range(1, 1001):
        if ((x % 3 == 0) <= (x % 5 != 0)) or (x + A >= 90):
            flag += 1


    if flag >= 1000:
        print(A)
        break