#134*5*

for x in range(1, 10**6 + 1):
    if str(x)[:3] == "134" and '5' in str(x) and x % 63 == 0:
        print(x, x//63)