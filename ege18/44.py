import sys
sys.stdin = open("18.k3.txt")

k=0
a = []
for i in range (1000):
    a.append(int(input()))

k = 0
for i in range (995):
    if a[i] < 100 or a[i+1] < 100 or a[i+2] < 100 or a[i+3] < 100:
        if a[i] + a[i + 1] < 100 or a[i] + a[i + 2] < 100 or a[i] + a[i + 3] < 100 + a[i] + a[i + 4] < 100 or a[i] + a[i + 5] < 100 or a[i] + a[i + 6] < 100:
            k += 1


print(k)