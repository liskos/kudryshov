def f(s):
    n = 50
    while n > 0:
        n = s // n
        s = s // 2
    return s

for i in range(1,9999):
    if f(i) == 10000:
        print(i)
        break