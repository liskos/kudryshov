import sys
sys.stdin = open('17data/17-1.txt')


def f(a, b):
    if a % 9 == 0 and b % 9 != 0 and b > 0 and b % 8 == 3:
        return True
    if a % 9 == 0 and b % 9 != 0 and b < 0 and b % 8 == 5:
        return True
    return False


a = [int(input()) for _ in range(10000)]
b = []
for i in range(9999):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        b.append(max(a[i],a[i+1]))
print(len(b), max(b))
