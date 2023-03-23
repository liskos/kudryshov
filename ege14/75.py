def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for i in range(2,37):
    s = f(68,i)
    l = f(94,i)
    if s[-1] == 3 and l[-1] == 3:
        print(i)

