def f(s):
    n = 740
    while s + n < 1200:
        s = s + 6
        n = n - 4
    return n


for i in range(1, 999):
    if f(i) == 68:
        print(i)
        break
