def f(s):
    n = 1
    while s < 94 :
        s = s + 8
        n = n * 2
    return n


for i in range (94, 1, -1):
    if f(i) == 128:
        print(i)
        break