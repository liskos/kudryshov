def f(s):
    n = 200
    while s // n >= 2:
        s = s + 5
        n = n + 5
    return s


for i in range(1,999):
    if f(i) > 99:
        print(i)
        break