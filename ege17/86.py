def f(n):
    a = []
    for i in (7,11,13,19):
        if n % i == 0:
            a.append(i)
    return len(a)


b = []
for i in range(20000,30000 + 1):
    if f(i) == 2:
        b.append(i)
print(len(b),sum(b) // len(b))
