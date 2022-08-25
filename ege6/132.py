def f(s):
    n = 12
    while s > 0 :
        s = s - 10
        n = n + 7
    return n

for i in range(1,999):
    if f(i) == 61:
        print(i)