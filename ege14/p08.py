def f(n):
    a = []
    while n != 0:
        a.append(n % 5)
        n = n // 5
    return a

s = 0
for i in range(10,18):
    a = f(i)
    s = s + a.count(2)
print(s)
