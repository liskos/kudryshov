def f(s):
    s = s // 8
    n = 2
    while s <= 102:
        s = s + 4
        n = n * 2 - 1
    return n

for i in range(1,999):
    if f(i) == 257:
        print(i)