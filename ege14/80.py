def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(1,999):
    s = f(a,6)
    l = f(a,5)
    p = f(a,11)
    if len(s) == 2 and len(l) == 3 and  p[-1] == 1 :
        print(a)

