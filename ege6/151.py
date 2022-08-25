def f(s):
    n = 1
    while n < 1024:
        s = s + 2 * n
        n = n + s
    return n

for i in range(1,999):
    if f(i) == 1961:
        print(i)