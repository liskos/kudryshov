def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]


for i in range(2,37):
    s = f(68,i)
    if s[-1] == 2 and len(s) == 4:
        print(i)
