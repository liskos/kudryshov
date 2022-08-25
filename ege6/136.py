def f(s):
    n = 20
    while n > s:
        s = s + 1
        n = n - 1
    return n

for i in range(1,999):
    if f(i) == 16:
        print(i)
        break