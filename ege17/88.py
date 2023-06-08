def f(n):
    a = []
    for i in range(10,20 + 1):
        if n % i == 0:
            a.append(i)
    return len(a)

b = []
for i in range(54123,75321 + 1):
    if f(i) == 5:
        b.append(i)
print(len(b),max(b))

