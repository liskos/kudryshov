def f(s):
    n = 2
    while s < 85:
        s = s + 15
        n = n * 2
    return n



for i in range(1,999):
    if f(i) == 64:
        print(i)