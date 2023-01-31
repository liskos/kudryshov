import sys
sys.stdin = open("17")

k=0
a = []
for i in range (4010):
    a.append(int(input()))
m = max(a)
ms = 3 * 10 ** 10
for i in range (4008):
    if (a[i] % 10 != 3 and a[i+1] % 10 != 3 and a[i+2] % 10 != 3) and a[i] ** 2 + a[i+1] ** 2 + a[i + 2] ** 2 > m:
        k += 1
        if a[i] ** 2 + a[i+1] ** 2 + a[i + 2] ** 2 < ms:
            ms = a[i] ** 2 + a[i+1] ** 2 + a[i + 2] ** 2
print(k)
print(ms)



