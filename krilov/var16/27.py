import sys
sys.stdin = open("27v16_B.txt")

n = int(input())
m = 0
minraz = 999999999
for i in range(n):
    a,b = map(int,input().split())
    m += max(a,b)
    k = abs(a - b)
    if k != 0 and k % 45 != 0 :
        minraz = min(minraz,k)
if m % 45 == 0:
    m = m - minraz
print(m,m % 45)