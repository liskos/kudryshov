def f(s):
    n = 3
    while s <= 51:
        s = s + 7
        n = n * 2
    return n


for i in range(51, 1, -1):
    if f(i) == 96:
        print(i)
        break