import sys

sys.stdin = open("1_26.txt")

k = int(input())  #Число ячеек
n = int(input())  #Число пассажиров
g = [list(map(int,input().split())) for i in range(n)]
g = sorted(g)
kk = [0] * k
z = 0
t = 0
for a,b in g :
    i = 0
    for i in range(0,k):
        if kk[i] < a:
            kk[i] = b
            z += 1
            t = i
            break
print(z,t + 1)






