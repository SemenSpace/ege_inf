def prost(x):
    delit = 0
    for i in range(2, x//2):
        if x % i == 0:
            return 0
    return 1



kon = []
for one in range(0, 100):
    for two in range(0, 100):
        s = '0' + '1'*one + '2'*two
        n = s
        if len(s) > 44:
            while "01" in s or "02" in s:
                s = s.replace("02", "1110", 1)
                s = s.replace("01", "220", 1)
            if prost(sum([int(i) for i in s])):
                kon.append([sum([int(i) for i in n]), n])
print(kon)
print(min(kon))