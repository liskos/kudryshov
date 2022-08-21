def f(s):
    n = 2
    while s < 500:
        s = s + 20
        n = n + 5
    return n


for i in range(1,999):
    if f(i) == 51:
        print(i)
        break