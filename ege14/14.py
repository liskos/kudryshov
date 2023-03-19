def f(a, i):
    s = []
    while a != 0:
        s.append(a % i)
        a = a // i
    return s[::-1]


for i in range(2, 37):
    s = f(23, i)
    if s[-1] == 1:
        print(i)
