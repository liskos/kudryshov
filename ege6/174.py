def f(s):
    s = s // 7
    n = 15
    while s < 211:
        if (s +n) % 5 == 0:
            s = s + 11
        n = n + 13
    return n

for i in range(1,999):
    if f(i) == 119:
        print(i)

