def f(s):
    n = 5
    while s > 23:
        s = s - 5
        n = n * 2
    return n


for i in range(9999,1,-1):
    if f(i) == 320:
        print(i)
        break