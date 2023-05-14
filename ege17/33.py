def f(n):
    s = []
    while n > 0:
        s.append(n % 3)
        n = n // 3
    return s[::-1]

k = []
for i in range(1000,9999 + 1):
    s = f(i)
    if len(s) == 8 and  ((i % 5 != 0) and (i % 7 != 0) and (i % 11 != 0)):
        k.append(i)
print(min(k),max(k))