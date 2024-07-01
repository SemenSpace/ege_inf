file = open("26_2.txt")
kol, pod = map(int, file.readline().split())
pod_iznach = pod

gruz_s = [int(i) for i in file]
gruz_s.sort()

gruz = []
count = 0
for i in gruz_s:
    if 210 <= i <= 220:
        pod -= i
        count += 1
    else:
        gruz.append(i)

last = []
for i in range(len(gruz) - 1):
    if pod - gruz[i] >= gruz[i + 1]:
        pod -= gruz[i]
        count += 1
    else:
        print(pod)
        for j in range(i + 1, len(gruz)):
            if pod - gruz[j] >= 0:
                last.append(gruz[j])
            else:
                print(pod_iznach - (pod - max(last)), count + 1)
                exit()