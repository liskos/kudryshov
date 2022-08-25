def f(s):
    s = s // 9
    n = 12
    while s < 220:
        if (s +n) % 3 == 0:
            s = s + 7
        n = n + 17
    return n

k = 0
for i in range(1,99999):
    if f(i) == 131:
        k += 1
    print(k)

