def f(d):
    s = 0
    n = 0
    while n < 200:
        s = s + 64
        n = n + d
    return s

for i in range (1,999):
    if f(i) == 192:
        print(i)
        break
    