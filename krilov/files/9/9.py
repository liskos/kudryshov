import sys
sys.stdin = open("1.txt")

a = []
k = 0
for i in range (900):
    x = sorted(list(map(int,input().split())))
    if (x[3]**2 > x[2] * x[1] * x[0]) or ((x[1] - x[0]) == (x[2] - x[1]) == (x[3] - x[2])):
        k +=1
print(k)