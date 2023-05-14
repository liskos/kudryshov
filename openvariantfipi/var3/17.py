import sys

sys.stdin = open("1_17.txt")
a = []
p = []
b = []
for i in range(4403):
    a.append(int(input()))
for _ in range(4403):
    if len(str(_)) == 2:
        p.append(a[_])
m = max(p)

for i in range(4402):
    if ((len(str(a[i])) == 2 and len(str(a[i+1])) != 2) or (len(str(a[i])) != 2 and len(str(a[i+1])) == 2)) and ((a[i] + a[i+1]) % m == 0):
        b.append(int(a[i] + a[i+1]))
print(len(b),max(b))


