def f(x):
    n = 1635
    while (x + n) // 1000 < 465283:
        x = x - 2
        n = n + 5
    return n // 1000

for i in range(1,999):
    if f(i) == 956:
        print(i)