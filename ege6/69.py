def f(s):
    n = 1
    while s > 43:
        s = s - 8
        n = n * 2
    return n


for i in range(43, 999):
    if f(i) == 128:
        print(i)
        break