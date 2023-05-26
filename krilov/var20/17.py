import sys
sys.stdin = open("17var20.txt")

a = []
b = []
for i in range(5500):
    a.append(int(input()))

for i in range(5499):
      if 50 <= (abs(a[i]) + abs(a[i+1])) <= 200 :
          b.append(a[i] + a[i+1])
          print(a[i],a[i+1])
print(len(b),min(b))

