def f(s):
    n = 11
    while s > -9:
        s = s - 4
        n = n + 5
    return n


for i in range(-991,999):
    if f(i) == 56:
        print(i)