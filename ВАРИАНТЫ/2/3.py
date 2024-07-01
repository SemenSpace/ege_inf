alp_19 = '0123456789ABCDEFGHI'

for x in alp_19:
    n = int('321' + x + '4', 19) + int('498' + x + '9', 19)
    if n % 23 == 0:
        print(n)
        print(n // 23)