def f(s):
    n = 121
    while s < 124:
        s = s + 10
        n = n + 17
    return n

for i in range(1,999):
    if f(i) == 291:
        print(i)