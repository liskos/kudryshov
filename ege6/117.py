def f(d):
    n = 20
    s = 40
    while s + n < d:
        s = s - 10
        n = n - 20
    return n

k = 0
for i in range(1,999):
    if f(i) > 0:
        k += 1
    print(k)