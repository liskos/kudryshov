def f(s):
    n = 1
    while s < 208:
        s = s + 20
        n = n * 2
    return n

for i in range (999,1,-1):
    if f(i) == 256:
        print(i)
        break