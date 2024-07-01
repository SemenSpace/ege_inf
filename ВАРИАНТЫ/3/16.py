from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + f(n - 1)

for i in range(0, 2124):
    f(i)

print(f(2124) - f(2122))