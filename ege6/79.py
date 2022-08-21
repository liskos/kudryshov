def f(s):
    n = 5
    while s < 110:
        s = s + n
        n = n + 1
    return n


for i in range(1,999):
    if f(i) == 15:
        print(i)
        break