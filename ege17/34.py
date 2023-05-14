def f(n):
    s = []
    while n > 0:
        s.append(n % 4)
        n = n // 4
    return s[::-1]

k = []
for i in range(1000,9999 + 1):
    s = f(i)
    if len(s) == 6 and  ((i % 3 != 0) and (i % 17 != 0) and (i % 19 != 0)):
        k.append(i)
print(len(k),min(k))