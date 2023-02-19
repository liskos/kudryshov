import sys
sys.stdin = open("26var11.txt")

s,n = map(int,input().split())
a = [int(input()) for _ in range(n)]
a = sorted(a)
v = 0
k = 0
while v + a[0] <= s :
    b = a[0]
    v += a[0]
    a.pop(0)
    k += 1
print(k)
c = s - v + b
d = [i for i in a if i <= c]
print(max(d))


