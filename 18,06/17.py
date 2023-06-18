import sys
sys.stdin = open("17 (1).txt")

a = []
for i in range(10000):
    a.append(int(input()))

m = max([a[i] for i in range(10000) if len(str(a[i])) == 3])

b =[]
for i in range(0,9999):
    if ((len(str(a[i])) == 3 and len(str(a[i+1])) != 3) or (len(str(a[i])) != 3 and len(str(a[i+1])) == 3)) and ((a[i] + a[i+1]) % m == 0):
        b.append(a[i] + a[i+1])

print(len(b),max(b))
