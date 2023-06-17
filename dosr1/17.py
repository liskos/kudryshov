import sys
sys.stdin = open("17_7596.txt")

a = []
for i in range(10000):
    a.append(int(input()))
b = []
for i in range(10000):
    if len(str(a[i])) == 3 and a[i] % 5 == 0:
        b.append(a[i])
c = []
m = min(b)

for i in range(9999):
    if (len(str(a[i])) == 3 and len(str(a[i+1])) != 3) or (len(str(a[i])) != 3 and len(str(a[i+1])) == 3) and ((a[i] + a[i+1]) % m == 0):
        c.append(a[i] + a[i+1])
print(len(c),min(c))
