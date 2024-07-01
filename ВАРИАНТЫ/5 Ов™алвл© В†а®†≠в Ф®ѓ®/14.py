n = 2 * 729 ** 2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27 ** 2020 - 2 * 9**2022 - 2024

kon = []
while n > 0:
    kon.append(n%27)
    n //= 27

k = 0
for i in kon:
    if i > 9:
        k += 1

print(k)