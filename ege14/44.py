def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(6,62):
    s = f(61,a)
    if s[-1] == 5 and s[-2] == 1  :
        print(a)

