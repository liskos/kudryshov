def f(n):
    """возвращает список делителей включая 1 и само число"""
    a = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            a.append(i)
            a.append(n//i)
    a = sorted(list(set(a)))
    return a

b = []
for i in range(174457,174506):
    a = f(i)
    if len(a) == 4:
        b.append((a[1] * a[2],a[1], a[2]))
b.sort()
for e,j,k in b :
    print(j,k)