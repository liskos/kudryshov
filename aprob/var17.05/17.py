import sys
sys.stdin=open("17_8504.txt")
a=[]
b = []
n = []
for i in range(4410):
    a.append(int(input()))


for i in range (4410):
    if len(str(a[i])) == 3 and a[i] % 10 == 5:
        b.append(a[i])
m = min(b)
print(m)

for i in range(4409):
    if (len(str(a[i])) == 3 or len(str(a[i+1])) == 3) and ((a[i] + a[i+1]) % m == 0):
        n.append(a[i] + a[i+1])

print(len(n),max(n))