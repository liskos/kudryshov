def f(s):
    n = 1
    while s < 28:
        s = s + 5
        n = n * 3
    return n


for i in range(1,999):
    if f(i) == 81:
        print(i)
        break