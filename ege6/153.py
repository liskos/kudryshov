def f(x):
    n = 1234
    while (x + n) // 1000 < 223456:
        x = x - 2
        n = n + 3
    return n // 1000



for i in range(223380000, 224000000):
    print(i, f(i))