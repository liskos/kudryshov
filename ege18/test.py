import sys
sys.stdin = open("18.k3.txt")

k=0
a = []
for i in range (1000):
    a.append(int(input()))
    print(a[i])