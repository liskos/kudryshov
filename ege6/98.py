def f(s):
    n = 5
    while s > 5:
        s = s // 2
        n = n + 4
    return n

for i in range (999,1,-1):
    if f(i) == 29:
        print(i)
        break