def f(s):
    n = 1
    while s <= 45:
        s = s + 4
        n = n * 2
    return n


for i in range(1,46):
    if f(i) == 256:
        print(i)
        break