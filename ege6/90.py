def f(s):
    n = 4
    while s <= 400:
        s = s + 5
        n = n + 8
    return n

for i in range(-1000, 100000):
    if f(i) > 1000:
        print(i)

