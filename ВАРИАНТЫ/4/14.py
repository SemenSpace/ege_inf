n = 5 * 216**155 + 4 * 36**156 - 4 * 6**157 - 2023

s = ''
while n > 0:
    s += str(n % 6)
    n //= 6

print(s.count('0'))