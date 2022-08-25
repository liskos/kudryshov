def f(s):
    n = 100
    while s - n >= 100:
        s = s + 20
        n = n + 40

    return s

for i in range(1,999):
    if f(i) != i:
        print(i)
        break