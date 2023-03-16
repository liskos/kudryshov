def f(n, i):
    a = []
    while n != 0:
        a.append(n % i)
        n = n // i
    return a[::-1]


for i in range(3, 100):
    a = f(86, i)
    if a[-1] == 2 and a[-2] == 2:
        print(i)
