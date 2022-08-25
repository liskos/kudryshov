def f(x):
    n = 168
    while (x + n) // 1000 < 361234:
        x = x - 3
        n = n + 6
    return n // 1000

for i in range(1,999):
    if f(i) == 654:
        print(i)