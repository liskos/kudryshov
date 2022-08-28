def f(s):
    s = s // 9
    n = 18
    while s < 150:
        if (s +n) % 5 == 0:
            s = s + 11
        n = n + 8
    return n

for i in range(1,999):
    if f(i) == 122:
        print(i)
        break
