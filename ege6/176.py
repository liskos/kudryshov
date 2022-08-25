def f(s):
    s = s // 11
    n = 9
    while s < 203:
        if (s +n) % 5 == 0:
            s = s + 6
        n = n + 13
    return n

k = 0
for i in range(1,9999999):
    if f(i) == 126:
        k += 1
        print(k)

