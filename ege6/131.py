def f(s):
    n = 4
    while s <= 96:
        s = s + 8
        n = n + 5
    return n



for i in range(1,999):
    if f(i) == 54:
        print(i)