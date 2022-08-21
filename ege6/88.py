def f(s):
    n = 3
    while s < 220:
        s = s + 6
        n = n + 3
    return n


for i in range(999,1,-1):
    if f(i) > 40:
        print(i)
        break