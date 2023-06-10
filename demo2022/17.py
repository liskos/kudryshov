import sys
sys.stdin = open('17_4705.txt')
a = [int(input()) for i in range(5000)]
m3 = max([i for i in a if i % 10 == 3])
k = 0
m = 0
for i in range(4999):
    if ((str(a[i])[-1] == '3' and str(a[i + 1])[-1] != '3') or (str(a[i+1])[-1] == '3' and str(a[i])[-1] != '3') )and (a[i] ** 2 + a[i + 1] ** 2 >= m3 ** 2):
        k += 1
        if a[i] ** 2 + a[i + 1] ** 2 > m :
            m = a[i] ** 2 + a[i + 1] ** 2
print(k)
print(m)

