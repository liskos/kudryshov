import sys
sys.stdin = open('17data/987987.txt')
a=[]
s =[]
for i in range(10000):
    a.append(int(input()))
    if a[i] % 100 == 0:
        s.append(a[i])
b = []
for i in range(9999):
    if a[i] < 0 or a[i + 1] < 0 and a[i]  + a[i + 1] < len(s):
        b.append((a[i] + a[i+1]))
print(len(b), max(b))
print(len(s))