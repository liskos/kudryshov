import sys
sys.stdin = open("27v17_A.txt")

n = int(input())
s = 0
for _ in range(n):
    a,b = sorted(map(int,input().split()))
    s += b
print(s, s % 47)

