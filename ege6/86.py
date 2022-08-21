def f(s):
    n = 0
    while s < 205:
        s = s + 10
        n = n + 1
    return n


for i in range(999,1,-1):
    if f(i) == 12:
        print(i)
        break