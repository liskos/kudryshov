def f(s):
    n = 2
    while s < 64:
        s = s + 8
        n = n * 2
    return n

for i in range(1,999):
    if f(i) == 256:
        print(i)