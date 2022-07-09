def f(s):
    n = 3
    while s <= 51:
        s = s + 7
        n = n * 2
    return n


for i in range(1, 51):
    if f(i) == 96:
        print(i)
        break