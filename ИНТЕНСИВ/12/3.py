for n3 in range(300, 510):
        for n2 in range(500, 510):
            for n1 in range(100):
                a = '0' + n3*'3' + n2*'2' + n1*'1' + '0'
                while '00' not in a:
                    a = a.replace('033', '1302', 1).replace('03', '120', 1).replace('023', '203', 1).replace('02', '20', 1)
                if a.count('1') == 340 and a.count('2') == 849 and a.count('3') == 151:
                    print(n2)
