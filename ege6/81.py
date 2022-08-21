def f(s):
    n = 5
    while s < 110:
        n = n + 1
        s = s + n
    return n


for i in range(1,999):
    if f(i)==15:
        print(i)
        break