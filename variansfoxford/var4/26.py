import sys
sys.stdin = open("EGE_26_2.txt")

n = int(input())
a = [int(input()) for _ in range (n)]
a = sorted(a,reverse=True)
print(a)
b = [a[0]]
for i in range(n):
    if a[i] <= b[-1] - 5:
        b.append(a[i])
print(len(b),b[-1])
