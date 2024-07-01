f = open("3.txt")
n, m = map(int, f.readline().split())
f = [int(i) for i in f]

half_disk = m // 2
k = 0

pic = []
vid = []

for i in f:
    if i >= 101:
        vid.append(i)
    else:
        pic.append(i)

ostatok_after_vid = 0
for i in sorted(vid):
    if half_disk - i >= 0:
        k += 1
        half_disk -= i
    else:
        k += 1
        ostatok_after_vid = abs(half_disk - i)
        break

os = abs(ostatok_after_vid)
dlya_pic = m // 2 - os
last = 0
ost = 0

for i in sorted(pic):
    if dlya_pic - i >= 0:
        k += 1
        dlya_pic -= i
        last = i
    else:
        ost = dlya_pic + i

mn = 0
for i in sorted(pic):
    if i <= ost:
        mn = min(mn, ost - i)
    else:
        break

print(mn, k)