def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(2,16):
    s = f(a,3)
    if s[-1] == 1 and  s[-2] == 2 :
        print(a)


