import sys
sys.stdin = open("26var11.txt")

s,n = map(int,input().split())
a = []
for i in range (n):
    a.append(int(input()))
print(a)
a = sorted(a)
print(a)
v = 0
b = []
while v <= s :
    b.append(a[0])
    v += a[0]
    a.pop(0)
v = v - b[-1]
a.append(b[-1])
b.pop(-1)
print(len(b))
c = s - sum(b[:-1])
d = []
for i in a:
    if i <= c :
        d.append(i)
print(c,max(d))


