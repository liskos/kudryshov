import sys

sys.stdin = open("17.txt")
a = []
m = []
for i in range(5000):
    a.append(int(input()))

for i in range(4999):
    if (str(a[i])[-1] == 7 and str(a[i+1])[-1] != 7) or (str(a[i])[-1] != 7 and str(a[i+1])[-1] == 7) and ((a[i] + a[i+1]) ** 2 >= min(a) ** 2):
        m.append(a[i] + a[i+1])
print(m)
