import sys
sys.stdin = open("17data/17-1.txt")

a = [int(input()) for _ in range(10000)]

b = []
for i in range(998):
    if a[i] > a[i + 1] < a[i + 2]:
        b.append(a[i+1])
print(len(b),max(b))


