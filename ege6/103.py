def f(s):
    n = 5
    while n > 0:
        s = s + n
        n = n - 1
    return s

for i in range(1,999):
    if f(i) <= 550:
        print(i)
        