def f(d):
    n = 27
    s = 12
    while s <= 2019:
        s = s + d
        n = n + 16
    return n


a = []
for i in range(1, 999):
    if f(i) == 171:
        a.append(i)
print(a)
print(len(a))
