import sys
sys.stdin = open("17var06.txt")
a = []
k = []
for i in range (5000):
    a.append(int(input()))
for i in range(4999):
    if ((a[i] > 0) and (int(a[i] ** 0.5)) ** 2 == a[i]) or (a[i+1] > 0 and (int(a[i+1] ** 0.5)) ** 2 == a[i+1]) :
        k.append(a[i] + a[i+1])
print(len(k), min(k))


