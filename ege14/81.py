def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(1,999):
    s = f(a,7)
    l = f(a,6)
    p = f(a,13)
    if len(s) == 2 and len(l) == 3 and  p[-1] == 3 :
        print(a)

