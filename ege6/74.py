def f(s):
    n = 10
    while s > 0:
        s = s - 15
        n = n + 3
    return n


for i in range (999,1,-1):
    if f(i) == 31:
        print(i)
        break