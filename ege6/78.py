def f(s):
    n = 0
    while s + n <= 300:
        s = s - 5
        n = n + 25
    return n


for i in range(999, 1, -1):
    if f(i) == 250:
        print(i)
        break