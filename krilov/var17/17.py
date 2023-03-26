import sys
sys.stdin = open("17var17.txt")

a = []
b = []
for i in range(5500):
    a.append(int(input()))

for i in range(5499):
      if a[i] < 450 and  a[i+1] < 450 :
          b.append(a[i] ** 3 + a[i+1]**3)
print(len(b),max(b))
