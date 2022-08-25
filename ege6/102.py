def f(s):
    n = 1
    while n < 21:
        s = s - 1
        n = n + 2
    return s

for i in range(1,999):
    if f(i) > 600:
        print(i)
        break