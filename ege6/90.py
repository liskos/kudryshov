def f(s):
    n = 4
    while s <= 400:
        s = s + 5
        n = n + 8
    return s

for i in range(400, 1, -1):
    if f(i) > 1000:
        print(i)
        break
