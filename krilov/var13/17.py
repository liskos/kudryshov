import sys
sys.stdin = open("17var13.txt")

a = []
b = []
for i in range(4500):
    a.append(int(input()))

for i in range(4499):
      if a[i] + a[i + 1] >= 100 and (a[i] < 0 or a[i + 1] < 0):
          b.append(a[i] * a[i + 1])
print(len(b),max(b))
