def f(n, i):
    a = []
    while n != 0:
        a.append(n % i)
        n = n // i
    return a[::-1]


for i in range(3, 100):
    a = f(71, i)
    if a[-1] == 3 and a[-2] == 1:
        print(i)
