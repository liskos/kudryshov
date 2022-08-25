def f(s):
    s = (s + 31) // 26
    n = 813
    while s > 0:
        n = n // 3
        s = s - n
    return n

for i in range(1,99999):
    if f(i) == 30:
        print(i)
        break