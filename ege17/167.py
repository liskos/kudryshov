import sys
sys.stdin = open("17data/17-3.txt")

a = [int(input()) for _ in range(5001)]

b = []
for i in range(4998):
    if a[i] % 2 != a[i + 1] % 2 != a[i + 2] % 2 != a[i + 3] % 2:
        b.append(a[i] + a[i+1] + a[i + 2] + a[i + 3])

print(len(b),max(b))
