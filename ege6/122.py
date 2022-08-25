def f(s):
    n = 1
    while s < 200:
        s = s + 25
        n = n * 2
    return n


m = 0
k = 0
for i in range(1,999):
    if f(i) == 64:
        print(i)