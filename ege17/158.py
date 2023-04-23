import sys
sys.stdin = open("17data/17-1.txt")

a = [int(input()) for i in range(10000)]
t = a[0]
k = 1
m = 1
k2 = 0
for i in range (1,10000):
    if a[i] < t :
        k+=1
    else:
        k = 1
    t = a[i]
    m = max(m,k)
    if k == 7:
        print(a[i-6:i+1])
        k2 +=1
print(m,k2)
