def f(s):
    n = 0
    while s < 1000:
        s = s * 2
        n = n + 5
    return n

for i in range(1,999):
    if f(i) == 10:
        print(i)
        break