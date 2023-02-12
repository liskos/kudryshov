import sys
sys.stdin = open("17var09.txt")
a = []
m = []
for i in range(5000):
    a.append(int(input()))

for i in range(4999):
    if a[i] % 10 == 5 and a[i+1] % 10 == 5 :
        m.append(abs(a[i] - a[i + 1]))

print(len(m),max(m))