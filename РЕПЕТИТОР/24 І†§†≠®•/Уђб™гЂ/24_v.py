# f = open("24_demo2021.txt")
# s = f.readline()
# cnt = 1
# max_cnt = 1
# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         cnt += 1
#     else:
#         cnt = 1
#     max_cnt = max(cnt, max_cnt)
# print(max_cnt)

# f = open("24_open_kim2021.txt")
# s = f.readline()
# a = s.split("XZZY")
# print(len(max(a, key=len)) + 6)

# f = open("24_open_kim2021.txt")
# s = f.readline()
# s = s.replace("XZZY", "XZZ ZZY")
# a = s.split()
# print(len(max(a, key=len)))


# f = open("24_aprobation2021.txt")
# s = f.readline()
# s = s.replace("G", " ")
# s = s.replace("W", " ")
# s = s.replace("P", " ")
# a = s.split()
# print(len(max(a, key=len)))

# f = open("24_ege2021.txt")
# s = f.readline()
# s = s.replace("ad", "a d")
# s = s.replace("da", "d a")
# a = s.split()
# print(len(max(a, key=len)))

# f = open("24_demo2022.txt")
# s = f.readline()
# s = s.replace("PP", "P P")
# a = s.split()
# print(len(max(a, key=len)))


# f = open("24_aprobation_2022_1.txt")
# s = f.readline()
# s = s.replace("AB", "AC")
# for i in range(1, 10000):
#     if i*"AC" in s:
#         print(i)

# f = open("24_aprobation_2022_2.txt")
# s = f.readline()
# s = s.replace("BA", "DA")
# for i in range(1, 10000):
#     if i*"DA" in s:
#         print(i)


# f = open("24_ege2022_day1.txt")
# s = f.readline()
# s = s.replace("A", "O")
# s = s.replace("B", "C")
# s = s.replace("D", "C")
# for i in range(1, 1000):
#     if i*"CO" in s:
#         print(i)


# f = open("24_ege2022_day2.txt")
# s = f.readline()
# s = s.replace("PNO", "NPO")
# for i in range(1, 1000):
#     if i*"NPO" in s:
#         print(i)


# f = open("24_demo2023.txt")
# s = f.readline()
# s = s.replace("A", "O")
# s = s.replace("C", "D")
# s = s.replace("F", "D")
# for i in range(1, 10000):
#     if i*"DO" in s:
#         print(i)


# f = open("24_aprobation2023_1.txt")
# s = f.readline()
# s = s.replace("C", "B")
# for i in range(1, 10000):
#     if i*"BBA" in s:
#         print(i*3)


# f = open("24_aprobation2023_2.txt")
# s = f.readline()
# s = s.replace("CFE", "FCE")
# for i in range(1, 10000):
#     if i*"FCE" in s:
#         print(i)


# f = open("24_open_kim2023.txt")
# s = f.readline()
# s = s.replace("A", "*")
# s = s.replace("C", "*")
# s = s.replace("B", "*")
# s = s.replace("**", "* *")
# a = s.split()
# print(len(max(a, key=len)))


f = open("24_aprobation2023_3.txt")
s = f.readline()
s = s.replace("N", "*")
s = s.replace("O", "*")
s = s.replace("P", "*")
s = s.replace("**", "* *")
s = s.replace("**", "* *")
a = s.split()
print(len(max(a, key=len)))