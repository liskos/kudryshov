def f(x):
    n = 987
    while (x + n) // 1000 < 354261:
        x = x - 5
        n = n + 8
    return n // 1000

k = 0
for i in range(1,999):
    if f(i) == 231:
        k += 1
        print(k)