import sys
sys.stdin = open("26var13.txt")


s, n = map(int,input().split())
a = [int(input()) for _ in range(n)]
a.sort()
v = 0
b = []
while v + a[0] <= s:
    b.append(a[0])
    v += a[0]
    a.pop(0)
print(len(b))
k = s - sum(b[:-1])
c = [i for i in a if i <= k]
print(max(c))
