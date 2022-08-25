def f(x):
    n = 1289
    while (x + n) // 1000 < 156725:
        x = x - 2
        n = n + 7
    return n // 1000

k = 0
for i in range(1,999):
    if f(i) == 327:
        k += 1
        print(k)