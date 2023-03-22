def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(4,41):
    s = f(a,2)
    if s[-1] == 1 and  s[-2] == 1 and  s[-3] == 0 and s[-4] == 1  :
        print(a)


