def f(s):
    n = 2
    while s < 45:
        s = s + 3
        n = n * 2
    return n


for i in range(1,999):
    if f(i) == 128:
        print(i)
        break