n = 729**6 - 3**20 + 90
new = ''
while n > 0:
    new += str(n%9)
    n //= 9
print(new.count('0'))