def f(x):
    s = 12 * (x // 10)
    n = 1
    while s < 300:
        s = s + 25
        n = n * 2
    return n

k = 0
for i in range(1,999):
    if f(i) > 500:
        k += 1
    print(k)