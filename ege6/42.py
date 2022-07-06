def f(d):
    n = 7
    s = 35
    while s <= 2570:
        s = s + d
        n = n + 9
    return n


a = []
for i in range(1, 999):
    if f(i) == 196:
        a.append(i)
print(a)
print(len(a))
