def f(d):
    n = 8
    s = 6
    while s <= 1800:
        s = s + d
        n = n + 7
    return n


a = []
for i in range(1, 999):
    if f(i) == 246:
        a.append(i)
print(a)
print(len(a))
