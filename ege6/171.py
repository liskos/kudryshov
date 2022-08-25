def f(s):
    s = s // 7
    n = 11
    while s < 130:
        if ( s + n ) % 3  == 0:
            s = s + 7
        n = n + 13
    return n

for i in range(1,999):
    if f(i) == 102:
        print(i)
        break