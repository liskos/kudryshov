import sys
sys.stdin = open("17_9372.txt")

a = [int(input()) for i in range(9999)]
b = []
c = []
for i in range(9999):
    if abs(a[i]) % 1001 == 0:
        b.append(abs(a[i]))
m = max(b)

for i in range(1,9998):
    if (len(str(abs(a[i]))) == 3 or len(str(abs(a[i+1]))) == 3) and ((a[i]+a[i+1]) > m):
        c.append(a[i]+a[i+1])

print(len(c),min(c))
