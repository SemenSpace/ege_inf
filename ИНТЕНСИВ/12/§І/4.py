for i1 in range(1, 50):
    for i2 in range(1, 50):
        for i3 in range(1, 50):
            n = "0" + '1'*i1 + '2'*i2 + '3'*i3 + "0"
            n1 = n
            while "00" not in n:
                n = n.replace("01", "210", 1)
                n = n.replace("02", "320", 1)
                n = n.replace("03", "3012", 1)

            if n.count('1') == 26 and n.count('2') == 54 and n.count('3') == 48:
                print(len(n1), n1)
                break
