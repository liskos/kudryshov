def f(s):
    n = 0
    while s*s <= 101:
        s = s + 1
        n = n + 2
    return n

for i in range(1,999):
    if f(i) == 16:
     print(i)