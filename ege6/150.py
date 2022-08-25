def f(s):
    n = 1
    sn = 0
    while n < 200:
        s = 3 * s - n
        n = n + 24
        sn = sn + (s + n)
    return abs(sn - n)


for i in range(-999,999):
    if f(i) < 100000:
        print(i)