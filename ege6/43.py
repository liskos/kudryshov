def f(d):
    n = 14
    s = 29
    while s <= 2000:
        s = s + d
        n = n + 5
    return n


a = []
for i in range(1, 999):
    if f(i) == 69:
        a.append(i)
print(a)
print(len(a))
