def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(4,37):
    s = f(75,a)
    if s[-1] == 3 and s[-2] == 1  :
        print(a)


