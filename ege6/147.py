def f(x):
    s = 6 * (x // 5)
    n = 1
    while s < 300:
        s = s + 35
        n = n * 2
    return n

k = 0
for i in range(1,999):
    if f(i) == 64:
        k += 1
    print(k)