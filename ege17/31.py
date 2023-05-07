def f(n):
    s = []
    while n > 0:
        s.append(n % 5)
        n = n // 5
    return s[::-1]

k = []
for i in range(1000,9999 + 1):
    s = f(i)
    if len(s) >= 6 and  ((s[-2] == 2 and  s[-1] == 3) or (s[-2] == 2 and  s[-1] == 1)):
        k.append(i)
print(len(k),min(k))