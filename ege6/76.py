def f(s):
    n = 105
    while n > s:
        s = s + 3
        n = n - 2
    return n


for i in range(999,1,-1):
    if f(i) == 67:
        print(i)
        break