def f(n):
    a = []
    for i in (5,11,17,19):
        if n % i == 0:
            a.append(i)
    return len(a)


b = []
for i in range(10000,20000 + 1):
    if f(i) == 2:
        b.append(i)
print(len(b),min(b))
