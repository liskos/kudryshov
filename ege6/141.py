def f(s):
    n = 1
    while s > n :
        s = s - 15
        n = n * 5
    return n

k = 0
for i in range(1,999):
    if f(i) == 125:
        k += 1
    print(k)