def f(s):
    n = 0
    while s + n < 450:
        s = s - 5
        n = n + 25
    return n


for i in range(1, 999):
    if f(i) <= 50:
        print(i)
        break
