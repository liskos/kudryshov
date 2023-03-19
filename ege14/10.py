def f(a,i):
    s = []
    while a != 0 :
        s.append(a % i)
        a = a // i
    return s[::-1]



for a in range(2,31):
    s = f(a,4)
    if s[-1] == 1 and s[-2] == 3 :
        print(a)