def f(s):
    n = 10
    while s > n + 20:
        s = s - 6
        n = n + 11
    return n

for i in range(1,999):
    if f(i) >= 450:
        print(i)
        break