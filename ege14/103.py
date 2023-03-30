for x in range(5, 37):
    if int("441", x) + 14 == int("252", 7):
        print(x)


def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]
print(f(5,2))