n = 7 * 512 ** 1912 + 6 * 64 ** 1954 - 5 * 8 ** 1991 - 4 * 8**1980 - 2022
print(oct(n).count('7'))
s = ''
while n > 0:
    s += str(n % 8)
    n //= 8

print(s.count('7'))
