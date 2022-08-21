def f(s):
    n = 50
    while s > 0:
        s = s // 2
        n = n - 3
    return n

for i in range (1,999):
    if f(i) == 23:
        print(i)
        break