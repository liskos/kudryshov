def f(x):
    n = 278
    while (x + n) // 1000 < 178453:
        x = x - 3
        n = n + 5
    return n // 1000

for i in range(1,999):
    if f(i) == 915:
        print(i)