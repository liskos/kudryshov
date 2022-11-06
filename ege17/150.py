import sys
sys.stdin = open('17data/17-1.txt')
a=[]
for i in range(10000):
    a.append(int(input()))
print(a)
b=[]
for i in range(9999):
    if (a[i] % 7 == 0 and a[i+1] % 17 != 0) or (a[i] % 17 != 0 and a[i+1] % 7 == 0):
        b.append(a[i] + a[i+1])
print(len(b), min(b))
