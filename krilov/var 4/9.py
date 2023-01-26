import sys
sys.stdin = open("9")

k = 0
for i in range  (900):
    a1,a2,a3,a4 = sorted(map(int,input().split()))
    if (a1 ** 2 > a2 + a3 + a4) and (a1 % 2 == 1 and a2 % 2 == 1 and a3 % 2 == 1 and a4 % 2 == 1) :
        k += 1
print(k)
