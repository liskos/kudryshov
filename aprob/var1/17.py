import sys

sys.stdin = open("KIM_0001234567_17.txt")

a = []
b = []
c = []
for i in range(10000):
    a.append(int(input()))
for i in range(10000):
    if abs(a[i]) % 3 == 0:
        c.append(a[i])

for i in range(9999):
    if (a[i] < 0 or a[i + 1] < 0) and ((a[i] + a[i + 1]) < 3330):
        b.append(a[i] + a[i + 1])
print(len(b), max(b))
print(len(c))
