import sys

sys.stdin = open("17data/17-299.txt")


def f(a, b, c):
    return (a == func(b) or a == func(c) or b == func(a) or b == func(c) or c == func(b) or c == func(
        a)) and a + b + c < 6771


def func(a):
    return sum(map(int, str(a)))


a = [int(input()) for i in range(8001)]
k = 0
m = 0
s = 0
for i in a:
    if i % 50 == 0:
        s += sum(map(int, str(i)))
for i in range(1, 8000):
    if f(a[i - 1], a[i], a[i + 1]):
        m = max(m, a[i - 1] + a[i] + a[i + 1])
        k += 1
print(k, m)
