def f(s):
    n = 0
    while 400 < s * s:
        s = s - 1
        n = n + 3
    return n


for i in range(999,1,-1):
    if f(i) < 1000:
        print(i)
        break
