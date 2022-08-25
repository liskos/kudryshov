def f(x):
    s = 6 * (x // 15)
    n = 1
    while s < 300:
        s = s + 18
        n = n * 2
    return n

k = 0
for i in range(1,999):
    if f(i) >= 2 and f(i) <= 500:
        k += 1
    print(k)