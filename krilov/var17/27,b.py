import sys
sys.stdin = open("27v17_B.txt")

n = int(input())
s = 0
mr = 999999
for _ in range(n):
    a,b = sorted(map(int,input().split()))
    s += b
    if b - a < mr and b - a != 0 and (b - a) % 47 != 0 :
        mr = b-a

print(s, s % 47)
print((s - mr),(s - mr) % 47)

