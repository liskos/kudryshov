def f(d):
    n = 2
    s = 0
    while s <= 365:
        s = s + d
        n = n + 5
    return n


for i in range(1, 10000):
    if f(i) == 67:
        print(i)
        break