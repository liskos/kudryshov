import sys
sys.stdin = open("17data/17-10.txt")


def f(n):
    s = []
    while n > 0:
        s.append(n % 7)
        n = n // 7
    return s[::-1]


a = [int(input()) for _ in range(1000)]
b = []
for i in range(999):
    if f(a[i] + a[i+1]) == f(a[i] + a[i+1])[::-1]:
         b.append(a[i] + a[i+1])

print(len(b),f(max(b)))



