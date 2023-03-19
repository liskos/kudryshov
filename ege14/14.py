def f(a, i):
    s = []
    while a != 0:
        s.append(a % i)
        a = a // i
    return s[::-1]


for i in range(12, 37):
    s = f(23, i)
    if str(s)[-1] == "1":
        print(i)
