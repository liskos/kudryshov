import sys
sys.stdin = open("17var18.txt")

a = []
b = []
for i in range(5500):
    a.append(int(input()))

for i in range(5499):
      if a[i] < 310 and  a[i+1] < 310 :
          b.append(a[i] ** 3 + a[i+1]**3)
print(len(b),min(b))
