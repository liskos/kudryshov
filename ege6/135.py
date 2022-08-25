def f(s):
    n = - 5
    while s > 10:
        s = s - 8
        n = n + 3
    return n


for i in range(-991,999):
    if f(i) == 67:
        print(i)