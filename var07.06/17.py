import sys
sys.stdin = open("17.txt")
def f(a, b):
    return (len(str(a)) == 3 and len(str(b)) != 3)  and (a * b % m == 0)

a = [int(input()) for i in range(1000)]
m = max([i for i in a if len(str(i)) == 3])

b = []

for i in range(999):
    if f(a[i], a[i+1]) or f(a[i+1], a[i]):
        b.append(a[i] * a[i+1])

print(len(b),min(b))



