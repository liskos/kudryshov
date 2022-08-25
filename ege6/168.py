def f(x):
    n = 1056
    while (x + n) // 1000 < 453261:
        x = x - 4
        n = n + 8
    return n // 1000

k = 0
for i in range(1,999):
    if f(i) == 515:
        k += 1
        print(k)