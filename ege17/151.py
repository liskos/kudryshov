import sys
sys.stdin = open('17data/17-1.txt')
a=[]
for i in range(10000):
    a.append(int(input()))
b = []
for i in range(9999):
    if str(a[i])[-1] == '6' and a[i] % 3 == 0 or str(a[i + 1])[-1]  == '6' and a[i + 1] % 3 == 0:
        b.append(min(a[i],a[i+1]))
print(len(b), min(b))