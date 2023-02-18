import sys

sys.stdin = open("17var11.txt")
a = []
m = []
b = []
for i in range(4500):
    a.append(int(input()))

for i in range(4499):
    if int(str(a[i])[-1]) % 2 == 0 and str(a[i])[-1] == str(a[i + 1])[-1]:
        m.append(abs(a[i] * a[i + 1]))
        b.append(a[i] + a[i + 1])
print(len(b), max(m))
