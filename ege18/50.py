import sys
sys.stdin = open("18.k3.txt")

k=0
a = []
for i in range (1000):
    a.append(int(input()))

max = 0
for i in range (998):
    if a[i] + a[i+1] > max:
        max = a[i] + a[i+1]
    elif a[i] + a[i+2] > max:
        max = a[i] + a[i+2]
print(max)




print(k)