def f(x):
    n = 4321
    while (x + n) // 1000 < 378128:
        x = x - 2
        n = n + 4
    return n // 1000

for i in range(1,999):
    if f(i) == 724:
        print(i)