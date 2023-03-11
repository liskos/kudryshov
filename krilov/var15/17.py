import sys
sys.stdin = open("17var15.txt")

a = []
b = []
c = []
for i in range(4500):
    a.append(int(input()))

for i in range(4499):
      if a[i] > 700 or a[i+1] > 700 :
          c.append(a[i] + a[i + 1])
          b.append(a[i] ** 2 + a[i+1]**2)
print(len(c),max(b))
