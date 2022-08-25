def f(x):
    n = 784
    while (x + n) // 1000 < 524368:
        x = x - 1
        n = n + 7
    return n // 1000

k = 0
for i in range(1,999):
    if f(i) == 352:
        k += 1
        print(k)