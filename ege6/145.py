def f(x):
    s = 5 * (x // 10)
    n = 1
    while s < 300:
        s = s + 28
        n = n * 3
    return n

k = 0
for i in range(1,999):
    if f(i) == 243:
        k += 1
    print(k)