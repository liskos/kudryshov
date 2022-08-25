def f(s):
    n = 18
    while s > 0 :
        s = s - 7
        n = n + 4
    return n


for i in range(1,999):
    if f(i) == 66:
        print(i)