def f(start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if start < end:
        return f(start + 1, end) + f(int('1' + str(bin(start))[2:], 2), end)


print(f(1, int('1111111', 2)))