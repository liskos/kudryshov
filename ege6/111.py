def f(s):
    n = 40
    while s + n < 100:
        s = s + 25
        n = n - 5
    return s

for i in range(1,999):
    if f(i) == i:
        print(i)
        break