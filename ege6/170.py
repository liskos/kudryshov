def f(s):
    s = s // 7
    n = 13
    while s < 255:
        if ( s + n ) % 2  == 0:
            s = s + 11
        n = n + 7
    return n

for i in range(1,999):
    if f(i) == 90:
        print(i)
        break