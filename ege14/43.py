def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(5,85):
    s = f(84,a)
    if s[-1] == 4 and s[-2] == 1  :
        print(a)

