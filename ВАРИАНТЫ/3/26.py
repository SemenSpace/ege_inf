file = open("26.txt")
N = int(file.readline())

f = []
for i in file:
    s = i.split()
    f.append([int(s[0]), int(s[1]), s[2]])
f.sort()

park_A = ["0" * 1441 * 2 for i in range(80)]
park_B = ["0" * 1441 * 2 for i in range(20)]

count_A = 0
count_pokA = 0

for i in range(N):
    start, long, type_ = f[i]
    all_time = start + long

    flag = 0
    if type_ == "A":
        for x in range(len(park_A)):
            if "1" not in park_A[x][start:all_time]:
                count_A += 1
                flag = 1
                park_A[x] = park_A[x][:start] + "1" * long + park_A[x][all_time:]
                break

        if flag == 0:
            for y in range(len(park_B)):
                a = y
                if "1" not in park_B[y][start:all_time]:
                    park_B[y] = park_B[y][:start] + "1" * long + park_B[y][all_time:]
                    count_A += 1
                    flag = 1
                    break
            if flag == 0:
                count_pokA += 1


    elif type_ == 'B':
        for y in range(len(park_B)):
            if "1" not in park_B[y][start:all_time]:
                park_B[y] = park_B[y][:start] + "1" * long + park_B[y][all_time:]
                flag = 1
                break

        if flag == 0:
            count_pokA += 1

print(count_A, count_pokA)
