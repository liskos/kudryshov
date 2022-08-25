def f(s):
    s = s // 5
    n = 8
    while s < 156:
        if (s +n) % 3 == 0:
            s = s + 6
        n = n + 11
    return n

for i in range(1,999):
    if f(i) == 140:
        print(i)

