def f(s):
    n = 6
    while s <= 154:
        s = s + 12
        n = n + 3
    return n



for i in range(1,999):
    if f(i) == 42:
        print(i)


