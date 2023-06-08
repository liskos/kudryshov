def f(n):
    a = []
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            a.append(n // i)
    return len(set(a))

b = []
for i in range(12356,76435 +1):
    if f(i) > 15:
        b.append(i)

print(len(b),max(b))


