def f(x):
    s = 7 * (x // 8)
    n = 1
    while s < 300:
        s = s + 18
        n = n * 3
    return n


k = 0
for i in range(1,999):
    if f(i) == 81:
        k += 1
    print(k)
    