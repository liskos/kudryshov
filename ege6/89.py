def f(s):
    n = 0
    while s < 275:
        s = s + 5
        n = n + 2
    return n


for i in range(-999,999):
    if f(i) < 195:
        print(i)
        break