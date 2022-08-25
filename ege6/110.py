def f(s):
    n = 127
    while s - n > 0:
        s = s + 15
        n = n + 20
    return s


for i in range(1, 999):
    if f(i) > 999:
        print(i)
        break
