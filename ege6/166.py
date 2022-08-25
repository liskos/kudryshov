def f(x):
    n = 357
    while (x + n) // 1000 < 263542:
        x = x - 2
        n = n + 7
    return n // 1000

k = 0
for i in range(1,999):
    if f(i) == 214:
        k += 1
        print(k)