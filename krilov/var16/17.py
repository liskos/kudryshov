import sys
sys.stdin = open("17var16.txt")

a = []
b = []
for i in range(5500):
    a.append(int(input()))

for i in range(5499):
      if a[i] > 300 or a[i+1] > 300 :
          b.append(a[i] ** 2 + a[i+1]**2)
print(len(b),min(b))
