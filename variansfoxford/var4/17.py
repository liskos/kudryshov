import sys

sys.stdin = open("17.txt")
a = []
m = []
b = []
for i in range(5000):
    a.append(int(input()))
for _ in range(5000):
    if abs(a[_]) % 10 == 2:
        m.append(a[_])
min = min(m)

for i in range(4999):
    if ((abs(a[i]) % 10 == 2 and abs(a[i+1]) % 10 != 2) or (abs(a[i]) % 10 != 2 and abs(a[i+1]) % 10 == 2)) and (((a[i] + a[i+1]) ** 2) >= ((min) ** 2)):
        b.append(int(a[i] + a[i+1])**2)
print(len(b),max(b))


