def f(s):
    n = 1
    while s > 200:
        s = s - 15
        n = n + 3
    return n

for i in range(1,999):
    if f(i) == 46:
        print(i)