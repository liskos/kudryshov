import sys
sys.stdin = open("17.txt")

a = []
b = []
for i in range(4000):
    a.append(int(input()))

for i in range(3999):
      if abs(a[i] * a[i + 1]) == int("E",16) and ((abs(a[i]) % 10 == 6) or abs(a[i+1]) % 10 != 6) or ((abs(a[i]) % 10 != 6) or abs(a[i+1]) % 10 == 6) :
          b.append(a[i]  + a[i+1])
print(len(b),max(b))
