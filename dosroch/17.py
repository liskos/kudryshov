import sys
sys.stdin = open("17.txt")

a = []
b = []
for i in range(4000):
    a.append(int(input()))

for i in range(4000):
    for j in range(i+1, 4000):
      if (abs(a[i] * a[j]) % 16 == 14) and (((abs(a[i]) % 10 == 6) and (abs(a[j]) % 10 != 6)) or ((abs(a[i]) % 10 != 6) and abs(a[j]) % 10 == 6)) :
          b.append(a[i]  + a[j])
print(len(b),max(b))
