def f(n):
    s = []
    while n > 0:
        s.append(n % 6)
        n = n // 6
    return s[::-1]

k = []
for i in range(1000,9999 + 1):
    s = f(i)
    if len(s) <= 5 and  ((s[-2] == 1 and  s[-1] == 3) or (s[-2] == 1 and  s[-1] == 4)):
        k.append(i)
print(len(k),max(k))