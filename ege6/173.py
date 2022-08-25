def f(s):
    s = s // 9
    n = 4
    while s < 180:
        if (s +n) % 5 == 0:
            s = s + 11
        n = n + 9
    return n

for i in range(1,999):
    if f(i) == 130:
        print(i)

